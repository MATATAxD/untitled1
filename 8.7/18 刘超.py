score = [68, 87, 92, 100,100, 76,100,100, 88,100, 54, 89, 76, 61]
# 1.查询score列表中成绩是满分的所有的学生学号
# for i in range(len(score)):
#     if score[i]==100:
#         print(i+1,end=' ')

# 2.删除score列表中所有的数值100
# a=score.count(100)
# # print(a)
# # for i in range(a):
# #     score.remove(100)
# # print(score)
# 3.有一个字符串,凡是出现"|"和 " "和 "-"和"," 前后,就算一个单词. 计算下列字符串  str = "hello world,a|nd python or and ddd and hello hello world and python or and dd-dddd and,hello wo|rld and python or and ddd and wor-ld and py-thon or and ddd and an|d ddd and" 单词的个数
str="hello world,a|nd python or and ddd and hello hello world and python or and dd-dddd and,hello wo|rld and python or and ddd and wor-ld and py-thon or and ddd and an|d ddd and"
# a=str.split("|")
# a_num=len(a)-1
# b=str.split("-")
# b_num=len(b)-1
# c=str.split(",")
# c_num=len(c)-1
# word=str.split(" ")
# word_num=a_num+b_num+c_num
# print('字符串总共有:%s个'%(word_num))
# a="hello world,a|nd python or and ddd and hello hello world and python or and dd-dddd and,hello wo|rld and python or and ddd and wor-ld and py-thon or and ddd and an|d ddd and"
# a=a.replace('|',' ').replace('-',' ').replace(',',' ')
# result=a.count(' ')+1
# print(result)
#4.编写程序，完成以下要求：
	# -  统计字符串中，各个字符的个数
	# -  比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
# word=input('输入字符串')
# word1=''
# for i in word:
#     if i not in word1:
#         word1+=i
#         a=word.count(i)
#         print('%s:%s'%(i,a),end='\t')
# 5.给定一个带文件后缀名的字符串,要求: 将后缀名输出来 例如:  aasd.sad.sas.da?sdasdsaa.txt  --> txt
# a=input('输入带文件名字符串')
# b=a.rfind('.')
# for i in range(b+1,len(a)):
#     print(a[i],end='')
# 6.用户输入一堆字符串,打印出最后一个单词的长度 asdsa adasd asdsadas asdsadeasd asdsad
# a=input('输入字符串')
# b=a.split()
# word=b[len(b)-1]
# len=len(word)
# print('最后一个单词的长度:',len)
#7.用for循环打印一个菱形. 用center()做
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#  *********
#   *******
#    *****
#     ***
#      *
# for i in range(1,12,2):
#     a='*'*i
#     print(a.center(11))
# for i in range(9,0,-2):
#     a='*'*i
#     print(a.center(11))
# 8.要求用户输入字符串,计算一个字符串中所有英文字母的个数.'dsaas12312asdas12312dsadsadsadas'
# a=input('输入字符串')
# count=0
# for i in a:
#     if i in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
#         count+=1
# print('字符串中所有英文字母的个数:%s'%(count))
# 9.模拟游戏聊天框,用户能一直输入内容,按回车,打印出用户输入的内容,但是,如果输入的内容当中,有敏感词汇,替换为 *
# 敏感词汇为:  ['sb','SB','sB','Sb','苍老师','你大爷','尼玛','马化腾']
# while True:
#     a=input('输入内容')
#     b=['sb','SB','sB','Sb','苍老师','你大爷','尼玛','马化腾']
#     for i in b:
#         a=a.replace(i,'*'* len(i))
#     print(a)

# 10.已知字符串 a = “aAsmr3idd4bgs7Dlsf9eAF”,要求如下
# 	- 请将a字符串的大写改为小写，小写改为大写。
# 	- 请将a字符串的数字取出，并输出成一个新的字符串。
# 	- 请去除a字符串多次出现的字母，仅留最先出现的一个。例 ‘abcabb’，经过去除后，输出 ‘abc’
# 	- 请将a字符串反转并输出。例：’abc’的反转是’cba’
# 	- 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）(难)
# 	- 请判断 ‘boy’里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
# 	- 输出a字符串出现频率最高的字母
a='aAsmr3idd4bgs7Dlsf9eAF'
# b=a.swapcase()
# print(b)
# 	- 请将a字符串的数字取出，并输出成一个新的字符串。
# shuzi=''
# for i in a:
#     if i not in 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM':
#         shuzi+=i
# print(shuzi)
# 	- 请去除a字符串多次出现的字母，仅留最先出现的一个。例 ‘abcabb’，经过去除后，输出 ‘abc’
# c=''
# for j in a:
#     if j not in c:
#         c+=j
# print(c)
# 	- 请将a字符串反转并输出。例：’abc’的反转是’cba
# d = ""
# for x in range(len(a)-1, -1, -1):
#     d += a[x]
# print(d)
# 	- 请判断 ‘boy’里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
# b='boy'
# flag=True
# for i in b:
#     if i not in a:
#         flag=False
#         break
# print(flag)
# 	- 输出a字符串出现频率最高的字母
# max=0
# for i in a:
#     if a.count(i)>max:
#         max=a.count(i)
# result=[]
# for i in a:
#     if a.count(i)==max and i not in result:
#         result.append(i)
# print(result)
# # 	- 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）(难)
# s=''
# for i in a:
#     if i.isalpha():
#         s+=i
# result=''
# #chr()将数字转化为字母
# for i in range(65,91):
#     upper=chr(i)*s.count(chr(i))
#     lower=chr(i+32)*s.count(chr(i+32))
#     result+=upper+lower
# print(result)




# 11.题目描述：
# 密码是我们生活中非常重要的东东，我们的那么一点不能说的秘密就全靠它了。哇哈哈. 接下来渊子要在密码之上再加一套密码，虽然简单但也安全。
# 假设渊子原来一个BBS上的密码为zvbo9441987,为了方便记忆，他通过一种算法把这个密码变换成YUANzhi1987，这个密码是他的名字和出生年份，怎么忘都忘不了，而且可以明目张胆地放在显眼的地方而不被别人知道真正的密码。
# 他是这么变换的，大家都知道手机上的字母： 1–1， abc–2, def–3, ghi–4, jkl–5, mno–6, pqrs–7, tuv–8 wxyz–9, 0–0,就这么简单，渊子把密码中出现的小写字母都变成对应的数字，数字和其他的符号都不做变换
# 声明：
# 密码中没有空格,不能有标点符号，而密码中出现的大写字母则变成小写之后往后移一位，如：X，先变成小写，再往后移一位，不就是y了嘛，简单吧。记住，z往后移是a哦。
# 输入描述:
# 输入包括多个测试数据。输入是一个明文，密码长度不超过100个字符，输入直到文件结尾；
# 输出描述:
# 输出渊子真正的密文
# 示例1：
# 输入：YUANzhi1987
# 输出：zvbo9441987
# while True:
#     ming = input("请输入明文:")
#     for i in ming:
#         if i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHJIJKLMNOPQRSTUVWXYZ0123456789":
#             print("请正确输入明文,没有空格,不能有标点符号!")
#             continue
#     if len(ming) > 100:
#         print("明文长度不能超过100个字符!")
#         continue
#     for j in ming:
#         if j in "abc":
#             ming = ming.replace(j, "2")
#         if j in "def":
#             ming = ming.replace(j, "3")
#         if j in "ghi":
#             ming = ming.replace(j, "4")
#         if j in "jkl":
#             ming = ming.replace(j, "5")
#         if j in "mno":
#             ming = ming.replace(j, "6")
#         if j in "pqrs":
#             ming = ming.replace(j, "7")
#         if j in "tuv":
#             ming = ming.replace(j, "8")
#         if j in "wxyz":
#             ming = ming.replace(j, "9")
#     for x in ming:
#         if x in "ABCDEFGHJIJKLMNOPQRSTUVWXYZ":
#             a = ord(x) + 33
#             if a == 96:
#                 a = 97
#             b = chr(a)
#             ming = ming.replace(x, b)
#     print("密文为:", ming)
#     break
