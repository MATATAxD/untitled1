import csv,re
import urllib.request
# 1.站酷: https://www.zcool.com.cn/
# 把该网站的数据保存400条下来;格式和周五要求的格式一样
# urls=['https://www.zcool.com.cn/','https://www.zcool.com.cn/?p=2#tab_anchor','https://www.zcool.com.cn/?p=3#tab_anchor','https://www.zcool.com.cn/?p=4#tab_anchor','https://www.zcool.com.cn/?p=5#tab_anchor','https://www.zcool.com.cn/?p=6#tab_anchor','https://www.zcool.com.cn/?p=7#tab_anchor','https://www.zcool.com.cn/?p=8#tab_anchor','https://www.zcool.com.cn/?p=9#tab_anchor','https://www.zcool.com.cn/?p=10#tab_anchor']
# count=0
# for i in urls:
#     url=i
#     count += 1
#     header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
#     request = urllib.request.Request(url, headers=header)
#     response = urllib.request.urlopen(request)
#     data = response.read().decode()
#    #print(data)
#     with open('zhanku.html', 'w', encoding='utf-8',newline='') as file:
#         file.write(data)
#     with open('zhanku.html', 'r', encoding='utf-8') as file:
#         content=file.read()
#     pattern=r'<div class="card-box">(.+?)</div>\s+</div>'
#     result = re.findall(pattern,content,re.S)
#     #print(result)
#     data=[]
#     for j in result:
#         pattern = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
#         urlAndTitleResult = re.findall(pattern,j,re.S)[0]
#     # url地址
#         url = urlAndTitleResult[1] or urlAndTitleResult[4]
#     # 作品名
#         title = urlAndTitleResult[2] or urlAndTitleResult[5]
#     # 作品类型
#         pattern = r'<p class="card-info-type" title="(.+?)">'
#         typeResult = re.findall(pattern,j,re.S)[0]
#     # 人气数 (38)
#         pattern = r'<span class="statistics-view" title="共(.+?)人气">'
#         fansResult = re.findall(pattern,j,re.S)
#     # 说明有数据
#         if len(fansResult) > 0:
#            fansResult = fansResult[0]
#         else:
#            fansResult = '无'
#     # 评论数
#         pattern = r'<span class="statistics-comment" title="共(.+?)评论">'
#         pinglunResult = re.findall(pattern, j, re.S)
#         if len(pinglunResult) > 0:
#              pinglunResult = pinglunResult[0]
#         else:
#              pinglunResult = '无'
#     # 点赞数
#         pattern = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
#         dianzanResult = re.findall(pattern, j, re.S)
#         if len(dianzanResult) > 0:
#             dianzanResult = dianzanResult[0]
#         else:
#             dianzanResult = '无'
#     # 作者
#         pattern = r'(<div class="card-item">\s+<span class=".+?">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(<div class="card-item">\s+<a href=".+?" title="(.+?)")'
#         author_result = re.findall(pattern, j, re.S)[0]
#         author = author_result[1]
#         if author == '':
#             author = author_result[3]
#     # 每条数据的字典
#         dic = {
#         'url地址': url,
#         '作品名': title,
#         '作品类型': typeResult,
#         '人气数': fansResult,
#         '评论数': pinglunResult,
#         '点赞数': dianzanResult,
#         '作者': author
#     }
#         data.append(dic)
#     header = ['url地址', '作品名', '作品类型', '人气数', '评论数', '点赞数', '作者']
#     with open('站酷.csv', 'a', encoding='utf-8-sig', newline='') as file:
#         csv_file = csv.DictWriter(file, header)
#         csv_file.writeheader()
#         csv_file.writerows(data)

# 2.致设计: https://www.zhisheji.com/
# 保存该网页的第一页的数据,存入到csv
url='https://www.zhisheji.com/'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
request = urllib.request.Request(url, headers=header)
response = urllib.request.urlopen(request)
data=response.read().decode()
#print(data)
with open('致设计.html','w',encoding='utf-8',newline='') as file:
    file.write(data)
with open('致设计.html','r',encoding='utf-8',newline='') as file:
    content=file.read()
pattern=r'<li id=".+?">(.+?)</div>\s+</div>\s+</li>'
result = re.findall(pattern,content,re.S)
#print(result,len(result))
data=[]
for i in result:
    pattern=r'class="img-box"><img class="previews" mysrc="(.+?)" src="" alt="(.+?)"' #图片地址作品名字
    result=re.findall(pattern,i,re.S)[0]
    img=result[0]
    name= result[1]
    pattern = r'<div class="desc">(.+?)</div>'               #作品类型
    leixing = re.findall(pattern, i, re.S)[0]
    pattern = r'href=".+?" title="(.+?)"'                    #标题作者
    result2 = re.findall(pattern, i, re.S)
    biaoti = result2[0]
    author = result2[1]
    pattern = r'<div class="info">\s+<em><span class="icon-view"></span>(.+?)</em>\s+<em><span class="icon-praise"></span>(.+?)</em>\s+<em><span class="icon-comment"></span>(.+?)</em>\s+</div>'
    result3 = re.findall(pattern, i, re.S)[0]          #人气点赞评论
    renqi = result3[0]
    dianzan = result3[1]
    pinglun = result3[2]

    dic={
        '图片地址':img,
        '作品名字':name,
        '作品类型':leixing,
        '点赞':dianzan,
        '评论':pinglun,
        '人气':renqi,
        '作者':author
    }
    data.append(dic)
header=['图片地址','作品名字','作品类型','点赞','评论','人气','作者']
with open('致设计.csv','w',encoding='utf-8',newline='') as file:
    csv_file = csv.DictWriter(file, header)
    csv_file.writeheader()
    csv_file.writerows(data)






