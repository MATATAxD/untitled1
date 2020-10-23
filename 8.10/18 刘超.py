# 0.任意选取豆瓣电影top250的5条数据用数据类型表示出来 (字典和列表的组合  列表包5个字典)
# a= [{
#     'name':'肖申克的救赎',
#     'aonther_name':'/ 月黑高飞(港) / 刺激1995(台)',
#     'director':'弗兰克·德拉邦特 Frank Darabont',
#     'star':'蒂姆·罗宾斯 Tim Robbins',
#     'year':'1994',
#     'country':'美国'
#     'leixing':'犯罪剧情',
#     'pingfen':'9.7',
#     'pingjia':'希望让人自由',
# },
# {
#     'name':'霸王别姬',
#     'aonther_name':'再见，我的妾',
#     'director':'陈凯歌 Kaige Chen',
#     'star':'张国荣 Leslie Cheung', '张丰毅 Fengyi Zhang',
#     'year':'1993',
#     'country':'中国'
#     'leixing':'爱情',
#     'pingfen':'9.6',
#     'pingjia':'风华绝代',
# },
#
# {
#     'name':'阿甘正传',
#     'aonther_name':'福雷斯特·冈普',
#     'director':'罗伯特·泽米吉斯 Robert Zemeckis',
#     'star':'汤姆·汉克斯 Tom Hanks',
#     'year':'1994',
#     'country':'美国'
#     'leixing':'爱情',
#     'pingfen':'9.5',
#     'pingjia':'一部美国近现代史',
# },
# {
#     'name':'这个杀手不太冷',
#     'aonther_name':'杀手莱昂',
#     'director':'吕克·贝松 Luc Besson',
#     'star':'让·雷诺 Jean Reno',
#     'year':'1994',
#     'country':'法国'
#     'leixing':'动作',
#     'pingfen':'9.4',
#     'pingjia':'怪蜀黍和小萝莉不得不说的故事',
# },
# {
#     'name':'美丽人生',
#     'aonther_name':'一个快乐的传说(港)',
#     'director':'罗伯托·贝尼尼 Roberto Benigni',
#     'star':'罗伯托·贝尼尼 Roberto Benigni',
#     'year':'1997',
#     'country':'意大利'
#     'leixing':'剧情','爱情',
#     'pingfen':'9.5',
#     'pingjia':'最美的谎言',
# },
#     ]
# 1.有字符串"key1:1|key2:2|key3:3|key4:5"处理成字典{'key1':1,'key2': 2...}
# a='key1:1|key2:2|key3:3|key4:5'
# b=a.replace('|',':')   # 把|替换成:
# list=b.split(':')
#print(list)
# c={}  #创建需要结果的字典
# for i in range(0,len(list),2):  #遍历找出key 和 value值
#     c[list[i]]=list[i+1]
# print(c)

# 2.有列表a = [11,77,22,33,88,44,55,77,88,70,30,99],将所有大于60的值保存在字典的第一个key中,将小于60的值保存在第二个key中:
# 格式: {'key1': 大于60的值列表,'key2': 小于60的值列表}
# a = [11,77,22,33,88,44,55,77,88,70,30,99]
# b={}     #创建新字典存放数据
# b['key1']=[]   #存放数据的列表也是字典的key 和对应的value值
# b['key2']=[]
# for i in a:            #遍历列表 如果大于60存入key1 小于存入key2
#     if i>60:
#         b['key1'].append(i)
#     else:
#         i<60
#         b['key2'].append(i)
# print(b)
# 3.
# 输出商品列表, 用户输入序号, 显示用户选中的商品
# 商品列表:
# products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],
#             ['wife', 10], ['wifi', 100000]]
# a.把商品列表变为:
# products = [{'name': 'iphone8', 'price': 6888}, {'name': 'MacPro', 'price': 14888}, {'name': '小米6', 'price': 2499},
#             {'name': 'Coffe', 'price': 31}....]
#
# b.在a的基础上, 页面显示: 序号 + 商品名称 + 商品价格:
#
# 1
# iphone8
# 6888
# 2
# MacPro
# 14888
# 3
# 小米6
# 2499
# ....
# c.用户输入商品的序号, 打印商品名称和价格
#
# d.如果用户输入的商品序号有误(没有该商品), 提示输入有误, 并重新输入
#
# e.用户输入Q或者q, 退出程序
# products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],['wife', 10], ['wifi', 100000]]
# products1=[]
# for i in products:
#     dic = {}
#     dic['name']=i[0]       #找出对应的下标
#     dic['price']=i[1]
#     products1.append(dic)    #添加列表
# #print(products1)
# for i in products1:
#     print(products1.index(i)+1,i['name'],i['price'])   #下标从0开始所以序号要+1
# while True:
#     try:
#         a=input('输入商品序号,输入Q或者q退出')
#         if a == 'q' or a == 'Q':
#             break
#         else:
#             a=int(a)
#             print(products1[a-1]['name'],products1[a-1]['price'])
#     except:
#         print('输入有误重新输入')

# 4.电影投票,由用户给每个电影打分,最终显示每个电影的评分(用户输入分数);
# 电影列表: list = ['囧妈','疯狂的外星人','金瓶梅','战狼','哪吒传奇','灵魂摆渡']
#
# 格式如下:
# 请给囧妈打分: 8
# 请给疯狂的外星人打分: 10
# ...
# ...
#
# 显示的结果:
# {'囧妈': 8,'疯狂的外星人': 10...}
# list = ['囧妈','疯狂的外星人','金瓶梅','战狼','哪吒传奇','灵魂摆渡']
# result={}
# for i in list:
#     a=input('请给%s打分:'%(i))
#     result[i]=a
# print(result)

# 5.车牌区域计数:
# 所有的车牌号:
# cars = ['京A88888','赣B12345','沪C76543','黑B33445','京B22445','沪A67854','黑C67890']
#
# locals ={'沪': '上海','黑': '黑龙江','赣': '江西','京': '北京'}
#
# 运行结果为:
# {'黑龙江': 2,'上海': 2,'北京': 2,'江西': 1}
# cars = ['京A88888','赣B12345','沪C76543','黑B33445','京B22445','沪A67854','黑C67890']
# locals ={'沪': '上海','黑': '黑龙江','赣': '江西','京': '北京'}
# a=[]
# dic={}    #创建结果字典
# for i in cars:    #遍历找出地名
#     a.append(i[0])
# for j in a:
#     dic[locals[j]]=a.count(j)   #找出出现次数添加
# print(dic)
# 6.zhubo = {'卢本伟': 5000000,'冯提莫': 8888,'UZI': 8000000000,'mlxg': 1000000,'letme': 88888888,'张琪格': 1000,'陈一发': 50000}
# 	a.计算主播的平均收益
# 	b.删除利益小于平均值的主播
# zhubo = {'卢本伟': 5000000,'冯提莫': 8888,'UZI': 8000000000,'mlxg': 1000000,'letme': 88888888,'张琪格': 1000,'陈一发': 50000}
# new_zhubo=[]
# sum=0
# for price in zhubo.values():
#     sum+=price
# avg=sum/len(zhubo)
# for key,value in zhubo.items():
#     if value<avg:
#         zhubo.pop(key)
# zhubo=new_zhubo
# print(zhubo)

# 7.根据以下字典,把数字的发音读出来
# dic = {
# 	'-': 'fu',
# 	'0': 'ling',
# 	'1': 'yi',
# 	'2': 'er',
# 	'3': 'san',
# 	'4': 'si',
# 	'5': 'wu',
# 	'6': 'liu',
# 	'7': 'qi',
# 	'8': 'ba',
# 	'9': 'jiu',
# 	'.': 'dian'
# }
# 运行:
# 请输入一个数: -328
# 发音为: fu san er ba
# a = input("请输入一个数:")
# dic = {
#         '-': 'fu',
#         '0': 'ling',
#         '1': 'yi',
#         '2': 'er',
#         '3': 'san',
#         '4': 'si',
#         '5': 'wu',
#         '6': 'liu',
#         '7': 'qi',
#         '8': 'ba',
#         '9': 'jiu',
#         '.': 'dian'
#     }
# for i in a:
#     print(dic[i], end=" ")

# 8.思考题(仅做思考,能实现最好!!!): 对于第7题,假如要求读出:
# 请输入一个数: -328
# 发音为: fu san 百 er 十 ba
#
# 输入一个数: 1234
# 发音为: yi 千 er 百 san 十 si
# userInput=input('输入一个数')
# dic = {
#         '-': 'fu',
#         '0': 'ling',
#         '1': 'yi',
#         '2': 'er',
#         '3': 'san',
#         '4': 'si',
#         '5': 'wu',
#         '6': 'liu',
#         '7': 'qi',
#         '8': 'ba',
#         '9': 'jiu',
#         '.': 'dian'
#     }
# fayin=['','十','百','千','万']
# #小数位
# xiaoshu=' '
# #先找到.的位置
# if ',' in userInput:
#     index=userInput.find(',')
#     #小数
#     float=userInput[index:]
#     for i in float:
#         xiaoshu+=dic[i]+' '  #dic[i]每个小数的发音
#     userInput=userInput[:index]
# #假设有负数
# fushu=''
# if '-'in userInput:   #从第二位开始截用切片：
#     userInput =userInput[1:]
#     fushu=dic['-']+' '
#
# # userInput='111'
# #整数位
# result=''
# flag=True
# #i每个数字
# for i in range(len(userInput)):
#     #发音的下标
#     index=len(userInput)-1-i
#     if userInput[i]=='0':
#         if flag==True:
#             result += dic[userInput[i]] + ' ' + fayin[index] + ' '
#             flag=False
#     else:
#         flag=True
#         result+=dic[userInput[i]]+' '+fayin[index]+' '
# a=userInput
# count=0
# a=a[::-1]
# for i in a:
#     if i=='0':
#         count+=1
#     else:   #0是不连续的
#         break
# if count >0:
#     index=result.find(fayin[count])
#     result=result[0:index+1]
# print(fushu + result + xiaoshu)








# 9.将以下字符串变为字典的格式:
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=json
# a='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=json'
# a=a.replace("?", " ").replace("=", " ").replace("&", " ")   #字符串转列表并用=和&分割
# b= a.split(" ")
# b.pop(0) # 去掉前面的https://www.baidu.com/s
# result={}
# for i in range(len(b)):   #遍历找出b的i值
#     if i % 2 == 0:
#         result[b[i]]=b[i+1]
# print(result)



# {"ie":"utf-8","f":"8","rsv_bp":"1","rsv_idx":"1","tn":"baidu","wd":"json}

#- 名片管理系统(不考虑重复)

# == == == == == == == == == == == == == == == == == == == == == == == == ==
# 名片管理系统V0.01

# 1.
# 添加一个新的名片
# 2.
# 删除一个名片(先查找, 是否删除)
# 3.
# 修改一个名片(先查找, 是否修改)
# 4.
# 查询一个名片
# 5.
# 显示所有的名片(50
# 条) [{}, {}, {}]
# 6.
# 退出系统
# == == == == == == == == == == == == == == == == == == == == == == == == ==
# 每条数据都应该有: 姓名, QQ号, 微信号, 住址
#
# -  QQ(10
# 位随机数)
# - 微信(11
# 位随机数)
# - 纯数字
#
# - 默认的50条数据在程序运行的时候随机产生
# 请输入操作序号: 5
# aaa
# 8909
# weixin
# 北京
# bbb
# 9099
# weixin
# 上海
# - 增:
# - 请输入名字, qq, 微信, 住址
# - 删
# - 请输入要删除的名字
# - 改(先查询, 再更新)
# - 请输入要修改的名字: 请输入名字, qq, 微信, 住址
#
# - 查询某一个人的数据:
# - 请输入要查询的名字:
# xing=["赵","钱","孙","李","周","吴","郑","王","冯","陈","褚","卫","蒋","沈","韩","杨","朱","秦","尤","许","何","吕","施","张","孔","曹","严","华","金","魏","陶","姜","戚","谢","邹","喻","柏","水","窦","章","云","苏","潘","奚","范","彭","郎","鲁","韦","昌","马","苗","凤","花","方","俞","任","袁","柳","酆","鲍","史","唐","费","廉","岑","薛","雷","贺","倪","汤"]
#
# ming=["涵清","星舞","秋枫","晨月","霁华","烟霏","殷云","烟岚","霏微","夕佳","思邈","紫琪","雅君","涵","鸿月","茜","雅洁","语彤","梓璇","靖怡","倾哥","清浅","疏影","茗月","醉烟","月墨","云落","桂燕","子琴", "腊梅", "芬", "莉娅", "娟娣", "艳红", "棠莉" ,"悦驰" ,"婉婷", "嘉洁" ,"彩红", "媛雪", "美芳", "束芳", "淑琳", "若瑶","莉轩", "燕齐", "昕妍", "思思" ,"玉瑶" ,"子婧" ,"爱琴", "维娟", "思娜", "欢欢" ,"鸾瑶" ,"玲丽", "旦娅", "苏娟" ,"宝琳" ,"思念","羽洁", "秋艳", "建颖" ,"泓茹", "富霞", "倩成" ,"诗茹" ,"欣瑶", "曦秀", "婷丽", "莉娜" ,"东玲" ,"巧娜" ,"佳艳" ,"蓓莉" ,"纪颖"]
#
# ["北京", "上海", "广州", "深圳", "辽宁", "天津", "四川", "广西", "山东", "山西", "西安", "云南", "新疆", "呼和浩特", "包头", "赤峰", "鄂尔多斯","呼伦贝尔", "阿拉善盟", "济南", "青岛", "烟台", "威海", "潍坊", "德州", "滨州", "东营", "聊城", "菏泽", "临沂", "北京", "上海", "天津", "重庆","淄博", "泰安", "枣庄", "日照", "莱芜", "海阳", "平度", "莱阳", "石家庄", "沧州", "承德", "秦皇岛", "唐山", "保定", "廊坊", "邢台", "衡水"]
# import random
# list_person = []
# for i in range(50):
#     dic_person = {}
#     qq = str(random.randint(1, 9))
#     for j in range(9):
#         qq = qq+str(random.randint(0, 9))
#     weixin = str(random.randint(1, 9))
#     for j in range(10):
#         weixin = weixin + str(random.randint(0, 9))
#     name = xing[random.randint(0, len(xing)-1)]+ming[random.randint(0, len(ming)-1)]
#     local1 = local[random.randint(0, len(local)-1)]
#     dic_person['name'] = name
#     dic_person['qq'] = qq
#     dic_person['vx'] = weixin
#     dic_person['local'] = local1
#     list_person.append(dic_person)
# print(list_person)
# while True:
#     print('=' * 30)
#     print('''1. 添加一个新的名片
#     2. 删除一个名片
#     3. 修改一个名片
#     4. 查询一个名片
#     5. 显示所有的名片
#     6. 退出系统''')
#     print('=' * 30)
#     yonghu = input('请输入操作序号：')
#     #显示所有名片
#     if yonghu == '5':
#         for i in list_person:
#             for j in i.values():
#                     print(j, end='     ')
#             print()
#     #添加名片
#     elif yonghu == '1':
#         dic_new = {}
#         name = input('请输入姓名：')
#         qq = input('请输入qq：')
#         vx = input('请输入微信：')
#         local1 = input('请输入地址：')
#         dic_new['name'], dic_new['qq'], dic_new['vx'], dic_new['local'] = name, qq, vx, local1
#         list_person.append(dic_new)
#     #删除名片
#     elif yonghu == '2':
#         def_name = input('输入要删除的名字：')
#         n = 0
#         for i in list_person:
#             if i['name'] == def_name:
#                 list_person.remove(i)
#                 n -= 1
#             else:
#                 n += 1
#         if n == len(list_person):
#             print('查无此人')
#     #修改名片
#     elif yonghu == '3':
#         change = input('输入要修改的名字：')
#         n = 0
#         for i in list_person:
#             if i['name'] == change:
#                 j = 0
#                 while j < 4:
#                     change1 = input('输入你要修改的项目的序号(1.姓名 2.qq 3.微信 4.地址)，输入q确定：')
#                     if change1 == '1':
#                         ch_name = input('输入修改后的名字：')
#                         i['name'] = ch_name
#                     elif change1 == '2':
#                         ch_qq = input('输入修改后的qq：')
#                         i['qq'] = ch_qq
#                     elif change1 == '3':
#                         ch_vx = input('输入修改后的微信：')
#                         i['vx'] = ch_vx
#                     elif change1 == '4':
#                         ch_dizhi = input('输入修改后的地址：')
#                         i['local'] = ch_dizhi
#                     elif change1 == 'q':
#                         break
#                     j += 1
#                 print(i)
#                 n -= 1
#             else:
#                 n += 1
#         if n == len(list_person):
#             print('查无此人')
#
#     #查询名片
#     elif yonghu == '4':
#         n = 0
#         find = input('输入要查找的名字：')
#         for i in list_person:
#             if i['name'] == find:
#                 print(i['name'], i['qq'], i['vx'], i['local'])
#                 n -= 1
#             else:
#                 n += 1
#         if n == len(list_person):
#             print('查无此人')
#
#     elif yonghu == '6':
#         print('退出成功')
#         break
import random
# 提示文字
msg = '''==================================================
   名片管理系统 V0.01
 1. 添加一个新的名片
 2. 删除一个名片 (先查找,是否删除)
 3. 修改一个名片 (先查找,是否修改)
 4. 查询一个名片 
 5. 显示所有的名片 (50条) [{},{},{}]
 6. 退出系统
=================================================='''
print(msg)

# 姓
xing = ["赵","钱","孙","李","周","吴","郑","王","冯","陈","褚","卫","蒋","沈","韩","杨","朱","秦","尤","许","何","吕","施","张","孔","曹","严","华","金","魏","陶","姜","戚","谢","邹","喻","柏","水","窦","章","云","苏","潘","奚","范","彭","郎","鲁","韦","昌","马","苗","凤","花","方","俞","任","袁","柳","酆","鲍","史","唐","费","廉","岑","薛","雷","贺","倪","汤"]
# 名
ming = ["涵清","星舞","秋枫","晨月","霁华","烟霏","殷云","烟岚","霏微","夕佳","思邈","紫琪","雅君","涵","鸿月","茜","雅洁","语彤","梓璇","靖怡","倾哥","清浅","疏影","茗月","醉烟","月墨","云落","桂燕","子琴", "腊梅", "芬", "莉娅", "娟娣", "艳红", "棠莉" ,"悦驰" ,"婉婷", "嘉洁" ,"彩红", "媛雪", "美芳", "束芳", "淑琳", "若瑶","莉轩", "燕齐", "昕妍", "思思" ,"玉瑶" ,"子婧" ,"爱琴", "维娟", "思娜", "欢欢" ,"鸾瑶" ,"玲丽", "旦娅", "苏娟" ,"宝琳" ,"思念","羽洁", "秋艳", "建颖" ,"泓茹", "富霞", "倩成" ,"诗茹" ,"欣瑶", "曦秀", "婷丽", "莉娜" ,"东玲" ,"巧娜" ,"佳艳" ,"蓓莉" ,"纪颖"]
# 地址
addrs = ["北京", "上海", "广州", "深圳", "辽宁", "天津", "四川", "广西", "山东", "山西", "西安", "云南", "新疆", "呼和浩特", "包头", "赤峰", "鄂尔多斯","呼伦贝尔", "阿拉善盟", "济南", "青岛", "烟台", "威海", "潍坊", "德州", "滨州", "东营", "聊城", "菏泽", "临沂", "北京", "上海", "天津", "重庆","淄博", "泰安", "枣庄", "日照", "莱芜", "海阳", "平度", "莱阳", "石家庄", "沧州", "承德", "秦皇岛", "唐山", "保定", "廊坊", "邢台", "衡水"]
# 所有的名片 [{},{},{}]
allData = []
# 生成50条数据
for i in range(50):
    # 姓名
    name = random.choice(xing) + random.choice(ming)
    # qq
    qq = random.randint(1000000000,9999999999)
    # 微信
    wechat = random.randint(10000000000,99999999999)
    # 地址
    addr = random.choice(addrs)
    dic = {'姓名': name,'qq': qq,'微信': wechat,'地址': addr}
    allData.append(dic)
print(len(allData))

# 一个名片  {'姓名': xxx,'qq': xxxxx,'微信': xxxxx,'地址': xxxxc}


while True:
    userInput = input('请输入操作序号: ')
    if userInput == '1':
        # 添加名片
        name = input('请输入要添加的姓名:')
        qq = input('请输入要添加的qq:')
        wechat = input('请输入要添加的微信:')
        addr = input('请输入要添加的地址:')
        # 输入的数据拼凑成一个字典
        dic = {'姓名': name, 'qq': qq, '微信': wechat, '地址': addr}
        # 加入到总的数据里面
        allData.append(dic)
        print('添加成功!!!')
    if userInput == '2':
        pass
    if userInput == '3':
        pass
    if userInput == '4':
        # 查询
        name = input('请输入要查询的姓名: ')
        flag = True
        for person in allData:
            if name in person['姓名']:
                flag = False
                for data in person.values():
                    print(data, end='\t')
                print()
        # 如果flag的值还是True,说明没有找到该人
        if flag:
            print('查无此人')
    if userInput == '5':
        # 显示所有
        for person in allData:
            # person: 每一张名片
            for data in person.values():
                print(data,end='\t')
            print()
            # print(person)
            # print(person['姓名'],end='\t')
            # print(person['qq'],end='\t')
            # print(person['微信'],end='\t\t')
            # print(person['地址'])
    if userInput == '6':
        print('退出操作!!!')
        break


