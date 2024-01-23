import requests
import re
import os

my_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}
res = requests.get("https://pic.netbian.com/4kmeinv/", headers=my_headers)
# print(res.text)
# 数据解析img_url ,re xpath,bs4
img_url_list = re.findall("/uploads/allimg/.*?\.jpg", res.text)
print(img_url_list)

for img_url in img_url_list:
    res = requests.get("https://pic.netbian.com"+img_url)
    # print(res.content)  # res.text:文本数据
    # 文件写操作
    name = os.path.basename(img_url)
    with open("./imgs/" + name, "wb") as f:  # w：写文本 wb写字节
        f.write(res.content)

