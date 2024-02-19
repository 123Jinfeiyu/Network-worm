# 1. 导包
from requests_html import HTMLSession

# 2. 实例化（需要加上括号)
session = HTMLSession()

# 3. 准备请求的url
url = 'https://www.baidu.com'

# 4. 发请求，获取响应
# get请求
# res = session.get(url)
# post请求
res = session.post(url)
# 查看请求头参数 内部自带了ua
print(res.request.headers)
# 获取响应内容
# print(res.text)