from selenium import webdriver

# 1. 加载驱动  Chrome(): 谷歌浏览器
'''
Chrome:c是大写

'''
driver = webdriver.Chrome()
# 页面的最大化
driver.maximize_window()
# 加载网页内容
driver.get('https://www.baidu.com/s?ie=UTF-8&wd=pip%20%E6%B8%85%E5%8D%8E%E6%BA%90')

driver.close()  # 关闭当前的窗口，还可以对未关闭的页面继续做操作

driver.quit()  # 退出驱动
# close() : 关闭当前的页面
# quit()  ：退出驱动
