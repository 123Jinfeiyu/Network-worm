from selenium import webdriver

# 1.创建一个配置对象
options = webdriver.ChromeOptions()
# 2.使用代理  前提是ip可用
options.add_argument('--proxy-server=http://192.168.129.130')
# 3.创建driver对象
driver = webdriver.Chrome(options=options)
# 4.设置起始的url地址
start_url = 'https://www.baidu.com'
# 访问
driver.get(url=start_url)