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
driver.get('https://passport.vip.com/login?src=https%3A%2F%2Fwww.vip.com%2F')
# 切换登录方式 列表.click()
driver.find_element(By.XPATH, '//div[@class="c-tab-nav "]/div[2]').click()

# 输入用户名
driver.find_element(By.ID, 'J_login_name').send_keys('123213123123')
# 输入密码
driver.find_element(By.ID, 'J_login_pwd').send_keys('123213123123')

# 勾选复选框
'''
如果需要点击的元素被覆盖或者是隐藏，通过执行js代码进行点击
'''
label = driver.find_element(By.ID, 'J_login_agree')
# 执行js代码
driver.execute_script('arguments[0].click();', label)

# 点击登录按钮
driver.find_element(By.ID, 'J_login_submit').click()

time.sleep(1)
'''
移动鼠标到对应的元素上面
'''
img = driver.find_element(By.CLASS_NAME, 'vipsc_qimg')
# 创建对象
action = ActionChains(driver)
# 移动
action.move_to_element(img)
# 提交
action.perform()

