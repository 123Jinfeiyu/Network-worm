import requests

while 1:
    word = input("翻译单词：")
    url = "https://aidemo.youdao.com/trans"
    my_data = {
        "q": word,
        "from": "Auto",
        "to": "Auto",
    }
    my_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }

    res = requests.post(url, headers=my_headers, data=my_data)
    print(res.json().get("translation")[0])