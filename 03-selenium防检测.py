from selenium import webdriver
from selenium.webdriver import ChromeOptions

option = ChromeOptions()  # 实例化一个ChromeOptions对象
option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以键值对的形式加入参数

# 加载的谷歌驱动
bro = webdriver.Chrome(options=option)  # 在调用浏览器驱动时传入option参数就能实现
bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })
