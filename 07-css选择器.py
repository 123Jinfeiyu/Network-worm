'''
教程：http://www.w3cmap.com/cssref/css-selectors.html
'''
# 1. 导入库
from bs4 import BeautifulSoup

# 模拟的是网页源码
html_doc = """
<html><head><title>The Dormouse's story<span>aaa</span></title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<a>aaaa<span>bbb</span></a>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister1" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'lxml')
# 定位标签, 默认是找所有的标签
# print(soup.select('a'))
# 通过class属性定位
# print(soup.select('a', class_="sister1"))  # 不行
# css选择器：标签.属性值
# print(soup.select('a.sister1'))  #
# id="link1" 标签#link1
# print(soup.select('a#link2'))  #

# 获取文本信息, 列表.string这是不可行的，用索引取的是标签
# print(soup.select('a#link2')[0].string)
# print(soup.select('a#link2')[0].text)

# 其他
# print(soup.select('p a'))  # 选择所有位于p元素内部的<a>标签,无论嵌套层数，都是可以获取到
# print(soup.select('p>a'))  # 选择所有作为p标签直接子元素的a标签
print(soup.select('p+a'))  # 选择所有紧接着<p>元素之后的<a>标签

