import time

from selenium import webdriver
import json

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化窗口
# 1. 加载登录网站
driver.get('https://login.taobao.com/member/login.jhtml')
# 扫码登录
# input("扫码登录，请回车")
# 得到登录之后的cookie
# cookies = driver.get_cookies()
# print(cookies)
# jsonCookies = json.dumps(cookies)  # 字符串类型的数据
# with open('taobao_cookies.json', 'w') as f:
#     f.write(jsonCookies)  # 必须是字符串

# 一旦加载某个网站，即使没有登录，也产生一个cookie
driver.delete_all_cookies()  # 删除页面上所有的cookie
with open('taobao_cookies.json', 'r') as f:
    cookies = json.loads(f.read())  # 将json字符串转为python对象

for cookie in cookies:
    # 用于向浏览器添加cookie信息
    driver.add_cookie({
        'domain': '.taobao.com',  # 表示cookie的作用域为.taobao.com
        'name': cookie['name'],  # 要添加的cookie名称
        'value': cookie['value'],  # 要添加的cookie值
        'path': '/',  # 根目录，代表cookie对整个网站有效
        'expires': None,  # 在浏览器关闭后删除，未关闭期间有效
    })
time.sleep(1)
driver.get('https://cart.taobao.com/cart.htm')
