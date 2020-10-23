import urllib.parse
import urllib.request
#url='https://www.baidu.com/'
userinput=input('输入搜索内容')
dic={
    'wd':userinput
}
result = urllib.parse.urlencode(dic)
#print(result)
url='https://www.baidu.com/s?'+result
#print(url)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36','Cookie':'BIDUPSID=444D5771BF7765563956C9C3C7AA01A0; PSTM=1578206094; BAIDUID=444D5771BF7765563692CE9C3A5CA0FE:FG=1; BD_UPN=12314353; ispeed_lsm=2; MCITY=-%3A; yjs_js_security_passport=67f07812b23f2c99d77d63cf68570e63ee7eba3c_1597835892_js; BD_HOME=1; delPer=0; BD_CK_SAM=1; PSINO=1; BDRCVFR[QxxZVyx49rf]=P81zGNCqivTfjT3nj0snWfkg1DLgv99; BDRCVFR[zv4OXfrzgxs]=lPVrSIjWtIsuAFWuA68mvqV; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; COOKIE_SESSION=3014_0_7_7_8_10_0_0_7_4_5_0_50827_0_734_0_1597890926_0_1597890192%7C9%2390117_607_1597653956%7C9; H_PS_PSSID=; BDSVRTM=0'}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode()
with open('1.html','w',encoding='utf-8') as file:
    file.write(content)