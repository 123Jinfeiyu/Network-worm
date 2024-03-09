## 导包
from lxml import etree
import requests
# from fake_useragent import UserAgent
import random
import time
import csv

## 创建文件对象
f = open('58同城石家庄在售楼盘信息_221个.csv', 'w', encoding='utf-8-sig', newline="")  # 创建文件对象
csv_write = csv.DictWriter(f, fieldnames=['房源的标题', '所在区', '地址', '价格','类型','面积','建造时间'])
csv_write.writeheader()  # 写入文件头

## 设置请求头参数：User-Agent, cookie, referer
cookies= 'f=n; isp=true; 58_ctid=241; is_58_pc=1; commontopbar_new_city_info=28%7C%E7%9F%B3%E5%AE%B6%E5%BA%84%7Csjz; ctid=28; aQQ_ajkguid=3A35F45C-4100-4332-9095-SX0309210955; sessid=ABF4E2C6-6578-BDF2-1DD4-SX0309210955; id58=CpQQXmXsX6Nef0grC5eiAg==; 58tj_uuid=229c793a-92df-44e3-ad94-e85efa9271da; new_uv=1; wmda_uuid=05b6f82541aaa5f62be842a6474923ce; wmda_new_uuid=1; wmda_visited_projects=%3B8788302075828; 58home=kaifeng; xxzlclientid=004af241-4dce-4cba-a023-1709989797284; xxzlxxid=pfmxakHgw67y5nCKxq4KU2C+ix9o8IOXwwoZt9jm8Eq86/C7WzfMbmjKAMprB/48ghwv; als=0; f=n; wmda_visited_projects=%3B8788302075828%3B2385390625025; commontopbar_new_city_info=241%7C%E7%9F%B3%E5%AE%B6%E5%BA%84%7Csjz; commontopbar_ipcity=kaifeng%7C%E5%BC%80%E5%B0%81%7C0; xxzl_deviceid=lyvg8UEeMOdI4Q0ADTUU%2Frmm6WhGo9STtLOwWFNu8nmaxUveUnWMAmhBO68DXVj5; xxzlbbid=pfmbM3wxMDMyMHwxLjUuMHwxNzA5OTkwMjU3MDAyfDR5cnZOaEc2V1c0Tkh4SHFueDdsWU9TYTJXbGR6TGVYaUtPZGNMSUMvRDQ9fDMyNWRmYWY1NTM1MTY0NDhiYTc4NDFhZjlhOTAxNGY4XzE3MDk5ODk3OTg3MzBfN2I2Mzk4Nzk2MTYwNDFiYTkxYmMyMjExNDM4MzdlZjZfMzA2MTA3NDgyM3w2ZGUwZjZiMGZhMjlhNDljMjAxMjFiNWE2NmY0NTkwMl8xNzA5OTkwMjU2NTE3XzEzOA==; xxzl_cid=8375f6c837d14ddd9c529610fca14646; xxzl_deviceid=vrfnMnMpzsIKfCLHsTP++Hcv/cnIjI+djXie7QD1dD8izDAx05t+PU+Z4058hAWU'
headers = {
    # 随机生成User-Agent
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    # 不同用户不同时间访问，cookie都不一样，根据自己网页的来，获取方法见另一篇博客：Python之反爬虫手段
    'cookie': cookies,
    # 设置从何处跳转过来
    'referer': 'https://sjz.58.com/xinfang/loupan/all/a1_p1_w1/',
}

## 总共筛选出221个在售楼盘，每页有60个楼盘，需爬取4页
for i in range(3):
    # 遍历url
    url = 'https://sjz.58.com/xinfang/loupan/all/a1_p{}_w1/'.format(i)
    # 请求发送
    page_text = requests.get(url=url, headers=headers).text
    # 数据解析
    tree = etree.HTML(page_text)
    #house_type房屋类型
    house_type=tree.xpath("//div[@class='tag-panel']/i[@class='status-icon wuyetp']/text()")

    #获取房屋的面积
    house_area=tree.xpath("//span[@class='building-area']/text()")
    area=[x.split('：')[1] for x in house_area]

    # 房屋的建造时间
    house_bulid_time = tree.xpath("//div[@class='tag-panel']/i[@class='status-icon onsale']/text()")

    # 获取小区名称字段
    communityName = tree.xpath("//div[@class='item-mod ']//a[@class='lp-name']/span/text()")

    # 获取长字符串
    detailAddress = tree.xpath("//div[@class='item-mod ']//a[@class='address']/span/text()")
    # 获取所在区字段
    district = [x[2:4] for x in detailAddress]
    # 获取地址字段
    address = [x.split(']')[1][1:] for x in detailAddress]
    # 获取均价字段
    price = tree.xpath("//a[@class='favor-pos']/p[@class='price' or 'favor-tag around-price']/span/text()")

    # 将数据读入csv文件
    for j in range(len(communityName)):  # 每页60个在售楼盘，最后一页不到60个
        data_dict = {'房源的标题': communityName[j], '所在区': district[j], '地址': address[j], '价格': int(price[j]),'类型':house_type[j],'面积':area[j],'建造时间':house_bulid_time[j]}
        csv_write.writerow(data_dict)

    print('第{}页爬取成功'.format(i + 1))

    # 设置睡眠时间间隔，防止频繁访问网站
    time.sleep(random.randint(5, 10))

print('-------------')
print('全部爬取成功！')