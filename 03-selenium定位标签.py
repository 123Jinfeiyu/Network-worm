import time

from selenium import webdriver
# 用于定位标签的类
from selenium.webdriver.common.by import By


# 1. 加载驱动
driver = webdriver.Chrome()
# 最大化页面
driver.maximize_window()
# 2. 加载网页
driver.get('https://www.baidu.com/')
time.sleep(2)
# 3. 定位元素
# 3.1 通过id定位  no such element: 没有定位到这个元素
# el = driver.find_element(By.ID, 'kw')
# # 输入内容
# el.send_keys('python')
# print(el)
# 截图
# driver.save_screenshot('百度.png')

'''
2. 通过class属性值定位
直接通过class属性值定位  属性值之间有空格 选其中一个属性值就可以了
'''
# el = driver.find_element(By.CLASS_NAME, 's_ipt')
# print(el)

'''
3. 通过name属性值定位
'''
# el = driver.find_element(By.NAME, 'wd')
# print(el)

'''
4. 通过标签名定位(不建议)
通过find_elements定位数据：返回的数据类型
'''
# el = driver.find_elements(By.TAG_NAME, 'input')
# print(el)
'''
5. 通过xpath定位  bg s_ipt_wr new-pmd quickdelete-wrap//

'''
el1= driver.find_element(By.XPATH, '//*[@id="kw"]')
el = driver.find_element(By.XPATH, '//span[@class="bg s_ipt_wr new-pmd quickdelete-wrap"]/input')
print(el)


