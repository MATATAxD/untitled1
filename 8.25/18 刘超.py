from selenium import webdriver
import time,pymysql,csv,json
from lxml import etree

# 1.使用selenium将致设计的数据爬取5页,并将数据保存为 csv,mysql,json
# 	https://www.zhisheji.com/
header_csv=['作者','作品名', '图片地址', '作品类型', '观看人数', '评论人数', '点赞人数','头像']
#创建csv文件
with open('致设计.csv','w',encoding='utf-8',newline='')as file:
    csv_file = csv.DictWriter(file, header_csv)
    csv_file.writeheader()
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.zhisheji.com/')
content=driver.page_source
#连接数据库
db=pymysql.connect('localhost','root','123456','text')
#创建游标对象
cursor = db.cursor()
#print(content)
content=driver.page_source
    with open('致设计.html','w',encoding='utf-8')as file:
        file.write(content)
    html=etree.HTML(content)
    #print(html)
    li_all=html.xpath('//*[@id="li_1505544"]/li')
    for li in li_all:
        # 图片地址
        url_img = li.xpath('//*[@id="li_1505544"]/a/span/img')
        #作品名字
        title=li.xpath('//*[@id="li_1505544"]/h3/a')
        # 作者
        author = li.xpath('//*[@id="li_1505544"]/div[3]/div/a/text()')
        # 观看人数
        watch = li.xpath('//*[@id="li_1505544"]/div[2]/em[1]/text()')
        # 点赞人数
        dianzan = li.xpath('//*[@id="li_1505544"]/div[2]/em[2]/text()')
        # 评论人数
        pinglun = li.xpath('//*[@id="li_1505544"]/div[2]/em[3]/text()')
        # 头像
        touxiang = li.xpath('//*[@id="li_1505544"]/div[3]/div/a/img')
        # 作品类型
        type = li.xpath('//*[@id="li_1505544"]/div[1]')
        dic={
            '作者': author,
            '作品名字' : title,
            '图片地址' : url_img,
            '观看人数': watch,
            '评论人数': pinglun,
            '点赞人数': dianzan,
            '头像'    : touxiang,
            '作品类型': type
            }
        with open('致设计csv', 'a', encoding='utf-8-sig', newline='')as file:
            csv_file=csv.DictWriter(file, header_csv)
            csv_file.writerow(dic)
        with open('致设计.json', 'a', encoding='utf-8', newline='')as file:
            json.dump(dic, file, ensure_ascii=False, indent=4)
        sql = "insert into zhisheji (作者,作品名字,头像,图品地址,作品类型,观看人数,点赞人数,评论人数) values ('%s','%s','%s','%s','%s','%s','%s','%s')"%(author,title,touxiang,url_img,type,watch,dianzan,pinglun)
        cursor.execute(sql)
        db.comit()
    # print('从%s页结束'%(i))
        btn = driver.find_element_by_xpath('//*[@id="istj"]/div/div/a[6+i-1]/span'%(i))
        btn.click()
        time.sleep(2)
        print('从%s页结束' % (i))
db.close()
driver.quit()



# 2.以所学的selenium知识点,将古诗文网我的模块里面的所有诗爬取出来: (输入验证码)
# https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx
# driver = webdriver.Chrome('chromedriver.exe')
# driver.get('https://so.gushiwen.org/user/collect.aspx')
# userInput=driver.find_element_by_xpath('//*[@id="email"]')     #输入账号
# userInput.send_keys('15619908257')
# userInput1=driver.find_element_by_xpath('//*[@id="pwd"]')      #输入密码
# userInput1.send_keys('123456')
# userInput2=driver.find_element_by_xpath('//*[@id="code"]')     #输入验证码
# yanzhenma=input('输入验证码:')
# userInput2.send_keys('%s'%(yanzhenma))
# btn = driver.find_element_by_xpath('//*[@id="denglu"]')         #登录
# btn.click()
# time.sleep(2)
# with open('古诗文.html','w',encoding='utf-8')as file:            #数据存储为html
#     file.write(driver.page_source)
# driver.quit()


