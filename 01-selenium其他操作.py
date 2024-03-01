import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# 键盘操作类
from selenium.webdriver.common.keys import Keys

# 1. 加载驱动


driver = webdriver.Chrome()

# 2. 最大化
driver.maximize_window()
# 设置浏览器大小
# driver.set_window_size(700, 700)
# 设置浏览器的位置
# driver.set_window_position(400, 600)
# 3.
driver.get('https://www.baidu.com')

el = driver.find_element(By.ID, 'kw')
# 输入框输入内容
el.send_keys('python')

el.clear()  # 清空输入框里面的内容
# 回车\点击百度一下
# el.send_keys(Keys.ENTER)

# click(): 点击元素
# driver.find_element(By.ID, 'su').click()
#
# time.sleep(2)
# # 页面刷新
# driver.refresh()
# time.sleep(2)
#
# # 回到上一页
# driver.back()
#
# time.sleep(2)
#
# # 回到下一页
# driver.forward()
#

