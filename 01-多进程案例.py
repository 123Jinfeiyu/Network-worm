import requests
from lxml import etree
import re
import multiprocessing
from retrying import retry

'''
多进程版生产者与消费者模式
    1. 生产者类：获取图片的名称，图片链接，图片的后缀名
    2. 消费者类：根据获取的数据下载图片，保存图片
'''


# 生产者类：获取图片的名称，图片链接，图片的后缀名
class Producer(multiprocessing.Process):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    # 初始化方法 创建对象之后默认触发
    def __init__(self, page_queue, img_queue):
        super().__init__()
        self.page_queue = page_queue
        self.img_queue = img_queue  # 存放数据的队列

    # 重写run方法
    def run(self):
        # 存放url的队列取完了，为空的情况，就结束循环
        while True:
            if self.page_queue.empty():
                break
            # 从队列当中取出url
            url = self.page_queue.get()
            # 调用发请求的方法
            page_data = self.fetch_page(url)  # page_data 网页源码
            if page_data:
                # 解析数据
                self.get_img(page_data)
        self.img_queue.put(None)

    # 定义一个重发的方法
    @retry(stop_max_attempt_number=5, wait_fixed=1000)
    def fetch_page(self, url):
        # 发请求，获取数据
        res = requests.get(url, headers=Producer.head)
        # 如果请求的状态码不是200 ，会抛出异常  raise(主动触发异常)
        res.raise_for_status()
        return res.text  # 将源码返回到方法的调用处

    # 解析数据方法
    def get_img(self, page_data):
        # 数据解析
        html = etree.HTML(page_data)
        # 使用xpath解析
        imgs = html.xpath('//img[@class="ui image lazy"]')
        print(len(imgs))
        # 循环遍历，获取每一张的图片
        for img in imgs:
            # 获取图片的标题, 返回的数据类型是list
            img_title = img.xpath('@alt')[0]
            # 获取图片链接
            img_url = img.xpath('@data-original')[0].replace('large', 'bmiddle')
            # 获取图片的后缀名
            hzm = img_url.split('.')[-1]
            # 将数据存放到队列当中(图片1，图片链接1, jpg)， (图片2， 图片链接2)
            self.img_queue.put((img_title, img_url, hzm))
            print(self.img_queue.qsize())


# 消费者类：根据获取的数据下载图片，保存图片
class Consumer(multiprocessing.Process):
    # 初始化方法
    def __init__(self, img_queue):
        super().__init__()
        self.img_queue = img_queue

    # 重写run方法
    def run(self):
        while True:
            data = self.img_queue.get()
            if data is None:
                break
            img_title, img_url, hzm = data
            # 获取图片数据，下载保存
            head1 = {
                'Referer': 'https://www.fabiaoqing.com/'
            }
            # 向图片链接发请求，保存数据
            res1 = requests.get(img_url, headers=head1)
            img_title = re.sub(r'[\\/:?<>|()？*]', '', img_title)
            # 保存图片 os
            with open(f'images/{img_title}.{hzm}', 'wb') as f:
                f.write(res1.content)
                print(f'{img_title}下载完成')


# 设定程序主入口
if __name__ == '__main__':
    # 存放url队列
    page_queue = multiprocessing.Queue()
    # 存放数据的队列
    img_queue = multiprocessing.Queue()
    # 将url添加到队列当中
    for page in range(1, 11):
        url = f'https://www.fabiaoqing.com/biaoqing/lists/page/{page}.html'
        page_queue.put(url)

    # 创建生产者
    for i in range(3):
        p = Producer(page_queue, img_queue)
        # 开启进程
        p.start()  # 调用run方法

    # 创建消费者
    for j in range(3):
        c = Consumer(img_queue)
        # 开启进程
        c.start()


# 20:37上课