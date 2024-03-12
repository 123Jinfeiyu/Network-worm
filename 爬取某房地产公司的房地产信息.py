import csv
import time
from lxml import etree
import requests
def get_html(url, header):
    try:
        rep = requests.get(url, headers=header, timeout=6)
        rep.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    return rep.text
def send_request(pages, url, header):
    # Loop through each page
    for page in range(1, pages + 1):
        time.sleep(2)
        info_url = f'{url}pg{page}'
        print(info_url)
        try:
            info_html = get_html(info_url, header)

            if not info_html:
                continue
            html = etree.HTML(info_html)
            房源地址 = html.xpath('//ul[@class="resblock-list-wrapper"]/li')
            print(len(房源地址))

            for li in 房源地址:
                address_div = li.xpath('.//div[@class="resblock-desc-wrapper"]/a[@class="resblock-location"]/text()')
                address_name = li.xpath('.//div[@class="resblock-desc-wrapper"]/div[@class="resblock-name"]/a/text()')
                house_type = li.xpath('.//div[@class="resblock-desc-wrapper"]/div[@class="resblock-tag"]/span/text()')
                house_area = li.xpath('.//div[@class="resblock-desc-wrapper"]/a[@class="resblock-room"]/span[@class="area"]/text()')
                price = li.xpath('.//div[@class="resblock-desc-wrapper"]/div[@class="resblock-price"]/div[@class="second"]/text()')

                # Clean text
                cleaned_text_address_div = [text.strip() for text in address_div if text.strip() != '']
                split_and_join_house_type = ['|'.join(house_type[i:i + 4]) for i in range(0, len(house_type), 4)]

                # Write to CSV
                with open('data.csv', 'a', newline='', encoding='utf-8') as csv_file:
                    writer = csv.writer(csv_file)
                    if csv_file.tell() == 0:
                        writer.writerow(['房源标题', '房源地址', '户型', '面积', '价格'])
                    writer.writerow([address_name[0] if address_name else '',
                                     cleaned_text_address_div[0] if cleaned_text_address_div else '',
                                     split_and_join_house_type[0] if split_and_join_house_type else '',
                                     house_area[0] if house_area else '',
                                     price[0] if price else ''])

                print("数据已追加保存到 data.csv 文件。")

        except Exception as e:
            print(f"Error processing {info_url}: {e}")
            continue

if __name__ == '__main__':
    header = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "text/plain;charset=UTF-8",
        "Cookie": "ab_jid=f43baa40903f2d167bb962376ec3c7d05bc7; ab_jid_BFESS=f43baa40903f2d167bb962376ec3c7d05bc7; BAIDUID_BFESS=DAAB8224336F56734F4FD1E52110802C:FG=1; ZFY=mi5K2hgNTZ5hH4fv:A:A0SpNq8:AAemtrOICgqyE8VTRd4:C; ab_bid=bd0cbba992f835deb3eb40444cd845387fed; ab_sr=1.0.1_ZTMwY2ZmZTFlODdiMzRlYzAyYmE1NTkzNGVhYWJmNmRiOTlhODljYTI1MWM2MjQ1N2Q5YTRiMTdjODJiNWQwMDkyNDI1Zjk5MTg5MjJjYWE3Mjc0MjM4NDZkY2UzNWYzM2MyOTIyNGU0ZDVmZTA2YTU5NTRjYzY4MWNkYzg5YTk5ODBkZTIyNmFmNWEyOWUyNzIwNTdlODQ0OGM4ODk5Nw==",
        "Origin": "https://ny.fang.ke.com",
        "Referer": "https://ny.fang.ke.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
        "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Microsoft Edge\";v=\"122\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "cookie": "ab_jid=f43baa40903f2d167bb962376ec3c7d05bc7; ab_jid_BFESS=f43baa40903f2d167bb962376ec3c7d05bc7; BAIDUID_BFESS=DAAB8224336F56734F4FD1E52110802C:FG=1; ZFY=mi5K2hgNTZ5hH4fv:A:A0SpNq8:AAemtrOICgqyE8VTRd4:C; ab_bid=bd0cbba992f835deb3eb40444cd845387fed; ab_sr=1.0.1_ZTMwY2ZmZTFlODdiMzRlYzAyYmE1NTkzNGVhYWJmNmRiOTlhODljYTI1MWM2MjQ1N2Q5YTRiMTdjODJiNWQwMDkyNDI1Zjk5MTg5MjJjYWE3Mjc0MjM4NDZkY2UzNWYzM2MyOTIyNGU0ZDVmZTA2YTU5NTRjYzY4MWNkYzg5YTk5ODBkZTIyNmFmNWEyOWUyNzIwNTdlODQ0OGM4ODk5Nw=="
    }
    send_request(27, 'https://ny.fang.ke.com/loupan/rs/', header)
