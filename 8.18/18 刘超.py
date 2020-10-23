import csv
import re
# 1.检索邮箱:
# @前面可以有字母数字下划线
# @后面都不能有下划线,可以有数字或者字母
# 21312321@qq.com
# abc@163.com
# hwqeqewyh@aaaedu.cc
# a@sad.com.cc
# abc@wqeq.org
# abc_abc@abc.abc
# a@163.abc
# userInput=input('输入一个邮箱')
# partern=r'^\w+@([0-9a-z]+\.)+[0-9a-z]+$'
# result=re.search(partern,userInput)
# if result == None:
#     print('不是一个正确的邮箱地址')
# else:
#     print('是一个正确的邮箱地址')

# 2.检验身份证号:
# 18位:
# 1位不能是0
# 2-17: 纯数字
# 18: 数字或者x
# userInput=input('输入一个身份证号')
# partern=r'^([1-9]\d{5}[12]\d{3}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])\d{3}[0-9xX])$'
# result=re.search(partern,userInput)
# if result == None:
#     print('不是身份证号码')
# else:
#     print('是一个正确的身份证号')


# 3.校验网址
# 	http://www.baidu.com
# 	http://baidu.com
# 	www.baidu.com
# 	https://www.baidu.com
# 	tieba.baidu.com
# 	news.baidu.com
# 	yuan.news.baidu.com
# 	news.baidu.com.cn
# userInput=input('输入一个网址')
# partern=r'^(http?://)?[0-9a-z]{3-10}(\.[a-z0-9]{2,}){1,3}$'
# result=re.search(partern,userInput)
# if result == None:
#     print('不是一个正确的网址')
# else:
#     print('是一个正确的网址')

# 附加题:
# 4.将zhanku.html放在pycharm打开,然后取出每条数据的 作品图片url地址,作品名字,作品类型,人气数,评论数,点赞数,作者
# 如果没有该字段的数据,写无;把数据存入到csv
#
# 作品图片的url地址: <img src="图片的地址">
with open('zhanku.html','r',encoding='utf-8') as file:  #读取zhank.html文件内容
    content = file.read()
#print(content)
#图片地址
partern_img=r'target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)\s+srcset="|target="_blank" class="card-img-hover" z-st="content_ad_cover"><img src="(.+?)" title='
result_img = re.findall(partern_img,content,re.S)          #从源代码当中查找图片写正则表达式
img=[i[0] if i[0] != '' else i[1] for i in result_img]     #生成图片地址的列表
#print(img)

#作品名字
partern_name=r'class="card-img-hover" title="(.+?)\s+target="_blank" z-st="home_main_card_cover">|class="title-content" target="_blank" title="(.+?)" z-st="content_ad_title"'
result_name=re.findall(partern_name,content,re.S)                  #从源代码当中查找作品名字写正则表达式
name=[i[0] if i[0] != '' else i[1] for i in result_name]           #生成作品名字的列表
#print(name)

#作品类型
partern_type=r'<p class="card-info-type" title="(.+?)">'           #从源代码当中查找作品类型写正则表达式
result_type=re.findall(partern_type,content,re.S)                  #生成作品类型的列表
type=result_type

#人气数
partern_renqi=r'<span class="statistics-view" title="共(.+?)人气">|<span class="time" title="推广">(.+?)</span>'
result_renqi=re.findall(partern_renqi,content,re.S)                #从源代码当中查找人气数写正则表达式
renqi=[i[0] if i[0] != '' else '无' for i in result_renqi]         #生成人气数的列表
#print(renqi)


#评论数
partern_pinglun=r'<span class="statistics-comment" title="共(.+?)评论">|<span class="time" title="推广">(.+?)</span>'
result_pinglun=re.findall(partern_pinglun,content,re.S)             #从源代码当中查找评论数写正则表达式
pinglun=[]                                                          #生成评论数的列表
for i in result_pinglun:                                            #评论数生成的元组有俩种情况通过遍历写出列表
    if i[0] !='':
        pinglun.append(i[0])
    else:
        pinglun.append(i[1])
#print(pinglun)

#点赞数
partern_dianzan=r'<span class="statistics-tuijian" title="共(.+?)推荐">|<span class="time" title="推广">(.+?)</span>'
result_dianzan=re.findall(partern_dianzan,content,re.S)             #从源代码当中查找点赞数写正则表达式
dianzan=[i[0] if i[0] != '' else '无' for i in result_dianzan]        #生成点赞数的列表
#print(dianzan)

#作者
partern_author=r'<a href="[0-9a-z./:]+" title="(.+?)" target="_blank" z-st="home_main_card_user">|<span class="time" title="推广">(.+?)</span>'
result_author=re.findall(partern_author,content,re.S)                #从源代码当中查找作者写正则表达式
author=[i[0] if i[0] != '' else i[1] for i in result_author]          #生成作者的列表
#print(author)
#创建字典存储数据
data=[]
for j in range(40):
    dic={}
    dic['图片地址'] = img[j]
    dic['作品名字'] = name[j]
    dic['作品类型'] = type[j]
    dic['人气数'] = renqi[j]
    dic['评论数'] = pinglun[j]
    dic['点赞数'] = dianzan[j]
    dic['作者'] = author[j]
    data.append(dic)
# print(data)
# 开始写入数据,并把数据存入到csv
header = ['图片地址', '作品名字', '作品类型', '人气数', '评论数', '点赞数', '作者']
with open('站酷.csv', 'w', encoding='utf-8-sig', newline='') as file:
    csv_file = csv.DictWriter(file, header)   # 写入者对象
    csv_file.writeheader()                    # 写入表头
    csv_file.writerows(data)                  # 写入多条数据


