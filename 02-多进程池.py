# 导入进程池模块
from concurrent.futures import ProcessPoolExecutor
import requests
from lxml import etree
import re
from retrying import retry


# 获取图片的数据（图片的标题，链接，后缀名）
@retry(stop_max_attempt_number=5, wait_fixed=1000)
def download_img(url):
    # 发请求，获取响应的内容
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }
    res = requests.get(url, headers=head)
    html = etree.HTML(res.text)
    imgs = html.xpath('//img[@class="ui image lazy"]')
    print(len(imgs))
    '''状态码不是200情况，考虑重发'''
    if len(imgs) == 0:
        raise Exception('页面图片数量为0')
    # 循环遍历，获取每一组图片的数据
    img_data = []
    for img in imgs:
        # 获取图片的标题, 返回的数据类型是list
        img_title = img.xpath('@alt')[0]
        # 获取图片链接
        img_url = img.xpath('@data-original')[0].replace('large', 'bmiddle')
        # 获取图片的后缀名
        hzm = img_url.split('.')[-1]
        img_data.append((img_title, img_url, hzm))
    return img_data


# 保存图片
def save_img(data):
    img_title, img_url, hzm = data
    # 获取图片数据，下载保存
    head1 = {
        'Referer': 'https://www.fabiaoqing.com/'
    }
    # 向图片链接发请求，保存数据
    res1 = requests.get(img_url, headers=head1)
    img_title = re.sub(r'[\\/:?<>|()？*]', '', img_title)
    # 保存图片 os
    with open(f'images1/{img_title}.{hzm}', 'wb') as f:
        f.write(res1.content)
        print(f'{img_title}下载完成')


if __name__ == '__main__':
    # 列表推导式
    # 定义要爬取的页面列表
    pages = [f'https://www.fabiaoqing.com/biaoqing/lists/page/{page}.html' for page in range(1, 5)]
    # 创建进程池  max_workers=
    with ProcessPoolExecutor() as pool:
        # 使用进程池执行下载图片任务（download_img)，所有的任务一次性提交
        # 任务交给谁做处理，任务
        img_data_list = pool.map(download_img, pages)
        # print(img_data_list)
        for img_list in img_data_list:
            # print(i)  # i代表是传递过来的列表
            for img_data in img_list:
                # print(img_data)  # img_data 是每一组的图片数据，提交给消费者
                pool.submit(save_img, img_data)
