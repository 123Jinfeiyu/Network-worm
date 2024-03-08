import time
# 显示等待
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import re
from selenium import webdriver
from selenium.webdriver.common.by import By


class JueJin:

    # 1. 初始化方法
    def __init__(self):
        # 初始化驱动，加载对应的网站数据
        self.driver = webdriver.Chrome()
        # 最大化窗口
        self.driver.maximize_window()
        # 加载网站
        self.driver.get('https://juejin.cn/')

    # 2. 解析文章
    def parse_html(self):
        # 用显示等待，判断元素都加载出来，再往下操作
        lis = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="entry-list list"]/li'))
        )
        # print(len(lis))  # 输出列表中元素的数量
        # 循环遍历每一个元素，做点击
        for li in lis:
            try:
                li.click()  # 做点击  打开了详情页面
                # 切换到新打开的窗口
                self.driver.switch_to.window(self.driver.window_handles[-1])
                # 获取文章
                article_title = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'article-title'))
                )
                # 获取文章标签
                title = article_title.text
                # 对标签进行处理，去除特殊字符
                title = re.sub(r'[,<>().*/\\? ？|]', '', title)
                # 获取文章内容  driver.find_elements: 返回的数据类型是列表
                contents = self.driver.find_elements(By.XPATH, '//div[@id="article-root"]/p')
                # print(title, contents)
                result = '\n'.join([i.text for i in contents])
                # 保存文章
                self.save_data(title, result)
            except Exception as e:
                print('没有文章内容')
            finally:
                # [第一个窗口]  1>1
                if len(self.driver.window_handles) > 1:
                    # 关闭当前的窗口，返回到第一个窗口 close quit
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])

    # 3. 滑动方法
    def slide(self, count):
        # 根据count值，设置滑动次数
        for i in range(count):
            # 滚动的代码  document.body.scrollHeight：页面最底部
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)

    # 4. 保存
    def save_data(self, title, result):
        with open(f'掘金/{title}.txt', 'w', encoding='utf-8') as f:
            f.write(result)

    # 5. 主方法
    def main(self):
        # 1. 先滑动元素
        self.slide(5)
        # 2. 解析文章数据
        self.parse_html()


# 创建一个对象，对象去调用类里面的方法
d = JueJin()  # 创建对象之后就会主动触发init方法
d.main()  #
