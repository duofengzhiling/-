import os
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
os.system('start Chrome --remote-debugging-port=9222')

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

#建立对象
driver = webdriver.Chrome(options=options)

#登录
url_login1='https://ids.chd.edu.cn/authserver/login?service=http%3A%2F%2Fcdjk.chd.edu.cn%2FhealthPunch%2Findex%2Flogin'
driver.get(url_login1)
time.sleep(4)
#多次尝试登陆，直至成功
for i in range(7):
# 获取用户与密码输入框并输入
    driver.find_element_by_xpath('//*[@id="username"]').send_keys("你的学号")
    time.sleep(1)
    #driver.find_element_by_xpath('//*[@id="password"]').click()
    #time.sleep(1)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("你的密码",Keys.ENTER)
    #time.sleep(4)
    title = driver.title
    #print("当前页面的title是：", title, "\n")
    if  title=='每日健康打卡':
        print("当前页面的title是：", title,i ,"\n")
        break
    currentPageUrl = driver.current_url
    if("https://cdjk.chd.edu.cn" in currentPageUrl):
        print("当前页面的网页是：", currentPageUrl, "\n")
        break
    pageSource = driver.page_source
    if(u"Internal Server Error" in pageSource ):
        print('ERROR,BACK!')
        driver.back()
        break
time.sleep(2)
#跳转到你的打卡网址，该代码属于手动跳转，事实上如果登陆正常的话，会自己跳转的
url_login2 = '打卡的网址'
driver.get(url_login2)
time.sleep(1)
#点击获取地理位置
dili = driver.find_element_by_xpath('//*[@id="xxdz41"]')
dili.click()
time.sleep(1)
#自己输入的地理位置
driver.find_element_by_xpath('//*[@id="app"]/div[2]/form/div[3]/div[2]/div/span/textarea').send_keys(" 详细的地理位置")
# 提交：
tijn = driver.find_element_by_xpath('//*[@id="app"]/div[2]/form/div[18]/div/div/span/button').click()

print('OK!')
driver.quit()

'''

Pyinstaller -F l.py 打包exe

Pyinstaller -F -w l.py 不带控制台的打包

Pyinstaller -F -i li.ico l.py 打包指定exe图标打包
'''