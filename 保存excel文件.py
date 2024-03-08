import time
import requests
from lxml import etree
from openpyxl import Workbook
# pip install openpyxl：第三方库

# 创建工作簿对象
wb = Workbook()
# 删除默认工作表
wb.remove(wb.active)

# 遍历豆瓣电影 Top250 的每一页
for page in range(1, 11):
    lst = []  # 存储一页的数据
    url = f'https://movie.douban.com/top250?start={(page-1)*25}&filter='
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    # 发送请求获取页面内容
    res = requests.get(url, headers=head)
    # 使用 lxml 解析页面内容
    result = etree.HTML(res.text)
    # 提取每个电影信息的 div 元素
    divs = result.xpath('//div[@class="info"]')
    # 遍历每个 div 元素，提取电影信息
    for div in divs:
        dic = {}
        # 提取电影标题
        title = div.xpath('./div[@class="hd"]/a/span/text()')
        dic['titles'] = ''.join(title)
        # 提取电影类型
        p = div.xpath('./div[@class="bd"]/p/text()')
        dic['types'] = ''.join(p).strip().split('/')[-1]
        # 提取电影评分
        dic['star'] = div.xpath('./div[@class="bd"]/div[@class="star"]/span[2]/text()')[0]
        # 提取电影引言
        quote = div.xpath('./div[@class="bd"]/p[@class="quote"]/span/text()')
        dic['quote'] = quote[0] if quote else ''
        # 将提取的电影信息加入列表
        lst.append(dic)

    # 创建工作表并命名
    ws = wb.create_sheet(f'第{page}页')
    sheet = wb[f'第{page}页']  # 获取对应的工作表对象
    # 写入表头信息
    headers = ['titles', 'types', 'star', 'quote']
    sheet.append(headers)
    # 遍历列表，逐行写入电影信息
    for data in lst:
        sheet.append([data['titles'], data['types'], data['star'], data['quote']])

# 保存工作簿到文件
wb.save('豆瓣.xlsx')
# 关闭工作簿
wb.close()
