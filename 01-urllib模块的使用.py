# urllib是内置模块，不需要额外安装
import urllib.request

url = 'https://img1.baidu.com/it/u=2559867097,3726275945&fm=253&fmt=auto&app=138&f=JPEG?w=1333&h=500'

# 直接保存
# 目标网址，保存路径
# 这个方法是基于网站没有做任何反爬的情况下使用（requests)
urllib.request.urlretrieve(url, '图片.jpg')