from selenium import webdriver
# Select类专门用于管理下拉框
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
'''
https://tieba.baidu.com/f/search/adv
'''

# 加载驱动
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://tieba.baidu.com/f/search/adv')

# 定位到下拉框元素
select_el = driver.find_element(By.NAME, 'rn')

# 创建一个下拉框对象
s_el = Select(select_el)
# index：根据选项的索引来进行定位  索引从0开始
# s_el.select_by_index(2)
# value：值  指的是value属性值 是字符串类型
# s_el.select_by_value('30')
# text：标签里面的文本内容
s_el.select_by_visible_text('每页显示20条')