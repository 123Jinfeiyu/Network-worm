from selenium import webdriver
import time
from selenium.webdriver.common.by import By

'''
新开一个窗口，鼠标聚焦会跟随新窗口变化而变化吗？
'''
driver = webdriver.Chrome()
driver.maximize_window()
# 打开网站
driver.get('https://juejin.cn/')
time.sleep(2)
# 点击元素  SyntaxError: 语法错误
driver.find_element(By.XPATH, '//div[@class="entry-list list"]/li[1]').click()
# 切换到详情页
driver.switch_to.window(driver.window_handles[-1])
time.sleep(1)
# 获取源码内容
print(driver.page_source)  