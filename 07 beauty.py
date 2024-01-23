import requests

url = "https://pic.netbian.com/uploads/allimg/231213/233751-17024818714f51.jpg"

res = requests.get(url)

# print(res.content)  # res.text:文本数据

# 文件写操作
with open("美女.jpg", "wb") as f:  # w：写文本 wb写字节
    f.write(res.content)
