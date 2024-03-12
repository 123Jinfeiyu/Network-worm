import requests
import os
from bs4 import BeautifulSoup
import pandas as pd
import json

# 设置为自己的cookies
cookies = {
    "SINAGLOBAL": "9635437729971.254.1710059539963",
    "ALF": "1712651577",
    "SUB": "_2A25I6QBoDeRhGeBI7VMS8SbNyzSIHXVrhx2grDV8PUJbkNAGLWrnkW1NRmoMsXM96fxAuhzRggtAJgdx_I4-jlKt",
    "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9WFr1YYkM8.hl666PGGWWZNz5JpX5o275NHD95QcSoqpe02ReK5RWs4Dqcj_i--Ni-i2iK.Ni--fi-2EiKL8i--fiKnXiK.Ei--fi-i8iK.Ei--fi-ihiKLs",
    "ariaDefaultTheme": "default",
    "ariaFixed": "true",
    "ariaReadtype": "1",
    "ariaMouseten": "null",
    "ariaStatus": "false",
    "XSRF-TOKEN": "YnB8KfCJ36otfqP-S847ppm_",
    "WBPSESS": "0vmKPeK7luZI9mjGad-L_5R_17x4vrEBSMnXRmp44tuSjtuhphO2wJ4Xqi-XqhSzfoImPu0_i-M0bbdojrDzb6oL3njv55xukYxVzTK2kUH0MaqNLzyRruL1QZHhpA2pHtn-UDp5NgIO_B3EcqM-3w==",
    "_s_tentry": "weibo.com",
    "Apache": "2824423445290.6025.1710089741335",
    "ULV": "1710089741382:2:2:2:2824423445290.6025.1710089741335:1710059539966"
}


def get_the_list_response(q='话题', n='1', p='页码'):
    headers = {
        "authority": "weibo.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cookie": "SINAGLOBAL=9635437729971.254.1710059539963; ALF=1712651577; SUB=_2A25I6QBoDeRhGeBI7VMS8SbNyzSIHXVrhx2grDV8PUJbkNAGLWrnkW1NRmoMsXM96fxAuhzRggtAJgdx_I4-jlKt; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFr1YYkM8.hl666PGGWWZNz5JpX5o275NHD95QcSoqpe02ReK5RWs4Dqcj_i--Ni-i2iK.Ni--fi-2EiKL8i--fiKnXiK.Ei--fi-i8iK.Ei--fi-ihiKLs; ariaDefaultTheme=default; ariaFixed=true; ariaReadtype=1; ariaMouseten=null; ariaStatus=false; XSRF-TOKEN=YnB8KfCJ36otfqP-S847ppm_; WBPSESS=0vmKPeK7luZI9mjGad-L_5R_17x4vrEBSMnXRmp44tuSjtuhphO2wJ4Xqi-XqhSzfoImPu0_i-M0bbdojrDzb6oL3njv55xukYxVzTK2kUH0MaqNLzyRruL1QZHhpA2pHtn-UDp5NgIO_B3EcqM-3w==; _s_tentry=weibo.com; Apache=2824423445290.6025.1710089741335; ULV=1710089741382:2:2:2:2824423445290.6025.1710089741335:1710059539966",
        "origin": "https://s.weibo.com",
        "referer": "https://s.weibo.com/",
        "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Microsoft Edge\";v=\"122\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}

    params = {
        'q': q,
        'nodup': n,
        'page': p,
    }
    response = requests.get('https://s.weibo.com/weibo', params=params, cookies=cookies, headers=headers)
    return response


def parse_the_list(text):
    #bs4语法解析
    soup = BeautifulSoup(text)
    divs = soup.select('div[action-type="feed_list_item"]')
    lst = []
    for div in divs:
        mid = div.get('mid')
        time = div.select('div.card-feed > div.content > div.from > a:first-of-type')
        if time:
            time = time[0].string.strip()
        else:
            time = None
        p = div.select('div.card-feed > div.content > p:last-of-type')
        if p:
            p = p[0].strings
            content = '\n'.join([para.replace('\u200b', '').strip() for para in list(p)]).strip()
        else:
            content = None
        star = div.select('ul > li > a > button > span.woo-like-count')
        if star:
            star = list(star[0].strings)[0]
        else:
            star = None
        lst.append((mid, content, star, time))
    df = pd.DataFrame(lst, columns=['mid', 'content', 'star', 'time'])
    return df


def get_the_list(q, p):
    df_list = []
    for i in range(1, p + 1):
        response = get_the_list_response(q=q, p=i)
        if response.status_code == 200:
            df = parse_the_list(response.text)
            df_list.append(df)
            print(f'第{i}页解析成功！', flush=True)

    return df_list


if __name__ == '__main__':
    # 先设置cookie，换成自己的；
    q = '#你的名字#'
    p = 20
    df_list = get_the_list(q, p)
    df = pd.concat(df_list)
    df.to_csv(f'{q}.csv', index=False, encoding='utf_8_sig')
