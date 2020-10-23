import requests,csv,pymysql,json,time
from lxml import etree
def GetData(page):
    global count
    # 一级网址
    url = 'http://www.tadu.com/store/98-a-0-5-a-20-p-{}-98'.format(page)
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }

    # get请求(直接有返回对象)
    response = requests.get(url,headers = headers)
    # 将源代码改为标签模式
    html = etree.HTML(response.text)
    # 获取当前页面每个书籍自己的url
    new_url = html.xpath('//ul[@class="bookList bookBgList"]/li/a/@href')
    #print(new_url)
    # 遍历new_url,跳转至二级页面
    for i in new_url:
        url = 'http://www.tadu.com/'+ i
        print(count + 1, '++++')
        print('第{}条数据开始下载'.format(count + 1))
        # 获取网页源代码
        response = requests.get(url, headers=headers)
        # with open('小说.html', 'w', encoding='utf-8') as file:
        #     file.write(response.text)
        # 将源代码改为标签模式
        html = etree.HTML(response.text)
        #print(html)
        # 获取书名
        name= html.xpath('//div[@class="bookNm"]/a/text()')[0]
        # 作者
        author=html.xpath('//div[@class="bookNm"]/span/text()')[0]
        #是否完本
        wanben=html.xpath('//div[@class="sortList"]/a/text()')[0]
        #字数
        zishu=html.xpath('//div[@class="datum"]/span[1]/em/text()')[0]
        #总人气
        renqi=html.xpath('//div[@class="datum"]/span[2]/em/text()')[0]
        #总银票
        yingpiao=html.xpath('//div[@class="datum"]/span[2]/em/text()')[0]
        #签约
        qianxue=html.xpath('//div[@class="datum"]/span[3]/em/text()')[0]
        #图片网址
        read=html.xpath('//div[@class="boxCenter bookIntro"]/a/img/@src')[0]
        #print(name,author,wanben,zishu,renqi,yingpiao,qianxue,read)
        # 建立字典,存储数据
        dic = {
            '书名': name,
            '作者': author,
            '是否完本': wanben,
            '字数': zishu,
            '总人气': renqi,
            '签约': qianxue,
            '总银票':yingpiao,
            '图片网址': read,
        }
        count += 1
        # 加入到列表里面
        allData.append(dic)
        # 存入到json数据
        data = {'count': count, 'data': allData}
        #print(data)
        with open('小说网.json', 'w', encoding='utf-8') as file:
            # 直接存入json
            json.dump(data, file, ensure_ascii=False, indent=4)

        # 表头
        header = ['书名', '作者', '是否完本', '字数', '总人气', '签约', '总银票', '图片网址']
        # 存入csv (爬一条存一条)
        with open('小说网.csv', 'a', encoding='utf-8', newline='') as file:
            # 写入者
            csv_file = csv.DictWriter(file, header)
            if count == 1:
                # 写入表头(第一条数据的时候写入表头)
                csv_file.writeheader()
            # 写入所有数据
            csv_file.writerow(dic)

        # 存入数据库 (将单引号替换为空)
        sql = "INSERT INTO xiaoshuo (书名,作者,是否完本,字数,总人气,签约,总银票,图片网址) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (name,author,wanben,zishu,renqi,qianxue,yingpiao,read)
        # 执行sql
        cursor.execute(sql)

        print(name)
        print('第{}条数据下载完毕'.format(count))
        # 设置循环延时
        #time.sleep(3)
#
# 打开json文件
with open('小说网.json', 'r', encoding='utf-8') as file:
    dic = json.load(file)
    count = dic['count']
    allData = dic['data']
#
# 连接数据库
db = pymysql.connect('localhost','root','123456','text')
# 生成游标对象
cursor = db.cursor()

# 开启循环
for page in range(1,50):
    count = 0
    print('第{}页数据开始'.format(page))
    GetData(page)
    print('第{}页数据结束'.format(page))
    print('===================================')
    #time.sleep(3)


#提交操作
db.commit()
# 关闭数据库
db.close()
