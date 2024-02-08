import re
import csv
import requests
from lxml import etree

'''
目标网站：
https://www.dy2018.com/html/gndy/dyzz/index.html
'''
lst = []
for page in range(1, 4):
    url = f'https://www.dy2018.com/html/gndy/dyzz/index_{page}.html'

    head = {
        'Cookie': 'guardret=AAMA; guard=11256197NCEHBAM=; Hm_lvt_8e745928b4c636da693d2c43470f5413=1704617670,1706680740,1706851576,1707130164; Hm_lpvt_8e745928b4c636da693d2c43470f5413=1707130164; Hm_lvt_93b4a7c2e07353c3853ac17a86d4c8a4=1704617670,1706680740,1706851576,1707130164; Hm_lpvt_93b4a7c2e07353c3853ac17a86d4c8a4=1707130164; Hm_lvt_0113b461c3b631f7a568630be1134d3d=1704617670,1706680740,1706851576,1707130164; Hm_lpvt_0113b461c3b631f7a568630be1134d3d=1707130164',
        'Referer': 'https://www.dy2018.com/?',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }
    res = requests.get(url, headers=head)
    res.encoding = 'gb2312'
    html = etree.HTML(res.text)
    # print(res.text)
    tables = html.xpath('//div[@class="co_content8"]/ul/td/table')

    for t in tables:
        # 获取详情页链接
        href = 'https://www.dy2018.com/' + t.xpath('./tr[2]/td[2]/b/a/@href')[0]
        # 向详情页url发请求
        detail_res = requests.get(href, headers=head)
        detail_res.encoding = 'gb2312'
        # 获取详情页源码
        detail_html = etree.HTML(detail_res.text)
        content = ''.join(detail_html.xpath('//div[@id="Zoom"]/text()')).replace(' ', '')
        # print(content)
        # 利用正则解析数据，将数据保存到字典当中
        dic = {}
        dic['译名'] = re.search('译　　名(.*?)◎', content).group(1).replace('\u3000', '')
        dic['类型'] = re.search('类　　别(.*?)◎', content).group(1).replace('\u3000', '')
        star = re.search('.*?评分(.*?)◎', content)
        if star:
            dic['评分'] = star.group(1).replace('\u3000', '')
        else:
            dic['评分'] = ''
        download = detail_html.xpath('//div[@id="downlist"]/table/tbody/tr/td/a/@href')[0]
        dic['下载地址'] = re.search('(.*?\.mp4)', download).group(1)
        print(dic)
        lst.append(dic)

with open('电影天堂.csv', 'w', encoding='utf-8-sig', newline='') as f:
    write = csv.DictWriter(f, fieldnames=('译名', '类型', '评分', '下载地址'))
    write.writeheader()
    write.writerows(lst)