from selenium import  webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get('https://music.163.com/#/discover/toplist')
# time.sleep(2)
# driver.switch_to.frame("g_iframe")
# print(driver.page_source)  # 返回结构源码
#
# html = etree.HTML(driver.page_source)

'''
find(): 在源码当中查找某个字符是否存在
'''
# driver.get('https://tieba.baidu.com/f?kw=%E7%BE%8E%E9%A3%9F&ie=utf-8&pn=385550')
# time.sleep(2)
# # html = driver.page_source  # 获取源码
# # print(html)
# # # 查找对应的字符  如果要查找的字符不存在的，返回-1
# # print(html.find('下一页'))  # 426208
# while True:
#     if driver.page_source.find("下一页&gt;") != -1:
#         driver.find_element(By.CLASS_NAME, 'next').click()
#         time.sleep(1)
#     else:
#         print('已经是最后一页了')
#         break


'''
获取属性值: get_attribute('src')
'''
driver.get('https://movie.douban.com/top250?start=0&filter=')
img_tag = driver.find_element(By.XPATH, '//div[@class="pic"]/a/img')
print(img_tag.get_attribute('src'))
'''
text: 获取文本内容
'''
div_tag = driver.find_element(By.XPATH, '//div[@class="hd"]/a')
print(div_tag.text)
