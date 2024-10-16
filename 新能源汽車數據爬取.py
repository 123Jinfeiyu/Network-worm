import json
import pandas as pd
import requests
from tqdm import tqdm

url = 'https://yhgscx.miit.gov.cn/fuel-consumption-center/fuel-consumption-center/fcSearchCtr/queryList'
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': '',
    'connection': 'keep-alive',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': 'wzws_sessionid=gDIyMi4xMzcuMTg4Ljg5oGcON1SBMTY0NTNkgjEwMDJmYQ==; route=1728984916.823.1668.337225',
    'host': 'yhgscx.miit.gov.cn',
    'origin': 'https://yhgscx.miit.gov.cn',
    'referer': 'https://yhgscx.miit.gov.cn/fuel-consumption-web/mainPage',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

# 初始化数据存储列表publicTimeEnd
# :
# ""
# publicTimeStart
# :
# ""
data = []

# 使用tqdm创建进度条
for num in tqdm(range(1, 46), desc="Fetching pages"):
    payload = {
        "oversrasName": "",
        "reportType": "2",
        "vehicleType": "",
        "vehicleBrand": "",
        "displacement": "",
        "driveType": "",
        "usualName": "",
        "runingRange": "",
        "vehicleProduce": "",
        "vehicleNumber": "",
        "fuelType": "",
        "publicTimeStart": "2015-01-01 00:00:00",
        "publicTimeEnd": "2023-12-01 00:00:00",
        "currentPage": num,
        "pageSize": 200,
        "position": "right",
        "pageSizes": [10, 30, 50, 100, 200],
        "layout": "sizes, total,prev, pager, next, jumper",
        "totalSize": 11499
    }

    # 发送POST请求
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response_data = json.loads(response.text)

    # 提取新能源汽车的列表
    vehicles = response_data['info']['list']

    # 提取所需数据并添加到data列表中
    for vehicle in vehicles:
        data.append({
            "汽车制造商": vehicle.get('oversrasName', 'null'),
            "汽车名称": vehicle.get('usualName', 'null'),
            "新能源汽车名字": vehicle.get('vehicleNumber', 'null'),
            "新能源汽车功率": vehicle.get('ratedPower', 'null'),
            "新能源汽车排量": vehicle.get('displacement', 'null'),
            "新能源汽车的启动日期": vehicle.get('publicTime', 'null')
        })

# 将数据转换为DataFrame
df = pd.DataFrame(data)

# 保存到Excel文件
excel_filename = 'new_energy_vehicles.xlsx'
df.to_excel(excel_filename, index=False, engine='openpyxl')

print(f'Data saved to {excel_filename}')