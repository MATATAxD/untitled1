import requests
url='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
headers={
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'

}
response=requests.get(url,headers=headers)
index=url.rfind('/')
if index != -1:
    name='images'+ url[index:]
#print(response.content)
#imges\xx.png
with open('images/name.png','wb')as file:
    file.write(response.content)
