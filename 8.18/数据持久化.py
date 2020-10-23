import csv
data = [
    {
        "名字": '肖申克的救赎',
        '别名': ['The Shawshank Redemption','月黑高飞(港)','刺激1995(台)'],
        '导演': {'中文名': '弗兰克·德拉邦特','英文名': 'Frank Darabont'},
        '主演': [{'中文名': '蒂姆·罗宾斯','英文名': 'Tim Robbins'}]
    },
    {
        "名字": '霸王别姬',
        '别名': ['再见，我的妾','Farewell My Concubine'],
        '导演': {'中文名': '陈凯歌','英文名': 'Kaige Chen'},
        '主演': [{'中文名': '张国荣','英文名': 'Leslie Cheung'},{'中文名': '张丰毅','英文名': 'Fengyi Zha'}]
    }
]
for i in data:
    i['别名'] = '/'.join(i['别名'])
    i['导演'] = i['导演']['中文名'] + ' ' + i['导演']['英文名']
    list=[]
    for j in i['主演']:
        list.append('/'+j['中文名']+'/'+j['英文名'])     #转列表再转字符串
    # print(list)
    str=''.join(list)
    # print(str)
    i['主演']=str[1:]

header=['名字','别名','导演','主演']
with open('豆瓣.csv','w',encoding='utf-8-sig',newline='') as file:
    csv_file=csv.DictWriter(file,header)
    csv_file.writeheader()
    csv_file.writerows(data)