import requests

'''
根据搜索内容，抓取对应源码内容
保存html源码内容

'''
# 规范代码 ctrl+alt+L
# 字典里面有多个值的情况，用逗号隔开
# ？后面都是参数
head = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
url = 'https://www.baidu.com/s'
# 通过正则表达式，快速转字典
data = {
    'wd': 'python',
    'rsv_spt': '1',
    'rsv_iqid': '0xf70517eb0063a853',
    'issp': '1',
    'f': '8',
    'rsv_bp': '1',
    'rsv_idx': '2',
    'ie': 'utf-8',
    'tn': 'baiduhome_pg',
    'rsv_dl': 'tb',
    'rsv_enter': '1',
    'rsv_sug3': '8',
    'rsv_sug1': '6',
    'rsv_sug7': '101',
    'rsv_sug2': '0',
    'rsv_btype': 'i',
    'prefixsug': 'python',
    'rsp': '8',
    'inputT': '1717',
    'rsv_sug4': '153455',
    'rsv_sug': '1',
}

# 发请求，获取响应内容
res = requests.get(url, headers=head, params=data)
# 解决乱码,看源码 charset='编码' ctrl+F
res.encoding = 'utf-8'
# 打印响应内容
print(res.text)
