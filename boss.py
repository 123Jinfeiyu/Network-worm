import json
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import finding_jobs
def chat_gpt_content():
    # 初始化chatgpt陪HR聊天
    from openai import OpenAI
    # 设置 API key 和 API base URL
    # api_key = "sk-0f120pZgs2uf84vPE0A81a35D75f43FbA34aF89d27Fe8dA5"
    # base_url = "https://api.132006.xyz"
    #
    # client = OpenAI(
    #     api_key=api_key,
    #     base_url=base_url
    # )
    # 调用chatGPT的接口
    # resume="我的简历"
    # description="我的工作描述"
    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": f"你将扮演一位求职者的角色，根据{resume}以及应聘工作的{description}，来直接给HR写一个礼貌专业的求职新消息，要求能够用专业的语言结合简历中的经历和技能，并结合应聘工作的描述，来阐述自己的优势，尽最大可能打动招聘者。并且请您始终使用中文来进行消息的编写,开头是招聘负责人，结尾是真诚的，付尧全。这是一封完整的求职信，不要包含求职信内容以外的东西，例如“根据您上传的求职要求和个人简历，我来帮您起草一封求职邮件：”这一类的内容，以便于我直接自动化复制粘贴发送",
    #         }
    #     ],
    #     model="gpt-3.5-turbo",
    # )
    # message=chat_completion.choices[0].message.content
driver=webdriver.Edge()
def log_in(url):
    global driver
    # 设置爬取时候的窗口最大化
    driver.maximize_window()
    # 打开一个网页
    driver.get(url)
    # 点击按钮
    login_button = driver.find_element(By.XPATH, "//*[@id='header']/div[1]/div[3]/div/a")
    login_button.click()

    # 等待微信登录按钮出现
    xpath_locator_wechat_login = "//*[@id='wrap']/div/div[2]/div[2]/div[2]/div[1]/div[4]/a"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_locator_wechat_login))
    )

    wechat_button = driver.find_element(By.XPATH, "//*[@id='wrap']/div/div[2]/div[2]/div[2]/div[1]/div[4]/a")
    wechat_button.click()

    xpath_locator_wechat_logo = "//*[@id='wrap']/div/div[2]/div[2]/div[1]/div[2]/div[1]/img"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_locator_wechat_logo))
    )

    xpath_locator_login_success = "//*[@id='header']/div[1]/div[3]/ul/li[2]/a"
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, xpath_locator_login_success))
    )

def get_job_description():

    global driver

    # 使用给定的 XPath 定位职位描述元素
    xpath_locator_job_description = "//*[@id='wrap']/div[2]/div[2]/div/div/div[2]/div/div[2]/p"

    # 确保元素已加载并且可以获取文本
    job_description_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_locator_job_description))
    )

    # 获取职位描述文本
    job_description = job_description_element.text
    print(job_description)  # 打印出职位描述，或者你可以在这里做其他处理

    # 返回职位描述文本，如果函数需要
    return job_description
def select_dropdown_option(driver, label):
    # 尝试在具有特定类的元素中找到文本
    trigger_elements = driver.find_elements(By.XPATH, "//*[@class='recommend-job-btn has-tooltip']")

    # 标记是否找到元素
    found = False

    for element in trigger_elements:
        if label in element.text:
            print(label)
            # 确保元素可见并且可点击
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element))
            element.click()  # 点击找到的元素
            found = True
            break

def click_instant_communication(driver):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='wrap']/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/a[2]")))
    driver.execute_script("arguments[0].click();", element)
    # element1 = driver.find_element(By.XPATH, "")
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element1))
def get_job_description_by_index(index):
    try:
        job_selector = f"//*[@id='wrap']/div[2]/div[2]/div/div/div[1]/ul/li[{index}]"
        job_element = driver.find_element(By.XPATH, job_selector)
        job_element.click()

        description_selector = "//*[@id='wrap']/div[2]/div[2]/div/div/div[2]/div/div[2]/p"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, description_selector))
        )
        job_description_element = driver.find_element(By.XPATH, description_selector)
        return job_description_element.text

    except NoSuchElementException:
        print(f"No job found at index {index}.")
        return None
if __name__ == '__main__':
    url = "https://www.zhipin.com/web/geek/job-recommend?ka=header-job-recommend"
    log_in(url)
    get_job_description()
    label="教师（南阳）"
    select_dropdown_option(driver, label)
    for i in range(1,10):
        description=get_job_description_by_index(i)
        # input()
        # click_instant_communication(driver)
        # print(description)
        print(driver.page_source)
        # 切换到第二个窗口
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='op-btn op-btn-chat']")))
        element.click()
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "default-btn.sure-btn")))
        element.click()
        time.sleep(4)
        element = driver.find_element(By.XPATH, '//*[@id="chat-input"]')
        ask_content="你好有时间谈谈吗?"
        element.send_keys(ask_content)
        element.send_keys(Keys.RETURN)
        driver.execute_script("window.history.go(-1)")

        time.sleep(3)

        # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        #     (By.XPATH, "//*[@id='wrap']/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/a[2]")))
        # driver.execute_script("arguments[0].click();", element)
