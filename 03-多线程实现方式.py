import threading
from queue import Queue
import requests
from lxml import etree
import re
import time
from retrying import retry  # 作为装饰器使用

num = 1


# 生产者类：获取数据——图片标题以及图片的链接
class Producer(threading.Thread):
    # 添加ua
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    def __init__(self, page_queue, image_queue):
        super().__init__()  # 要求还需要调用一些父类的__init__方法
        self.page_queue = page_queue
        # 专门用来存放数据
        self.image_queue = image_queue

    # 重写run方法
    def run(self):
        # 存放url的队列取完了，为空的情况，才结束
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()  # url队列当中每一页url
            # print(url)
            page_data = self.fetch_page(url)  # 获取源码内容 page_data 相当于网页源码的内容
            if page_data:
                self.get_img(page_data)
        self.image_queue.put(None)

    # 设置重复发请求
    @retry(stop_max_attempt_number=4, wait_fixed=1000)  # 设置最大的请求数量  wait_fixed=1000,每次间隔1秒
    def fetch_page(self, url):
        # 发请求
        res = requests.get(url, headers=Producer.head)
        # 如果请求的状态码不是200 会抛出异常
        res.raise_for_status()
        return res.text

    # 获取图片链接以及标题
    def get_img(self, html):
        # 数据解析
        html = etree.HTML(html)
        # 使用xpath解析，找img标签。 只要通过xpath获取的标签，返回的数据类型列表
        imgs = html.xpath('//img[@class="ui image lazy"]')
        print(len(imgs))
        # for 循环遍历
        for img in imgs:
            # 获取图片标题
            img_title = img.xpath('@alt')[0]
            # 图片链接
            img_url = img.xpath('@data-original')[0].replace('large', 'bmiddle')
            # print(img_title, img_url)
            # 获取图片的后缀名
            hzm = img_url.split('.')[-1]
            # (标题，链接，hzm)  (标题 链接 hzm)
            self.image_queue.put((img_title, img_url, hzm))
            print(self.image_queue.qsize())
        self.image_queue.put((None)) #False也可以

# 消费者类：保存图片
class Consumer(threading.Thread):
    def __init__(self, image_queue):
        super().__init__()
        self.image_queue = image_queue

    # 重写run方法
    def run(self):
        while True:
            global num
            data = self.image_queue.get()
            if data is None:
                #判下False
                break
            img_title, img_url, hzm = data
            # 获取图片数据，下载图片，保存图片数据
            head1 = {
                'Referer': 'https://www.fabiaoqing.com/'
            }
            # 再次向图片的链接发请求，获取图片的二进制数据
            res1 = requests.get(img_url, headers=head1,verify=False)
            img_title = re.sub(r'[\\/:*?"<>|]', '', img_title)
            # 保存图片
            with open(f'images/{img_title}{num}.{hzm}', 'wb') as f:
                f.write(res1.content)  # res1.content 获取响应内容的二进制数据
                num = num + 1
                print(f'{img_title}下载成功了')


# 程序主入口
if __name__ == '__main__':
    # 存放url的队列
    page_queue = Queue()
    # 存放数据的队列
    image_queue = Queue()
    for page in range(1, 11):
        url = f'https://www.fabiaoqing.com/biaoqing/lists/page/{page}.html'
        page_queue.put(url)

    # 创建生产者线程对象
    for i in range(3):
        t = Producer(page_queue, image_queue)  # 将存放url的队列传递给生产者
        t.start()

    # 创建消费者线程对象
    for j in range(3):
        t = Consumer(image_queue)
        t.start()
