# 使用xpath解析站酷,要求10页数据
import requests
from lxml import etree
import csv
header_csv = ['作者', '头像', '作品名', '作品地址', '作品类型', '观看人数', '评论人数', '点赞人数']
with open('站酷.csv', 'w', encoding='utf-8-sig', newline='') as file:
    csv_file = csv.DictWriter(file, header_csv)
    csv_file.writeheader()
for page in range(1, 11):
    print('第%s页开始' % (page))
    url = 'https://www.zcool.com.cn/?'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    dic = {
        'page': page
    }
    response = requests.get(url, headers=header, params=dic)
    content = response.text
    html = etree.HTML(content)
    div_all = html.xpath('//div[@class="card-box"]')
    count = 0
    for div in div_all:
        count += 1
        url_result = div.xpath('./div/a/img/@src')[0]
        title_result = div.xpath('./div/a/img/@title')[0]
        type_result = div.xpath('.//p[@class="card-info-type"]/text()')[0]
        watch_count_result = div.xpath('.//p[@class="card-info-item"]/span[1]/text()')
        if len(watch_count_result) > 0:
            watch_count_result = watch_count_result[0]
        else:
            watch_count_result = "无"
        pinglun_count_result = div.xpath('.//p[@class="card-info-item"]/span[2]/text()')
        if len(pinglun_count_result) > 0:
            pinglun_count_result = pinglun_count_result[0]
        else:
            pinglun_count_result = "无"
        dianzan_count_result = div.xpath('.//p[@class="card-info-item"]/span[3]/text()')
        if len(dianzan_count_result) > 0:
            dianzan_count_result = dianzan_count_result[0]
        else:
            dianzan_count_result = "无"
        author_result = div.xpath('.//span[@class="user-avatar showMemberCard"]/a/@title|.//div[@class="card-item"]/a/text()')[0]
        author_url_result = div.xpath('.//span[@class="user-avatar showMemberCard"]/a/img/@src')
        if len(author_url_result) > 0:
            author_url_result = author_url_result[0]
        else:
            author_url_result = "无"
        # 数据
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
        with open('站酷.csv', 'a', encoding='utf-8-sig', newline='') as file:
            csv_file = csv.DictWriter(file, header_csv)
            csv_file.writerow(dic)
    print('第%s页结束' % (page))