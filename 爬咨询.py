import json
import requests
for i in range(1,8):
    url = 'http://www.whggzy.com/portal/category'

    cookies = {
        "_zcy_log_client_uuid": "df83bbc0-bce1-11ee-a622-e79dc8b88d3f",
        "acw_tc": "2f624a2717063466977785310e3282e1c73848b56eac5945b750e56ffc6027"
    }

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": "_zcy_log_client_uuid=df83bbc0-bce1-11ee-a622-e79dc8b88d3f; acw_tc=2f624a2717063466977785310e3282e1c73848b56eac5945b750e56ffc6027",
        "Origin": "http://www.whggzy.com",
        "Referer": "http://www.whggzy.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "X-Requested-With": "XMLHttpRequest"
    }

    payload = {
        "pageNo": i,
        "pageSize": 15,
        "categoryCode": "GovernmentProcurement",
        # "_t": 1706352392000
    }

    try:
        res = requests.post(url, json=payload, headers=headers, cookies=cookies)
        res.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        # Parse the JSON response
        response_dict = json.loads(res.text)
        # Extract titles
        titles = [item["title"] for item in response_dict["result"]["data"]["data"]]
        for title in titles:
            with open('政策法规.txt', 'a', encoding='utf-8') as f:
                f.write(title+'\n')


    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
