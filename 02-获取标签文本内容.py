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

# <title>The Dormouse's story</title>
title_tag = soup.title
# print(title_tag.string)
# print(title_tag.text)

# <head><title>The Dormouse's story<span>aaaa</span></title></head>
# head = soup.head
# print(head.string)  # None
# print(head.text)  # 标签文本内容进行了拼接
'''
当直接定位title标签，标签里面有文本，两者返回的结果是一致
当定位head标签，只有一个子标签有文本内容，两种返回的结果是一致
当定位head标签， 多个子标签有文本内容，
string,因为文本数量>=2 时，string不知道获取哪一个
.text: 两段文本的拼接
'''
html = soup.html
# result = html.text
# result = html.strings  # 获取多个
result = html.stripped_strings  # 获取多个
print(list(result))
# for i in result:
#     print(i)

'''
获取一个标签里面的文本
string/text
获取多个子标签的文本内容
strings
stripped_strings: 可以去除多余的换行符
'''