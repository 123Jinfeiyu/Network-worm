from selenium import webdriver
from selenium.webdriver.chrome.options import Options

phone = {
    "deviceName":"iPhone X"
}

chrome_options = Options()

chrome_options.add_experimental_option("mobileEmulation", phone)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.kugou.com/')