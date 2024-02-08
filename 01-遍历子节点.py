# 1. 导入库
from bs4 import BeautifulSoup
# 模拟的是网页源码
html_doc = """
<html><head><title>The Dormouse's story</title></head>
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
# <head><title>The Dormouse's story</title></head>
head_tag = soup.head
print(head_tag.contents)  # 返回子标签内容， 数据类型是列表
'''
迭代器.生成器：next()/循环/强制转换
.string
'''
print(list(head_tag.children))  # 孩子  list_iterator，迭代器取值
# 获取子子孙孙
print(list(head_tag.descendants))  # generator
