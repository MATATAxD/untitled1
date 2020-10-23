# 使用xpath解析致设计,要求10页数据
import requests
from lxml import etree
import csv
header_csv = ['作者','作品名', '作品地址', '作品类型', '观看人数', '评论人数', '点赞人数','头像']
with open('致设计.csv', 'w', encoding='utf-8-sig', newline='') as file:
    csv_file = csv.DictWriter(file, header_csv)
    csv_file.writeheader()
for page in range(1, 11):
    print('第%s页开始' % (page))
    url = 'https://www.zhisheji.com/new_index_tj'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    dic = {
        'page': page
    }
    response = requests.post(url, headers=headers, params=dic)
    content = response.text
    html = etree.HTML(content)
    div_all = html.xpath('//li')
    count = 0
    for div in div_all:
        count += 1
        url_result= div.xpath('.//a/span/img/@mysrc')[0]
        title_result= div.xpath('.//a/span/img/@alt')[0]
        type_result = div.xpath('.//div[@class="desc"]/text()')[0]
        watch = div.xpath('.//em/text()')
        watch_count_result= watch[0]
        dianzan_count_result = watch[1]
        pinglun_count_result = watch[2]
        author_result= div.xpath('.//div[@class="sjs-name"]/a/@title')[0]
        author_url_result= div.xpath('.//div[@class="sjs-name"]/a/img/@mysrc')[0]
    # print(div_all)
        dic = {
            '作者': author_result,
            '头像': author_url_result,
            '作品名': title_result,
            '作品地址': url_result,
            '作品类型': type_result,
            '观看人数': watch_count_result,
            '评论人数': pinglun_count_result,
            '点赞人数': dianzan_count_result
        }
        with open('致设计.csv', 'a', encoding='utf-8-sig', newline='') as file:
            csv_file = csv.DictWriter(file, header_csv)
            csv_file.writerow(dic)
    print('第%s页结束' % (page))