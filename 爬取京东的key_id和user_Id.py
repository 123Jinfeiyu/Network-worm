import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# msedgedriver.exe下载后放到浏览器的目录下
driver = webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })
driver.get("http://www.jd.com/")   # 你要进入的浏览器
driver.maximize_window()
web_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/ul[3]/li[1]/a[1]/span[2]").click()
login_index = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[1]/div[2]").click()
# #填你的手机号码，然后页面的验证码手动拖下
button_element1 = driver.find_element(By.ID, "mobile-number").send_keys('17633699252')
button_element2 = driver.find_element(By.ID, "send-sms-code-btn").click()
time.sleep(30)
# ('请输入他们给你的商品id')
user_input='11145'
button_element222 = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div/div[2]/input").send_keys(user_input)
button_element3 = driver.find_element(By.CLASS_NAME, "button").click()
#用户点击有优惠卷的商品时间
time.sleep(10)
input()
# driver.quit()