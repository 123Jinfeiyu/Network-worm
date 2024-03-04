from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
# 打开网站
driver.get("https://juejin.cn/post/7278299358910201897")
time.sleep(1)
driver.window_handles

# 打开网站
driver.execute_script('window.open("https://www.baidu.com")')
time.sleep(1)
driver.window_handles

# 打开第二个网站
driver.execute_script('window.open("https://www.douban.com")')
time.sleep(1)
driver.window_handles

# 打开第三个网站
driver.execute_script('window.open("https://juejin.cn/")')
driver.window_handles
# 打印一下 当前操作的url
print(driver.current_url)

# 切换窗口 定位元素 数据类型：列表
print(driver.window_handles)

driver.switch_to.window(driver.window_handles[1])

# 打印一下 当前操作的url
print(driver.current_url)