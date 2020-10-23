import requests,csv,pymysql,json,time
from lxml import etree
def GetData(page):
    global count
    # 一级网址
    url = 'https://bj.ke.com/ershoufang/haidian/pg{}'.format(page)
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    # get请求(直接有返回对象)
    response = requests.get(url,headers = headers)
    # 将源代码改为标签模式
    html = etree.HTML(response.text)
    print(html)
    # 获取当前页面每个车辆自己的url
    new_url = html.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[4]/ul/li[1]/div/div[1]/a/@href')
    #print(new_url)
    # 遍历new_url,跳转至二级页面
    for i in new_url:
        url=i
        print(count + 1, '++++')
        print('第{}条数据开始下载'.format(count + 1))
        # 获取网页源代码
        response = requests.get(url, headers=headers)
        # 将源代码改为标签模式
        html = etree.HTML(response.text)
        #房源信息
        name=html.xpath('//*[@id="beike"]/div[1]/div[2]/div[2]/div/div/div[1]/h1/text()')[0]
        #房间图片
        tupian=html.xpath('//*[@id="topImg"]/div[1]/img/@src')[0]
        #参考价
        money=html.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[2]/div[2]/span[1]/text()')[0]
        #类型
        type=html.xpath('//div[@class="mainInfo"][1]/text()')[0]
        #结构
        jiegou=html.xpath('//div[@class="subInfo"]/text()')[0]
        #小区名称
        xiaoqu=html.xpath('//div[@class="communityName"]/a[1]/text()')[0]
        #所在区域
        quyu=html.xpath('//span[@class="info"]/a[1]/text()')[0]
        #房间大小
        big=html.xpath('//div[@class="area"]/div[1]/text()')[0]
        #print(name,tupian,money,type,jiegou,xiaoqu,quyu,big)
        # 建立字典,存储数据
        dic = {
            '房源信息': name,
            '房间图片': tupian,
            '参考价': money,
            '类型': type,
            '结构': jiegou,
            '小区名称': xiaoqu,
            '所在区域':quyu,
            '房间大小': big,
        }
        count += 1
        # 加入到列表里面
        allData.append(dic)
        # 存入到json数据
        data = {'count': count, 'data': allData}
        #print(data)
        with open('贝壳二手房.json', 'w', encoding='utf-8') as file:
            # 直接存入json
            json.dump(data, file, ensure_ascii=False, indent=4)
        # 表头
        header = ['房源信息', '房间图片', '参考价', '类型', '结构', '小区名称', '所在区域', '房间大小']
        # 存入csv (爬一条存一条)
        with open('贝壳二手房.csv', 'a', encoding='utf-8', newline='') as file:
            # 写入者
            csv_file = csv.DictWriter(file, header)
            if count == 1:
                # 写入表头(第一条数据的时候写入表头)
                csv_file.writeheader()
            # 写入所有数据
            csv_file.writerow(dic)
# #
        # 存入数据库 (将单引号替换为空)
        sql = "INSERT INTO beike (房源信息,房间图片,参考价,类型,结构,小区名称,所在区域,房间大小) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (name,tupian,money,type,jiegou,xiaoqu,quyu,big)
        # 执行sql
        cursor.execute(sql)

        print(name)
        print('第{}条数据下载完毕'.format(count))
        # 设置循环延时
        #time.sleep(3)
#
# 打开json文件
with open('贝壳二手房.json', 'r', encoding='utf-8') as file:
    dic = json.load(file)
    count = dic['count']
    allData = dic['data']
#
# 连接数据库
db = pymysql.connect('localhost','root','123456','text')
# 生成游标对象
cursor = db.cursor()
#
# # 开启循环
for page in range(1,2000):
    count = 0
    print('第{}页数据开始'.format(page))
    GetData(page)
    print('第{}页数据结束'.format(page))
    print('===================================')
#     #time.sleep(3)
# #
# #
# 提交操作
db.commit()
# 关闭数据库
db.close()




