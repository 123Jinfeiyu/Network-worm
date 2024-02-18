from lxml import etree
import requests
import csv

url = 'http://www.piaofang.biz/'

res = requests.get(url)
res.encoding = 'gb2312'
# 发请求，获取响应内容
# print(res.text)
# 数据解析
html = etree.HTML(res.text)
# 解析数据，解析响应的源码，还是元素的源码？响应的源码
trs = html.xpath('//div[@class="zhuti"]/table/tr')
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
        name = tr.xpath('./td[@class="title"]/a/text()')
        if len(name) == 0:
            name = tr.xpath('./td[@class="title"]/text()')
        pf = tr.xpath('./td[@class="piaofang"]/span/text()')
        dic['电影名称'] = name[0]
        dic['票房'] = pf[0]
        lst.append(dic)
print(lst)
with open('movie.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=('电影名称', '票房'))
    writer.writeheader()
    writer.writerows(lst)