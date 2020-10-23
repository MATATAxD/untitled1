from selenium import webdriver
import time
#driver 浏览器
driver=webdriver.Chrome('chromedriver.exe')
url='https://www.baidu.com/'
driver.get(url)
#print(driver.page_source)
a=driver.find_element_by_xpath('//*[@id="kw"]').send_keys('aaa')
driver.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(2)
with open('百度.html','w',encoding='utf-8')as file:
    file.write(driver.page_source)
time.sleep(2)
driver.quit()

