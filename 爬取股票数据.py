import json
import os
import pandas as pd
import requests
# 初始化一个空的DataFrame
all_data = pd.DataFrame()
for i in range(1,8):
        url=f'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page={i}&num=40&sort=symbol&asc=1&node=hs_bjs&symbol=&_s_r_a=auto'
        headers={
                "Accept-Encoding": "gzip, deflate, sdch",
                "Accept-Language": "en-US,en;q=0.8",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Referer": "http://www.wikipedia.org/",
                "Connection": "keep-alive"
            }
        #方法1
        res=requests.post(url,headers=headers).json()
        pd.set_option('display.max_columns', None)
        df = pd.DataFrame(res)
        # Append data to the total DataFrame using concat
        all_data = pd.concat([all_data, df], ignore_index=True)
# 准备一个换行列表
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
# 重命名 DataFrame 列名
all_data.rename(columns=translation_dict, inplace=True)
# Write the entire DataFrame to the CSV file, mode='a' for append
all_data.to_csv('./炒股3.csv', index=False, encoding='utf-8', mode='a', header=not os.path.exists('./炒股3.csv'))
# Display the entire DataFrame
pd.set_option('display.max_columns', None)

# for key in res[0]:
#     print(key,res[0][key])

#方法2
# res1=json.loads(res.text)

#保存文件
# f = open('data.json', 'w', encoding='utf-8')
# f.write(str(res[0]))
