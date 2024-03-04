from selenium import  webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# 2. 设置无界面
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

driver.get('https://movie.douban.com/top250?start=0&filter=')
img_tag = driver.find_element(By.XPATH, '//div[@class="pic"]/a/img')
print(img_tag.get_attribute('src'))
'''
text: 获取文本内容
'''
div_tag = driver.find_element(By.XPATH, '//div[@class="hd"]/a')
print(div_tag.text)
