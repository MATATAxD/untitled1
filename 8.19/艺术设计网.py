import re
import csv
with open('设计中国.html','r',encoding='utf-8') as file:
    content = file.read()
#print(content)

#图片地址
partern_img=r'<div class="pi_person_box">\s+<a target="_blank" href=".+?">\s+<img src="(.+?)" alt="'
result_img = re.findall(partern_img,content,re.S)
img=result_img
#print(result_img,len(img))

#作品名字
partern_name=r'class="img_box">\s+<img src="(.+?)"\s+alt="(.+?)"\s+class="zoom zoom_jzxs"'
name=re.findall(partern_name,content,re.S)
name=[i[1] for i in name]
#print(name,len(name))

#作者/
partern_aothor=r'<div class="pi_person_box">\s+<a target="_blank" href=".+?">\s+<img src="(.+?)" alt="(.+?)" class="pi_person">\s+</a>'
result_name = re.findall(partern_aothor,content,re.S)
aothor=result_name
#print(aothor,len(aothor))
aothor=[i[1] for i in aothor]
#print(aothor,len(aothor))

#作品类型
partern_type=r'<span class="sort_pm ">(.+?)</span>'
result_type = re.findall(partern_type,content,re.S)
type=result_type
#print(len(result_type))

#人气数
partern_renqi=r'<span class="iconBox icon_liulan"></span>\s+<span class="icon_num">(.+?)</span>'
result_renqi = re.findall(partern_renqi,content,re.S)
renqi=result_renqi
#print(len(result_renqi))

#点赞数
partern_dianzan=r'<div class="ph_lists_box">\s+<span class="iconBox icon_zan"></span>\s+<span class="icon_num">(.+?)</span>'
result_dianzan = re.findall(partern_dianzan,content,re.S)
dianzan=result_dianzan
#print(len(result_dianzan))

#评论数
partern_pinglun=r'<div class="ph_lists_box">\s+<span class="iconBox icon_pinglun"></span>\s+<span class="icon_num">(.+?)</span>'
result_pinglun = re.findall(partern_pinglun,content,re.S)
pinlun=result_pinglun
#print(len(result_pinglun))
#
data=[]
for j in range(24):
    dic={}
    dic['图片地址'] = img[j]
    dic['作品名字'] = name[j]
    dic['作品类型'] = type[j]
    dic['人气数'] = renqi[j]
    dic['评论数'] = pinlun[j]
    dic['点赞数'] = dianzan[j]
    dic['作者']   = aothor[j]
    data.append(dic)
#print(data)
header = ['图片地址', '作品名字', '作品类型', '人气数', '评论数', '点赞数', '作者']
with open('艺术设计网.csv', 'w', encoding='utf-8-sig', newline='') as file:
    csv_file = csv.DictWriter(file, header)   # 写入者对象
    csv_file.writeheader()                    # 写入表头
    csv_file.writerows(data)                  # 写入多条数据
