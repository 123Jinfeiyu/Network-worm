from bs4 import BeautifulSoup

html = """<a>
<b>bbb</b><c>ccc</c><d>ddd</d>
<a>"""
soup = BeautifulSoup(html, 'lxml')
b_tag = soup.b
print(b_tag.next_sibling)  # 下一个兄弟节点
print(list(b_tag.next_siblings))  # 下一个所有的兄弟节点，返回的是生成器

c_tag = soup.c
print(c_tag.previous_sibling)