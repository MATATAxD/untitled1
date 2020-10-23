import requests

url='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E4%BD%A9%E5%A5%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E4%BD%A9%E5%A5%87&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=1e&1597988955783='
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
response = requests.get(url,headers = headers)
#服务器返回的是josn数据使用josn.()
content=response.json()
# print(type(content))
#print(content['data'],len(content['data']))
count=0
allData=content['data'][:len(content['data'])-1]
for img in allData:
    count+=1
    # print(content,'+++++')
    # print(img['hoverURL'])
    index='hoverURL'.rfind('/')
    if index != -1:
       name='images'+ url[index:]
    #print(name)
#print(response.content)
#imges\xx.png
with open('name','wb')as file:
    file.write(response.content)



