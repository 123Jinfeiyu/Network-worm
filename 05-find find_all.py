'''
find: 查找一个标签元素
find_all: 查找多个标签元素
'''
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
xmind
"""
soup = BeautifulSoup(html_doc, 'lxml')

# 找一个a标签 查找一个， 默认找的就是第一个
# a_tag = soup.find('a')
# 找所有符合条件的标签，返回的数据类型是list
a_tag = soup.find_all('a')
print(a_tag.string)

