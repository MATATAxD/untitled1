import requests,csv,pymysql,json,time
from lxml import etree
url = 'https://m.ke.com/liverpool/api/ershoufang/getList?cityId=110000&condition=%252Fpg2&curPage=2'
headers={
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1'


}
response=requests.get(url,headers=headers)
newsList = response.json()['data']
print(newsList)
title=newsList['title']
print(title)






