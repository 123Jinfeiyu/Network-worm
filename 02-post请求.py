import requests
import pandas as pd
# # 读取CSV文件
# df = pd.read_csv('炒股1.csv')
# url = 'https://fanyi.so.com/index/search'
# # 设置了请求头参数
# head = {
#     'Pro': 'fanyi',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
# }
# trs = input("请输入你翻译的内容：")
# '''
# trs[0]: 取的是第一个值,进行编码，求长度
# 如果长度为1：输入英文，英译汉
# 如果长度为3：输入中文，汉译英
# '''
# length = len(trs[0].encode('utf-8'))
# if length == 3:
#     eng = 0
# else:
#     eng = 1
# # 参数得是字典格式的 英译汉
# '''
# eng: 1 英译汉
# eng：0 汉译英
# '''
# arg = {
#     'eng': eng,
#     # 如果参数为空的情况，要么删除，要么设置为空字符
#     'ignore_trans': 0,
#     'query': trs,
# }
# # 发请求，获取响应
# '''
# get请求：parmas=arg
# post请求：data=arg
# '''
# res = requests.post(url, data=arg, headers=head)
#
# # 打印响应内容
# # res.text: 获取的内容数据类型字符串，数据格式是json格式，转换字典数据类型
# # json.loads()
# # print(res.text)
# result = res.json()  # 数据已经拿到了
# print(result['data']['fanyi'])  # 将json格式的数据转换成对应的python对象
'''
url是正确的
post请求携带了参数
最后：没有拿到数据(考虑，反爬）

'''
import requests
import pandas as pd

# 读取CSV文件
df = pd.read_csv('炒股1.csv')

# 定义列名的英文到中文的映射
translation_dict = {
    'symbol': '股票代码',
    'code': '代码',
    'name': '股票名称',
    'trade': '成交价',
    'pricechange': '价格变动',
    'changepercent': '涨跌幅',
    'buy': '买入价',
    'sell': '卖出价',
    'settlement': '昨收',
    'open': '开盘价',
    'high': '最高价',
    'low': '最低价',
    'volume': '成交量',
    'amount': '成交额',
    'ticktime': '时间',
    'per': '市盈率',
    'pb': '市净率',
    'mktcap': '总市值',
    'nmc': '流通市值',
    'turnoverratio': '换手率'
}

url = 'https://fanyi.so.com/index/search'
# 设置了请求头参数
head = {
    'Pro': 'fanyi',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

# 遍历字典的每个键值对，进行翻译
for en_col, cn_col in translation_dict.items():
    # 发送翻译请求
    res = requests.post(url, data={'query': en_col, 'eng': 1}, headers=head)
    result = res.json()

    # 获取翻译结果并更新字典
    translation_dict[en_col] = result['data']['fanyi']

# 重命名 DataFrame 列名
df.rename(columns=translation_dict, inplace=True)

# 保存为新的CSV文件
df.to_csv('炒股_translated.csv', index=False, encoding='utf-8')

