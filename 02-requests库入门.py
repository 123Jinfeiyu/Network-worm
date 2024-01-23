import requests

'''
需求：抓取百度首页的源码，保存html文件
1. 确认url：https://www.baidu.com/
2. 发请求，获取响应内容：(get)
'''
# 网址
url = 'https://www.baidu.com/'
'''
碰到反爬，给程序做伪装：伪装的第一步，添加User-Agent（用户代理),简称ua
伪装请求头：是字典数据类型{"key":"value"}
引号之间不用留空格
'''
head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
# 发请求, 得到的内容响应
# 将响应赋值给res这个变量
res = requests.get(url, headers=head)
print(res)  # <Response [200]>  200代表请求成功
# 获取响应内容 文本内容  二进制数据（图片，视频，音频)
# print(res.text)  # 获取响应的文本内容
# 查看代码的请求头
print(res.request.headers)  # 查看请求头信息
# .txt word html
# 保存文件： 上下文管理器  w：写入  r：读取  a：追加
with open('百度.html', 'w', encoding='utf-8') as f:
    f.write(res.text)  # 写入方法

# 20:49上课
