import urllib.parse
import urllib.request
import requests

url='https://www.zhisheji.com/new_index_tj'
headers={
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.'


}
dic={
    'page':1
}
result=urllib.parse.urlencode(dic).encode()
print(result)
request = urllib.request.Request(url, headers=headers,data=result)
response = urllib.request.urlopen(request)
content = response.read().decode()
with open('2.html','w',encoding='utf-8') as file:
    file.write(content)

