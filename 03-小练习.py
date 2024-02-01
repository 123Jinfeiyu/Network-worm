from lxml import etree
import csv

# 需求：获取href属性值以及a标签的文本内容，并且将数据保存到表格当中
wb_data = """
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
"""
# 创建对象
html = etree.HTML(wb_data)
all_a = html.xpath('//li/a')
# print(all_a)
# 循环遍历  [(),()]  [{},{},{}]
lst = []
for a in all_a:
    dic = {}
    # print(a)
    # a标签的基础上，可以取链接，文本信息
    dic["链接"] = a.xpath('@href')[0]
    dic["内容"] = a.xpath('text()')[0]
    print(dic)
    lst.append(dic)  # append() 添加

# 数据保存
with open('练习.csv', 'w', encoding='utf-8-sig', newline='') as f:
    # 1. 创建写入对象
    write = csv.DictWriter(f, fieldnames=("链接", "内容"))
    # 2. 写入表头
    write.writeheader()
    # 3. 写入数据
    write.writerows(lst)


# # 先获取属性值
# links = html.xpath('//li/a/@href')
# # 获取文本内容
# results = html.xpath('//li/a/text()')
# print(links, results)

'''
链接         文本
link1.html first item

'''
