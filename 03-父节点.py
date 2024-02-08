# 1. 导入库
from bs4 import BeautifulSoup
# 模拟的是网页源码
html_doc = """
<html><head><title>The Dormouse's story<span>aaa</span></title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'lxml')

# 定位到title标签
# title_tag = soup.title
# print(title_tag.parent)  # parent：父亲的意思  获取当前标签的父标签

a_tag = soup.a
# print(a_tag.parents)  # 返回的也是生成器
for i in a_tag.parents:
    print(i.name)  # 获取标签的名字