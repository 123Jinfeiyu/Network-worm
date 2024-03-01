import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.vip.com/')
time.sleep(1)
# 定位到下拉框元素
el_select = driver.find_element(By.XPATH, '//ul[@id="J-topNavTool"]/li[6]')
el_select.click()

el_select.find_element(By.XPATH, './div/p/span[2]').click()