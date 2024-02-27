import time

import requests
from bs4 import BeautifulSoup
import os

'''
涉及两个页面
    目标url：http://www.b5200.org/199_199539/
        章节：目录名称，具体内容页面的链接

    具体内容页面：获取内容
'''

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}


# 1. 得到网页源码
def get_html(url):
    # 发请求，获取响应内容
    res = requests.get(url, headers=head)
    # print(res.text)
    # 将源码内容返回到函数的调用处
    return res.text


# 2. 解析数据
def parse_html(html):
    # 实例化对象
    soup = BeautifulSoup(html, 'lxml')
    # 解析：获取目录以及内容链接
    div = soup.find('div', id='list')
    # 获取所有的dd标签 去除前面9个dd标签
    dds = div.find_all('dd')[9:]  # list
    # print(len(dds))
    for d in dds:
        time.sleep(0.5)
        a = d.find('a')  # a标签定位到
        # 链接以及标题
        title = a.string
        '''
        http://www.b5200.org/199_199539/191030589.html
                            /199_199539/191030589.html
        字符串的相加就是拼接
        '''
        href = 'http://www.b5200.org' + a.get('href')
        # print(title, href)
        # 获取具体的章节内容
        # 向小说链接发请求，获取对应的小说内容
        res_content = get_html(href)
        # 解析小说内容
        soup1 = BeautifulSoup(res_content, 'lxml')
        data = soup1.find('div', id="content")
        result = '\n'.join(list(data.stripped_strings))
        # print(result)
        save_data(title, result)  # 获取一章内容，就保存一次
        # break


# 3. 保存数据
def save_data(title, result):
    path = '希腊神话：灵性支配者'
    if not os.path.exists(path):  # 判断文件夹是否存在，不存在，就创建
        os.mkdir(path)
    with open(f'{path}/{title}.txt', 'w', encoding='utf-8') as f:
        f.write(result)
    print(f'{title}保存成功！')


# 主函数
def main():
    url = 'http://www.b5200.org/199_199539/'
    # 调用get_html函数，得到网页源码
    html = get_html(url)  # html代表源码
    # 数据解析
    parse_html(html)


main()

'''
判断章节名称 == '卷末感言’
创建一个新的文件夹（卷二)
'''
