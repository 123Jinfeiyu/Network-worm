from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# 显示等待
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

'''
网站加载
代码执行：快
强制等待：time.sleep(2): 等待(浪费时间)

隐式等待：全局元素
显示等待：单个元素
'''
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# time.sleep(3)  强制等待
'''
隐式等待: 针对的是所有元素，声明一次就行
我想要的元素加载了，但是网页上面有部分元素还没加载完成，还是会继续等
'''
# driver.implicitly_wait(5)  # 隐式等待
'''
显示等待：针对的是单个元素
until方法：具体的条件内容
EC: 期望条件
'''
el = WebDriverWait(driver, 10).until(
    # 元素加载条件 id值为kw的这个元素
    EC.presence_of_element_located((By.ID, 'kw'))
)
# el = driver.find_element(By.ID, 'kw1')
print(el)