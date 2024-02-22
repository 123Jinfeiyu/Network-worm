import time

import requests
from lxml import etree
import re


# 定义下载图片的函数
def download_img():
    for page in range(1, 11):
        url = f'https://www.fabiaoqing.com/biaoqing/lists/page/{page}.html'
        # 添加ua
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        }
        # 发请求
        res = requests.get(url, headers=head)
        # 数据解析
        html = etree.HTML(res.text)
        # 使用xpath解析，找img标签。 只要通过xpath获取的标签，返回的数据类型列表
        imgs = html.xpath('//img[@class="ui image lazy"]')
        # print(len(imgs))
        # for 循环遍历
        for img in imgs:
            # 获取图片标题
            img_title = img.xpath('@alt')[0]
            # 图片链接
            img_url = img.xpath('@data-original')[0].replace('large', 'bmiddle')
            print(img_title, img_url)
            # 获取图片的后缀名
            hzm = img_url.split('.')[-1]
            head1 = {
                'Referer': 'https://www.fabiaoqing.com/'
            }
            # 再次向图片的链接发请求，获取图片的二进制数据
            res1 = requests.get(img_url, headers=head1)
            img_title = re.sub(r'[\\/:*?"<>|]', '', img_title)
            # 保存图片
            with open(f'images/{img_title}.{hzm}', 'wb') as f:
                f.write(res1.content)  # res1.content 获取响应内容的二进制数据


start = time.time()
download_img()
end = time.time()
print(f'所花费的时间是{end - start}')  # 所花费的时间是295.2128076553345
