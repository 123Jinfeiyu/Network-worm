from bs4 import BeautifulSoup
import requests
import csv

url = 'http://www.piaofang.biz/'

res = requests.get(url)
res.encoding = 'gb2312'
# 发请求，获取响应内容
# print(res.text)
# 数据解析
html = BeautifulSoup(res.text, 'lxml')
# 解析数据，解析响应的源码，还是元素的源码？
zhuti = html.find('div', class_='zhuti')
trs = zhuti.find_all('tr')
# print(len(trs))
'''
标题：第一个tr不需要（切片)
如果是空行，tr长度是为0
'''
lst = []
for tr in trs[1:]:
    dic = {}
    if len(tr) != 0:
        # 取值 返回的数据类型 是列表 当前节点用点表示
        name = tr.find('td', class_='title')
        #对比name = tr.xpath('./td[@class="title"]/a/text()')
        # if len(name) == 0:
        #     name = tr.xpath('./td[@class="title"]/text()')
        pf = tr.find('td', class_='piaofang')
        # print(list(name.stripped_strings))
        dic['电影名称'] = ''.join(list(name.stripped_strings))
        #将list中零散的元素进行拼接
        dic['票房'] = list(pf.stripped_strings)[0]
        print(dic)
        lst.append(dic)

with open('movie.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=('电影名称', '票房'))
    writer.writeheader()
    writer.writerows(lst)