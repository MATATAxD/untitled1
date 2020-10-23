import requests,csv,pymysql,json
from lxml import etree
def getData(page):
    global count
    url='https://bj.zu.anjuke.com/?from=navigation'
    dic={
        'p':page
    }
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'

    }
    response = requests.get(url, headers=headers, params=dic)
    # 源代码
    content = response.text
    # with open('1.html','w',encoding='utf-8') as file:
    #     file.write(content)
    # 把代码字符串转换成标签对象
    html = etree.HTML(content)
    # 先拿到每条数据的标签
    divElements = html.xpath('//*[@id="list-content"]/div')
    #print(len(divElements))
    for div in divElements:
        #从当前标签元素获取数据
        url = div.xpath('//*[@id="list-content"]/div[3]/a/img/@src')[0]             #图片地址
        title = div.xpath('//*[@id="list-content"]/div[3]/div[1]/h3/a/b/text()')[0]     #房源
        big=div.xpath('//*[@id="list-content"]/div[3]/div[1]/p[1]/b[3]/text()')[0]      #房间大小
        louceng=div.xpath('//*[@id="list-content"]/div[3]/div[1]/p[1]/text()[5]')[0]     #楼层位置
        address=div.xpath('//*[@id="list-content"]/div[3]/div[1]/address/a/text()')[0]     #地址
        type=div.xpath('//*[@id="list-content"]/div[3]/div[1]/p[2]/span[1]/text()')[0]     #租房类型
        direction=div.xpath('//*[@id="list-content"]/div[3]/div[1]/p[2]/span[2]/text()')[0]    #房间朝向
        price=div.xpath('//*[@id="list-content"]/div[3]/div[2]/p/strong/b/text()')[0]          #价格
        dic={
            '图片地址':url,
            '房源':title,
            '房间大小':big,
            '楼层位置':louceng,
            '地址':address,
            '租房类型':type,
            '房间朝向':direction,
            '价格':price,

        }
        # 加入到列表里面
        allData.append(dic)
        # 存入到json数据
        data = {'data': allData}
        #print(data)
        with open('安居客.json','w',encoding='utf-8') as file:
            # 直接存入json
            json.dump(data,file,ensure_ascii=False,indent=4)
        # 次数+1
        count += 1
        print(count, '++++')
        # 存入数据库
        sql = "INSERT INTO anjuke (房源,图片地址,房间大小,楼层位置,地址,租房类型,房间朝向,价格) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (title,url,big,louceng,address,type,direction,price)
        print(sql)
        # 执行sql
        cursor.execute(sql)
        # 表头
        header = ['图片地址', '房源', '房间大小', '楼层位置', '地址', '租房类型', '房间朝向','价格']
        # 存入csv (爬一条存一条)
        with open('安居客.csv', 'a', encoding='utf-8-sig', newline='') as file:
            # 写入者
            csv_file = csv.DictWriter(file, header)
            if count == 1:
                # 写入表头(第一条数据的时候写入表头)
                csv_file.writeheader()
            # 写入所有数据
            csv_file.writerow(dic)

count = 0
# 连接数据库
db = pymysql.connect('localhost','root','123456','text')
# 生成游标对象
cursor = db.cursor()
# 所有的数据
allData = []
for page in range(1,20):
    print('第{}页开始'.format(page))
    # 爬取一页的代码
    getData(page)
    print('第{}页结束'.format(page))

#提交操作
db.commit()
# 关闭数据库
db.close()




