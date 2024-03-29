import random
import csv
import requests
from lxml import etree
import re


def get_html(url):
    headers = {
        'Cookie': 'fspop=test; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=18de58ebd1dc8-0781367aca0121-26001b51-1fa400-18de58ebd1dc8; _lxsdk=18de58ebd1dc8-0781367aca0121-26001b51-1fa400-18de58ebd1dc8; _hc.v=e7591ef3-c496-282e-03be-46a7b2893610.1708953354; s_ViewType=10; WEBDFPID=0z3y2988u5865305y2wv1zxu850438yz81wv41vvz68979588uv40412-2024313365701-1708953365701OIAUWMWfd79fef3d01d5e9aadc18ccd4d0c95072764; cy=1699; cye=jiuzhaigou; ctu=7856a9354d2f042638dfcb2bef216c3ac514e40deeef1b46b6b125b7017afc5f; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1708953354,1708954981; qruuid=4a051dec-1f57-4582-b007-8efbd3e45050; dplet=af734946bfd30d54c8c65d98e993f923; dper=0202ca1e85836dfdb1645c2dc9fe8a74d927fc7899e438f1563c96a17e4230ca029e167081f129ae00c913032ee8f7a478b5c45d933c79f72ba200000000501e000081ee2a702bc802060900a233a47d6234b4a3c197420be44a6f2ca9a42962dad7cb727f690535f810a44336cb322c9076; ll=7fd06e815b796be3df069dec7836c3df; ua=%E4%BA%91%E8%85%BF%E7%83%A4%E5%92%96%E5%95%A1; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1708955341; _lxsdk_s=18de58ebd1e-6b5-984-be5%7C%7C1047',
        'Host': 'www.dianping.com',
        'Referer': 'https://www.dianping.com/search/keyword/344/0_%E7%81%AB%E9%94%85',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    }
    try:
        html = requests.get(url, headers=headers)
        html.encoding = html.apparent_encoding
        if html.status_code == '200':
            print('连接成功')
    except Exception as e:
        print('连接失败%s' % e)
    return html.text


# 获取信息
def get_comment(html):
    xp = etree.HTML(html)
    lis = xp.xpath('//*[@id="review-list"]/div[2]/div[3]/div[3]/div[2]/ul/li')
    for li in lis:
        try:
            # 用户昵称
            username = li.xpath('./div/div[1]/a/text()')[0].strip() \
                            .replace("\r\n", "，").replace("\n", "，").replace("\r", "，")
            # 用户类型
            usertype = "vip"
            try:
                usertype = li.xpath('./div/div[1]/span/@class')[0].strip() \
                            .replace("\r\n", "，").replace("\n", "，").replace("\r", "，")
            except:
                usertype = "普通用户"
            # 评分
            ss = li.xpath('./div/div[2]/span/@class')[0].strip() \
                            .replace("\r\n", "，").replace("\n", "，").replace("\r", "，")
            score = float("".join(re.findall(r'\d+', ss)))/10
            # 评论
            comment = li.xpath('./div/div[4]/text()')[0].strip() \
                            .replace("\r\n", "，").replace("\n", "，").replace("\r", "，")
            # 发布时间
            times = li.xpath('./div/div[6]/span[1]/text()')[0].strip() \
                            .replace("\r\n", "，").replace("\n", "，").replace("\r", "，")
            if '更新于' in times:
                times = times.split('更新于')[1]
            # 赞
            zan = 0
            # 收藏
            sc = 0
            thisdd = li.xpath('./div/div[6]/span[3]/*')
            if thisdd[1].tag=='em':
                zan = "".join(re.findall(r'\d+', thisdd[1].xpath('./text()')[0]))
            if thisdd[len(thisdd)-1].tag=='em':
                sc = "".join(re.findall(r'\d+', thisdd[len(thisdd)-1].xpath('./text()')[0]))
            print(username, usertype, score, zan, sc, times, comment)
            writer.writerow([username, usertype, score, zan, sc, times, comment])
        except Exception as e:
            continue


if __name__ == '__main__':
    file = open("jiuzhaigou.csv", "a", encoding="utf-8", newline="")
    writer = csv.writer(file)
    # 爬取信息
    for page in range(1, 11):
        BASE_URL = 'https://www.dianping.com/shop/l7i1vLDwzpc4d0jw/review_all/p{}'
        print('正在爬取第{}页信息'.format(str(page)))
        url = BASE_URL.format(str(page))
        html = get_html(url)
        get_comment(html)
    file.close()
    print('信息已保存到本地')
