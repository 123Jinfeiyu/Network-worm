import requests

# requests.get()
# requests.post()
url = "https://www.baidu.com/"
res = requests.get(url)  # res是响应对象，包含了所有的响应信息

# print(res.status_code)
# print(res.headers)
# print(res.text)

# 文件写操作
with open("baidu.html", "w") as f:
    f.write(res.text)
