import requests,os
from lxml import etree
# 1.下载英雄联盟英雄的皮肤图片: (要求每个英雄都有一个文件夹,文件夹是该英雄的名字,文件夹里面的图片文件就是这个英雄的皮肤)
# 	https://lol.qq.com/data/info-heros.shtml
# url='https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
# header={
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
#
# }
# response = requests.get(url, headers=header)
# #print(response.text)
# all=response.json()['hero']
# for i in all:
#     print(i['heroId'],i['title'])
#     dir = 'lol/' + i['title']    #创建文件夹
#     os.mkdir(dir)
#     #皮肤的网络请求
#     hero_url= 'https://game.gtimg.cn/images/lol/act/img/js/hero/%s.js'%(i['heroId'])
#     hero_response = requests.get(hero_url, headers=header)
#     #print(hero_response.text)
#     hero_skins=hero_response.json()['skins']
#     for skin in hero_skins:
#         #图片的url地址
#         img_url=skin['mainImg']
#         if img_url=='':
#             img_url=skin['chromaImg']
#         img_response = requests.get(img_url, headers=header)
#         index=img_url.rfind('.')
#         #图片名字路径中把有/都替换成.
#         name = dir + '/'+skin['name'].replace('/','.')+img_url[index:]
#         with open(name,'wb')as file:
#             file.write(img_response.content)
#     print('%s的皮肤下载完毕'%(i['title']))

# 2.下载简历模板: (站长素材)
# 	http://sc.chinaz.com/jianli/free.html
# yiji_url='http://aspx.sc.chinaz.com/query.aspx?keyword=%E4%B8%8B%E8%BD%BD&classID=864'
# header={
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
# }
# response = requests.get(yiji_url, headers=header)
# response.encoding = 'utf-8'
# #一级页面请求
# yiji_html=etree.HTML(response.text)
# yiji_result=yiji_html.xpath('//div[@class="box col3 ws_block"]')
# print(len(yiji_result))
# os.mkdir('简历')
# for i in yiji_result:
#     erji_url=i.xpath('./a/@href')[0]
#     name=i.xpath('./a/img/@alt')[0]
#     print(erji_url,name)
#     #二级页面的请求
#     erji_response=requests.get(erji_url,headers=header)
#     erji_response.encoding='utf-8'
#     content=erji_response.text
#     html=etree.HTML(content)
#     rar_url=html.xpath('//ul[@class="clearfix"]//a/@href')[1]
#     print(rar_url)
#     rar_response=requests.get(rar_url,headers=header)
#     wenjian = '简历/'+ name + '.rar'
#     with open(wenjian,'wb')as file:
#         file.write(rar_response.content)


# 3.自己找一个图片网站(比如百度图片..),下载海量图片
#
# (按照自己在网页中的操作找出接口)

# from base import download
# # rn: 每页的数据条数
# # pn: rn * page
# userInput = input('请输入想下载的图片名称: ')
# # 所有的图片数据
# count = 0
# for page in range(1,5):
#     print('第{}页开始'.format(page))
#     url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=55&gsm=1e&1597988871073='
#     # 关键的参数
#     dic = {
#         'pn': 30 * page,
#         'rn': 30,
#         'queryWord': userInput,
#         'word': userInput
#     }
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
#     }
#     # params: get请求的字典参数
#     response = requests.get(url, headers=headers,params=dic)
#     # 服务器返回的如果是json数据,使用json()
#     content = response.json()
#
#     # 所有的数据(最后一项没有)
#     allData = content['data'][:len(content['data']) - 1]
#     for img in allData:
#         count += 1
#         imgUrl = img['hoverURL'] or img['middleURL']
#         print(count, '++++',imgUrl)
#         # 所有图片的url地址
#         # print(img['hoverURL'])
#         download(imgUrl)
#     print('第{}页开始'.format(page))



# 4.自己实现一个翻译功能: http://www.iciba.com/
# (自己找接口,自己测试参数,自己测试请求头)
userInput=input('请输入要翻译的单词')
url='http://www.iciba.com/word?'
dic={
    'w':userInput
}
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
response=requests.get(url,headers=headers,params=dic)
content=response.text
#print(content)
html=etree.HTML(content)
#print(htlm)
result=html.xpath('//ul[@class="Mean_part__1RA2V"]/li/span/text()')
result=':'.join(result)
print(result)













