from requests_html import HTMLSession

session = HTMLSession()

url = 'https://www.sogou.com'

# 发请求
res = session.get(url)
# 获取响应数据 获取属性值, 返回的数据类型列表
data = res.html.xpath('//input[@id="stb"]/@value')
print(data[0])
# 获取文本内容
result = res.html.xpath('//a[@id="weixinch"]/text()')
print(result[0])