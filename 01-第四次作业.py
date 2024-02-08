import requests
from lxml import etree
import csv

url = 'http://www.piaofang.biz/'

res = requests.get(url)
# 乱码，设置编码格式
res.encoding = 'gb2312'

# 获取响应数据
html = res.text
# print(html)
# 数据解析
tree = etree.HTML(html)
# 定位标签位置：以元素为准，以响应的内容为准
trs = tree.xpath('//div[@class="zhuti"]/table/tr')
# print(len(trs))
# 通过循环遍历
lst = []
for tr in trs[1:]:
    dic = {}
    # 如果是空行，长度为0
    if len(tr) != 0:
        name = tr.xpath('./td[@class="title"]/a/text()')
        # 要列表为空的情况下，才能换一个xpath语法  not True——False
        if not name:
            name = tr.xpath('./td[@class="title"]/text()')
        pf = tr.xpath('./td[@class="piaofang"]/span/text()')
        dic['title'] = name[0]
        dic['票房'] = pf[0]
        lst.append(dic)

# 数据保存
with open('piaofang.csv', 'w', encoding='utf-8-sig', newline='') as f:
    # 创建csv对象
    writer = csv.DictWriter(f, fieldnames=('title', '票房'))
    # 写入表头信息
    writer.writeheader()
    # 写入数据
    writer.writerows(lst)


