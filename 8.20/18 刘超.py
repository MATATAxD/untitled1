from lxml import etree
import csv
import requests
import urllib.request
import urllib.parse
url='https://www.zhisheji.com/new_index_tj'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'

}
dic={

    'page':1
}
response = requests.post(url,headers = headers,data=dic)
with open('致设计.html','w',encoding='utf-8') as file:
    file.write(response.text)



