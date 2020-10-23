# a=[
#     {'name':'张三','age':'18','sex':'男','地址':'北京'},
#     {'name':'李四','age':'17','sex':'男','地址':'北京'},
#     {'name':'王五','age':'19','sex':'男','地址':'北京'}
#
#
# ]
# for i in range(0,len(a)):
#     print(a[i]['name']+' ',+str(a[i]['age'])+' '+a[i]['sex']+' ',+a[i]['地址'])
a=[]
for i in range(1,4):
    print('输入第%s个人的信息'%(i))
    name=input('姓名')
    sex=input('性别')
    age=input('年龄')
    add=input('地址')
    id={
        '姓名':name,
        '性别':sex,
        '年龄':age,
        '地址':add
    }
    a.append(id)
print(a)
for i in a:
    print(i['姓名'],end='\t')
    print(i['性别'], end='\t')
    print(i['年龄'], end='\t')

