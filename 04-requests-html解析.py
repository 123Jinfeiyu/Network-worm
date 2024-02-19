from requests_html import HTMLSession

session = HTMLSession()

url = 'https://www.sogou.com'

# 发请求
res = session.get(url)

# 使用css语法 find默认找多个标签
data = res.html.find('a#weixinch')[0]
print(data.text)
print(data.attrs['href'])  # 返回的数据类型 字典
print(data.attrs.get('href'))  # 返回的数据类型 字典
'''
字典取值
dic = {'name': 'xxx'}
dic['age']: 当key不存在，会报错
dic.get('age'): 当key不存在，不会报错，返回None
'''