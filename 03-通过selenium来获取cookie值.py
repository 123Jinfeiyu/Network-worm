import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# 通过selenium获取登录之后的cookie
driver.get('https://i.qq.com/')
# 切换iframe
driver.switch_to.frame('login_frame')
# 定位头像图片
driver.find_element(By.ID, 'img_out_3561774713').click()
# time.sleep(3)
# 登录之后，获取cookie值，就是登录之后的cookie值
cookies = driver.get_cookies()
li = []
for cookie in cookies:
    # print(cookie)
    name = cookie.get('name')
    value = cookie.get('value')
    li.append(name+'='+value)
cookies = '; '.join(li)
print(cookies)
url = 'https://user.qzone.qq.com/3561774713'
# 添加反爬参数
head = {
    'Cookie': cookies,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 发请求，获取响应内容
res = requests.get(url, headers=head)

# 打印响应内容
print(res.text)   # 