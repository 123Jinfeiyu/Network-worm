from requests_html import HTMLSession

session = HTMLSession()

url = 'https://www.sogou.com/web?query=python&_asf=www.sogou.com&_ast=&w=01015002&p=40040108&ie=utf8&from=index-nologin&s_from=index&oq=&ri=0&sourceid=sugg&suguuid=&sut=0&sst0=1708344099409&lkt=0%2C0%2C0&sugsuv=1696940988658509&sugtime=1708344099409'

# 发请求
res = session.get(url)

# res.text
# res.html
# print(res.html.text)
# with open('sougou1.html', 'w', encoding='utf-8') as f:
#     f.write(res.html.html)

# {k:v} {1, 3, 2}:集合的特点：去重，无序
print(res.html.absolute_links)  # 网页当中的绝对路径
print(res.html.links)   # 获取网页的相对路径
print(res.html.base_url) # 当前请求的url