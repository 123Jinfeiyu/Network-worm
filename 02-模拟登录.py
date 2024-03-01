import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 加载驱动


driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
# 加载网页
driver.get('https://www.douban.com/?r=9&c=3_6')
time.sleep(2)

# 切换iframe
login_frame = driver.find_element(By.XPATH, '//div[@class="login"]/iframe')
# 切换
driver.switch_to.frame(login_frame)
# 切换登录方式：定位密码标签
'''
速度太快？
'''
driver.find_element(By.CLASS_NAME, 'account-tab-account').click()

# 定位账号与密码
driver.find_element(By.ID, 'username').send_keys('1232323232')
# 密码
driver.find_element(By.ID, 'password').send_keys('erereree')

# 定位登录按钮
driver.find_element(By.CLASS_NAME, 'btn-account ').click()