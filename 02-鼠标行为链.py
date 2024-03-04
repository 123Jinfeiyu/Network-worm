import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# 鼠标行为链
from selenium.webdriver import ActionChains

'''
https://passport.vip.com/login?src=https%3A%2F%2Fwww.vip.com%2F
'''
# 1. 加载驱动
driver = webdriver.Chrome()
# 2. 最大化
driver.maximize_window()
# 加载网站
driver.get('https://blog.csdn.net/weixin_36273267/article/details/106356546')

# 需要定位到双击的元素
span = driver.find_element(By.CLASS_NAME, 'read-count')
# 创建动作链对象
actions = ActionChains(driver)

# 双击
actions.double_click(span).perform()