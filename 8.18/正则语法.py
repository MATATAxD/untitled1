import re
# userInput=input('输入一个手机号')
# partern=r'^1[3,5,7,1,8]\d{9}$'
# result=re.search(partern,userInput)
# if result ==None:
#     print('不是手机号')
# else:
#     print('是一个正确的手机号')
#

# userInput=input('输入一个座机号')
# partern=r'^(0\d{2,3}-)?\d{7}$'
# result=re.search(partern,userInput)
# if result == None:
#     print('不是座机号')
# else:
#     print('是一个正确的座机号')

userInput=input('输入一个身份证号')
partern=r'^([1-9]\d{5}[12]\d{3}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])\d{3}[0-9xX])$'
result=re.search(partern,userInput)
if result == None:
    print('不是身份证号码')
else:
    print('是一个正确的身份证号')

