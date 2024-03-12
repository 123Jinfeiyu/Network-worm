#地址: https://weibo.com/需求:在该平台，找评论超过100的任意动态，
# 采集评论区的数据采集字段:评论用户id+评论时间(需将时间戳转换为北京时间+评论内容+用户地点)
# 数据存储方案: CSV. exceI二者选一
import json

import pandas as pd
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
url = 'https://weibo.com/'
cookies = 'wb_view_log=1280*7201.5; SINAGLOBAL=9635437729971.254.1710059539963; ULV=1710059539966:1:1:1:9635437729971.254.1710059539963:; ALF=1712651577; SUB=_2A25I6QBoDeRhGeBI7VMS8SbNyzSIHXVrhx2grDV8PUJbkNAGLWrnkW1NRmoMsXM96fxAuhzRggtAJgdx_I4-jlKt; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFr1YYkM8.hl666PGGWWZNz5JpX5o275NHD95QcSoqpe02ReK5RWs4Dqcj_i--Ni-i2iK.Ni--fi-2EiKL8i--fiKnXiK.Ei--fi-i8iK.Ei--fi-ihiKLs; ariaDefaultTheme=default; ariaFixed=true; ariaReadtype=1; ariaMouseten=null; ariaStatus=false; XSRF-TOKEN=YnB8KfCJ36otfqP-S847ppm_; WBPSESS=0vmKPeK7luZI9mjGad-L_5R_17x4vrEBSMnXRmp44tuSjtuhphO2wJ4Xqi-XqhSzfoImPu0_i-M0bbdojrDzb6oL3njv55xukYxVzTK2kUH0MaqNLzyRruL1QZHhpA2pHtn-UDp5NgIO_B3EcqM-3w=='
#携带cookie发送请求
#获取内容
def get_content_1(uid, mid, the_first=True, max_id=None):
    headers = {
        "authority": "weibo.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "client-version": "v2.44.75",
        "cookie": "wb_view_log=1280*7201.5; SINAGLOBAL=9635437729971.254.1710059539963; ULV=1710059539966:1:1:1:9635437729971.254.1710059539963:; ALF=1712651577; SUB=_2A25I6QBoDeRhGeBI7VMS8SbNyzSIHXVrhx2grDV8PUJbkNAGLWrnkW1NRmoMsXM96fxAuhzRggtAJgdx_I4-jlKt; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFr1YYkM8.hl666PGGWWZNz5JpX5o275NHD95QcSoqpe02ReK5RWs4Dqcj_i--Ni-i2iK.Ni--fi-2EiKL8i--fiKnXiK.Ei--fi-i8iK.Ei--fi-ihiKLs; ariaDefaultTheme=default; ariaFixed=true; ariaReadtype=1; ariaMouseten=null; ariaStatus=false; XSRF-TOKEN=YnB8KfCJ36otfqP-S847ppm_; WBPSESS=0vmKPeK7luZI9mjGad-L_5R_17x4vrEBSMnXRmp44tuSjtuhphO2wJ4Xqi-XqhSzfoImPu0_i-M0bbdojrDzb6oL3njv55xukYxVzTK2kUH0MaqNLzyRruL1QZHhpA2pHtn-UDp5NgIO_B3EcqM-3w==",
        "referer": "https://weibo.com/",
        "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Microsoft Edge\";v=\"122\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "server-version": "v2024.03.06.1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
        "x-requested-with": "XMLHttpRequest",
        "x-xsrf-token": "YnB8KfCJ36otfqP-S847ppm_",
        "cookie": cookies,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',

    }

    params = {
        'is_reload': '1',
        'id': f'{mid}',
        'is_show_bulletin': '2',
        'is_mix': '0',
        'count': '20',
        'uid': f'{uid}',
        'fetch_level': '0',
        'locale': 'zh-CN',
    }

    if not the_first:
        params['flow'] = 0
        params['max_id'] = max_id
    else:
        pass
    response = requests.get('https://weibo.com/ajax/statuses/buildComments', params=params,headers=headers)
    return response
#回调检验
# res=get_content_1()
#数据解析
def get_content_2(get_content_1_url):
    headers = {
        "authority": "weibo.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "client-version": "v2.44.75",
        "cookie": "wb_view_log=1280*7201.5; SINAGLOBAL=9635437729971.254.1710059539963; ULV=1710059539966:1:1:1:9635437729971.254.1710059539963:; ALF=1712651577; SUB=_2A25I6QBoDeRhGeBI7VMS8SbNyzSIHXVrhx2grDV8PUJbkNAGLWrnkW1NRmoMsXM96fxAuhzRggtAJgdx_I4-jlKt; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFr1YYkM8.hl666PGGWWZNz5JpX5o275NHD95QcSoqpe02ReK5RWs4Dqcj_i--Ni-i2iK.Ni--fi-2EiKL8i--fiKnXiK.Ei--fi-i8iK.Ei--fi-ihiKLs; ariaDefaultTheme=default; ariaFixed=true; ariaReadtype=1; ariaMouseten=null; ariaStatus=false; XSRF-TOKEN=YnB8KfCJ36otfqP-S847ppm_; WBPSESS=0vmKPeK7luZI9mjGad-L_5R_17x4vrEBSMnXRmp44tuSjtuhphO2wJ4Xqi-XqhSzfoImPu0_i-M0bbdojrDzb6oL3njv55xukYxVzTK2kUH0MaqNLzyRruL1QZHhpA2pHtn-UDp5NgIO_B3EcqM-3w==",
        "referer": "https://weibo.com/",
        "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Microsoft Edge\";v=\"122\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "server-version": "v2024.03.06.1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
        "x-requested-with": "XMLHttpRequest",
        "x-xsrf-token": "YnB8KfCJ36otfqP-S847ppm_",
        "cookie": cookies,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',

    }

    s = '{"name":"https://weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id=4944997453660231&is_show_bulletin=2&is_mix=0&max_id=139282732792325&count=20&uid=1762257041&fetch_level=0&locale=zh-CN","entryType":"resource","startTime":20639.80000001192,"duration":563,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","renderBlockingStatus":"non-blocking","workerStart":0,"redirectStart":0,"redirectEnd":0,"fetchStart":20639.80000001192,"domainLookupStart":20639.80000001192,"domainLookupEnd":20639.80000001192,"connectStart":20639.80000001192,"secureConnectionStart":20639.80000001192,"connectEnd":20639.80000001192,"requestStart":20641.600000023842,"responseStart":21198.600000023842,"firstInterimResponseStart":0,"responseEnd":21202.80000001192,"transferSize":7374,"encodedBodySize":7074,"decodedBodySize":42581,"responseStatus":200,"serverTiming":[],"dns":0,"tcp":0,"ttfb":557,"pathname":"https://weibo.com/ajax/statuses/buildComments","speed":0}'
    s = json.loads(s)
    print(type(s))
    s['name'] = get_content_1_url
    s = json.dumps(s)
    print(type(s))
    data = f'------WebKitFormBoundaryNs1Toe4Mbr8n1qXm\r\nContent-Disposition: form-data; name="entry"\r\n\r\n{s}\r\n------WebKitFormBoundaryNs1Toe4Mbr8n1qXm\r\nContent-Disposition: form-data; name="request_id"\r\n\r\n\r\n------WebKitFormBoundaryNs1Toe4Mbr8n1qXm--\r\n'
    response = requests.post('https://weibo.com/ajax/log/rum', headers=headers, data=data)
    return response.text
#创建会话对象与浏览器保持连接
# session=HTMLSession()
# r=session.get(url)
# print(r.html.html)
#等价替换
#主函数
def get_once_data(uid, mid,the_first=True, max_id=None):
    respones_1 = get_content_1(uid, mid, the_first, max_id)
    print(respones_1)
    url = respones_1.url

    response_2 = get_content_2(url)
    df = pd.DataFrame(respones_1.json()['data'])
    max_id = respones_1.json()['max_id']
    return max_id, df


if __name__ == '__main__':
    # 自定义
    name = '一级微博爬取目录'
    mid='4937550524843111'
    uid='7817933011'
    page=100
    df_list=[]
    max_id=''
    for i in range(page):
        if i==0:
            max_id, df = get_once_data(uid=uid, mid=mid)
        else:
            max_id, df = get_once_data(uid=uid, mid=mid, the_first=False, max_id=max_id)
        if df.shape[0] == 0 or max_id == 0:
            break
        else:
            df_list.append(df)
            print(f'第{i}页解析完毕！max_id:{max_id}')
    df = pd.concat(df_list).astype(str).drop_duplicates()
    df.to_csv(f'{name}.csv', index=False,encoding="utf_8_sig")
# for k,v in rep.cookies.items():
#      print(k+"="+v)