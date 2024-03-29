# coding: utf-8
import json

import requests
#請求前
url="https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=0&count=20&selected_categories=%7B%22%E7%B1%BB%E5%9E%8B%22:%22%E5%96%9C%E5%89%A7%22,%22%E5%9C%B0%E5%8C%BA%22:%22%E6%AC%A7%E7%BE%8E%22%7D&uncollect=false&tags=%E5%96%9C%E5%89%A7,%E6%AC%A7%E7%BE%8E,2020%E5%B9%B4%E4%BB%A3,%E5%86%92%E9%99%A9&ck=kdcu"
headers={
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Cookie": "viewed=\"25903874\"; bid=YbIsaPIZI_0; ll=\"118238\"; __utmz=30149280.1710995277.8.7.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; dbcl2=\"256489542:9UCSKCd82b0\"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.25648; ck=kdcu; ap_v=0,6.0; __utma=30149280.997776567.1702189322.1710995277.1711690336.9; __utmb=30149280.0.10.1711690336; __utmc=30149280; frodotk_db=\"a41cf34253b31540ec56d9c6fb193fc0\"",
    "Origin": "https://movie.douban.com",
    "Referer": "https://movie.douban.com/explore",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

rep=requests.get(url, headers=headers)
print(rep.text.encode('utf-8'))
#json構造
json_dict=json.dumps(rep.text, ensure_ascii=False)
print(json_dict)
print(type(json_dict))
# 将Unicode字符串转换为UTF-8编码的字节字符串
json_bytes_utf8 = json.dumps(json_dict, ensure_ascii=False).encode('utf-8')

# 将Unicode字符串转换为GBK编码的字节字符串
json_bytes_gbk = json.dumps(json_dict, ensure_ascii=False).encode('gbk')

print(json_bytes_utf8)
print(json_bytes_gbk)
# 請求后包含中文二进制形式的字符串
binary_str = '{"count": 20, "show_rating_filter": true, "recommend_categories": [{"is_control": true, "type": "\u7c7b\u578b", "data": [{"default": true, "text": "\u5168\u90e8\u7c7b\u578b"}, {"default": false, "text": "\u559c\u5267"}, {"default": false, "text": "\u7231\u60c5"}, {"default": false, "text": "\u52a8\u4f5c"}, {"default": false, "text": "\u79d1\u5e7b"}, {"default": false, "text": "\u52a8\u753b"}, {"default": false, "text": "\u60ac\u7591"}, {"default": false, "text": "\u72af\u7f6a"}, {"default": false, "text": "\u60ca\u609a"}, {"default": false, "text": "\u5192\u9669"}, {"default": false, "text": "\u97f3\u4e50"}, {"default": false, "text": "\u5386\u53f2"}, {"default": false, "text": "\u5947\u5e7b"}, {"default": false, "text": "\u6050\u6016"}, {"default": false, "text": "\u6218\u4e89"}, {"default": false, "text": "\u4f20\u8bb0"}, {"default": false, "text": "\u6b4c\u821e"}, {"default": false, "text": "\u6b66\u4fa0"}, {"default": false, "text": "\u60c5\u8272"}, {"default": false, "text": "\u707e\u96be"}, {"default": false, "text": "\u897f\u90e8"}, {"default": false, "text": "\u7eaa\u5f55\u7247"}, {"default": false, "text": "\u77ed\u7247"}]}, {"is_control": true, "type": "\u5730\u533a", "data": [{"default": true, "text": "\u5168\u90e8\u5730\u533a"}, {"default": false, "text": "\u534e\u8bed"}, {"default": false, "text": "\u6b27\u7f8e"}, {"default": false, "text": "\u97e9\u56fd"}, {"default": false, "text": "\u65e5\u672c"}, {"default": false, "text": "\u4e2d\u56fd\u5927\u9646"}, {"default": false, "text": "\u7f8e\u56fd"}, {"default": false, "text": "\u4e2d\u56fd\u9999\u6e2f"}, {"default": false, "text": "\u4e2d\u56fd\u53f0\u6e7e"}, {"default": false, "text": "\u82f1\u56fd"}, {"default": false, "text": "\u6cd5\u56fd"}]}'

# 使用 decode() 方法将二进制字符串解码为 UTF-8 编码的字符串
decoded_str = binary_str.decode('utf-8')

# 输出解码后的中文字符串
print(decoded_str)
# 在Python 2中，Unicode字符串和字节字符串是两种不同的数据类型，有以下区别：
#
# Unicode字符串（Unicode）：
#
# Unicode字符串是以Unicode编码表示的文本数据，可以包含任何语言的字符。
# 在Python 2中，通过在字符串前面加上u前缀来表示Unicode字符串，例如：u'Hello, 你好'。
# Unicode字符串在内存中以Unicode编码形式存在，不依赖于特定的字符编码。
# 字节字符串：
#
# 字节字符串是以特定编码（如UTF-8、GBK等）表示的二进制数据，用来处理非文本数据或特定编码的文本数据。
# 在Python 2中，普通字符串（没有u前缀）即为字节字符串，例如：'Hello, 你好'。
# 字节字符串以字节的形式存储在内存中，需要根据特定编码进行解码才能正确显示文本内容。
# 当你从JSON数据中使用json.loads加载数据时，Python 2会将JSON字符串解析为Unicode字符串。如果你需要将Unicode字符串转换为特定编码的字节字符串，可以使用.encode()方法将其编码为对应的字节序列。
#
# 总的来说，Unicode字符串用于处理文本数据，而字节字符串用于处理二进制数据或特定编码的文本数据。在Python 3中，这两种类型已经合并为字符串类型，并且默认使用Unicode编码。