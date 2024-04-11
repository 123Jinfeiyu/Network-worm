import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # 添加这一行导入语句
# 初始化chatgpt陪HR聊天
from openai import OpenAI

# 创建一个Edge浏览器实例
driver = webdriver.Edge()
#防检测
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })
#设置爬取时候的窗口最大化
driver.maximize_window()
# 打开一个网页
driver.get("https://wow.liepin.com/")
#点击切到密码登录
pwd_login= driver.find_element(By.XPATH,"//*[@id='home-banner-login-container']/div/div/div/div/div[2]/div/div[2]")
pwd_login.click()
time.sleep(2)
login_input = driver.find_element(By.XPATH,"//*[@id='login']")
login_input.send_keys("18705434934")
pwd_input=driver.find_element(By.XPATH,"//*[@id='pwd']")
pwd_input.send_keys("521114@wjp")
checkbox=driver.find_element(By.XPATH,"//*[@id='home-banner-login-container']/div/div/div/div/div[4]/div/label/span[1]/input")
checkbox.click()
click_button=driver.find_element(By.XPATH,"//*[@id='home-banner-login-container']/div/div/div/div/div[3]/div/form/button/span")
click_button.click()
time.sleep(6)
set_search=driver.find_element(By.XPATH,"//*[@id='main-container']/div/div[3]/div[1]/div/div[1]/div/div/div/input")
keyword="数据分析"
set_search.send_keys(keyword)
sumit_button=driver.find_element(By.XPATH,"//*[@id='main-container']/div/div[3]/div[1]/div/div[1]/div[1]/div/div/span")
sumit_button.click()
time.sleep(2)
# 切换到第二个窗口
driver.switch_to.window(driver.window_handles[1])
# 滑动到页面底部
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 等待网页加载所有元素
driver.implicitly_wait(10)  # 等待10秒
for i in range(1,40):
    # 使用鼠标行为链进行悬浮操作
    test_element = driver.find_element(By.XPATH,f"//*[@id='lp-search-job-box']/div[3]/section[1]/div[2]/div[{i}]/div/div[2]/div/div[2]")
    actions = ActionChains(driver)
    actions.move_to_element(test_element)
    actions.click()
    actions.perform()
    element2 = driver.find_element(By.XPATH, "//*[@id='im-chatwin']/div/div[2]/div[3]/div[1]/div/textarea")
    element2.send_keys("你可以调用gpt回复你需要群回复的内容")
    element2.send_keys(Keys.RETURN)
    driver.execute_script("window.history.go(-1)")
    #投递简历
    # element3=driver.find_element(By.XPATH, "//*[@id='im-chatwin']/div/div[2]/div[1]/div/div[2]/div[1]/span/svg")
    # element3.click()
    # time.sleep(2)
    # element4 = driver.find_element(By.XPATH, "//*button[@class='ant-btn ant-btn-primary']")
    # element4.click()
    #留三秒的点击退出聊天时间
    time.sleep(4)
input()
    # 如果下一页按钮不可点击，则退出循环
# 关闭浏览器实例
driver.quit()