import requests
import threading

cookies = {
    'ttwid': '1%7CvQ6QCiLyIG9SJypBIXRtIfGPJXv6br9a79NgmLfR-U4%7C1697436889%7C0ea69e384e5deb1dc65f4200190d8d2f33f9c4ca6c30e10208ee46af29a5015d',
    'xgplayer_user_id': '905282558930',
    'live_use_vvc': '%22false%22',
    'bd_ticket_guard_client_web_domain': '2',
    's_v_web_id': 'verify_lqb0qvhc_0iBmLw3t_sd2W_46Bf_9Mcf_68rowVA3IeLv',
    'passport_csrf_token': '200d4853a5fd758c92f83d148e5a6655',
    'passport_csrf_token_default': '200d4853a5fd758c92f83d148e5a6655',
    'n_mh': 'k9zkCfOQfFegoa7kc0V7SXvDVdHwnUROJ967U1dUUI0',
    '_bd_ticket_crypt_doamin': '2',
    '_bd_ticket_crypt_cookie': 'ee202c92a742381a4b3088235c965832',
    '__security_server_data_status': '1',
    'store-region': 'cn-bj',
    'store-region-src': 'uid',
    'LOGIN_STATUS': '0',
    'dy_swidth': '1728',
    'dy_sheight': '1117',
    'FORCE_LOGIN': '%7B%22videoConsumedRemainSeconds%22%3A180%7D',
    'volume_info': '%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.314%7D',
    'odin_tt': '20343b08ecb1611a4b04324c1a697f7e92e68e324e4606b2c80abadd3210987dc5b78518a2b0b6e221726782326016937e13203155c45a3b6a704d48ceb7e65e7f250011dbd98cd56711807de5cccdf0',
    'SEARCH_RESULT_LIST_TYPE': '%22single%22',
    'download_guide': '%223%2F20240122%2F0%22',
    'pwa2': '%220%7C0%7C3%7C0%22',
    'stream_player_status_params': '%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22',
    '__ac_nonce': '065afa15400ef3673f1ab',
    '__ac_signature': '_02B4Z6wo00f012jlk1gAAIDAOhqzQKoWZrdoxZfAAL-iqJci2ZpglkK6M7yKIwliOzfNMYPqrKO.vuP0wT0vQT7a2PJDE6YD4Ay8vsvJo0BaiNeB-WiQrnKtEPSVe3-wGkOxq1t1gYLod2Ro14',
    'csrf_session_id': 'b03ca9c6fb9b4ef4d85efd46128ba9de',
    'strategyABtestKey': '%221706008917.986%22',
    'bd_ticket_guard_client_data': 'eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQnNtWm5qUEJ6SExwVlpzZjhzV1BoYWlOQzJZM0ZNNk9iTnNoOGRQMzFmRFVtOVdDLzhXWHJ4NVFDTXZvTWZLdFNuMVlKU2ZvclVETmZ6SEkrUkF5MVE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D',
    'tt_scid': 'YGv8c2oqhsh25YyltzHqh1S9m0yykWythr.t-x6hPh8pknuFsZTspYcKKHrLRlFw371e',
    'IsDouyinActive': 'true',
    'stream_recommend_feed_params': '%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1728%2C%5C%22screen_height%5C%22%3A1117%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A10%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A150%7D%22',
    'home_can_add_dy_2_desktop': '%221%22',
    'msToken': '_vjXTFXg1qnycSDdQcVu4ao-RjLHYr360C_Mi5plElthGniJuBQhDGgbj25Ncskr8S-Vb3LYE6kHoUScjl01v1VOhDyBI_aqKpjtYhlA2lkmF63DpwtUy0s_P5B3DA==',
    'msToken': '4vtKfjALRZz-4wLsSKNCxUShqEfmp8_tiY55saliOmnGo4e_adJhsS5hSUSewB19It4MrqasbgcY75oIFaMgIGHv2-8lXKQx4whBno5G3oKX5N3J8d8HskZxLoebXA==',
}

headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'ttwid=1%7CvQ6QCiLyIG9SJypBIXRtIfGPJXv6br9a79NgmLfR-U4%7C1697436889%7C0ea69e384e5deb1dc65f4200190d8d2f33f9c4ca6c30e10208ee46af29a5015d; xgplayer_user_id=905282558930; live_use_vvc=%22false%22; bd_ticket_guard_client_web_domain=2; s_v_web_id=verify_lqb0qvhc_0iBmLw3t_sd2W_46Bf_9Mcf_68rowVA3IeLv; passport_csrf_token=200d4853a5fd758c92f83d148e5a6655; passport_csrf_token_default=200d4853a5fd758c92f83d148e5a6655; n_mh=k9zkCfOQfFegoa7kc0V7SXvDVdHwnUROJ967U1dUUI0; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=ee202c92a742381a4b3088235c965832; __security_server_data_status=1; store-region=cn-bj; store-region-src=uid; LOGIN_STATUS=0; dy_swidth=1728; dy_sheight=1117; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.314%7D; odin_tt=20343b08ecb1611a4b04324c1a697f7e92e68e324e4606b2c80abadd3210987dc5b78518a2b0b6e221726782326016937e13203155c45a3b6a704d48ceb7e65e7f250011dbd98cd56711807de5cccdf0; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20240122%2F0%22; pwa2=%220%7C0%7C3%7C0%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; __ac_nonce=065afa15400ef3673f1ab; __ac_signature=_02B4Z6wo00f012jlk1gAAIDAOhqzQKoWZrdoxZfAAL-iqJci2ZpglkK6M7yKIwliOzfNMYPqrKO.vuP0wT0vQT7a2PJDE6YD4Ay8vsvJo0BaiNeB-WiQrnKtEPSVe3-wGkOxq1t1gYLod2Ro14; csrf_session_id=b03ca9c6fb9b4ef4d85efd46128ba9de; strategyABtestKey=%221706008917.986%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQnNtWm5qUEJ6SExwVlpzZjhzV1BoYWlOQzJZM0ZNNk9iTnNoOGRQMzFmRFVtOVdDLzhXWHJ4NVFDTXZvTWZLdFNuMVlKU2ZvclVETmZ6SEkrUkF5MVE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; tt_scid=YGv8c2oqhsh25YyltzHqh1S9m0yykWythr.t-x6hPh8pknuFsZTspYcKKHrLRlFw371e; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1728%2C%5C%22screen_height%5C%22%3A1117%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A10%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A150%7D%22; home_can_add_dy_2_desktop=%221%22; msToken=_vjXTFXg1qnycSDdQcVu4ao-RjLHYr360C_Mi5plElthGniJuBQhDGgbj25Ncskr8S-Vb3LYE6kHoUScjl01v1VOhDyBI_aqKpjtYhlA2lkmF63DpwtUy0s_P5B3DA==; msToken=4vtKfjALRZz-4wLsSKNCxUShqEfmp8_tiY55saliOmnGo4e_adJhsS5hSUSewB19It4MrqasbgcY75oIFaMgIGHv2-8lXKQx4whBno5G3oKX5N3J8d8HskZxLoebXA==',
    'pragma': 'no-cache',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAA0HwZJN6-JDCSTjxiMk-czhyZWxes8XIDEjppFXExauK8-kQTLMEH9ZdfIXxnl9tS',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

# user_id = "MS4wLjABAAAAMbqnWxzUfZegt9vrNBDz7zyqwhvG6vXiKTDxVm2wUD0"
user_id = "MS4wLjABAAAA0HwZJN6-JDCSTjxiMk-czhyZWxes8XIDEjppFXExauK8-kQTLMEH9ZdfIXxnl9tS"
url = f'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id={user_id}&max_cursor=1671081109000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1728&screen_height=1117&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=150&webid=7290435875619390995&msToken=4vtKfjALRZz-4wLsSKNCxUShqEfmp8_tiY55saliOmnGo4e_adJhsS5hSUSewB19It4MrqasbgcY75oIFaMgIGHv2-8lXKQx4whBno5G3oKX5N3J8d8HskZxLoebXA==&X-Bogus=DFSzswVYPTiANVoktizN7jLNKBOg'

response = requests.get(
    url,
    cookies=cookies,
    headers=headers,
)

print(":::",response.text)

# aweme_list = response.json().get("aweme_list")
# print(aweme_list)

# url_list = [aweme.get("video").get("play_addr").get("url_list")[0] for aweme in aweme_list]
# print(url_list)

# def get_one_video(url, c):
#     res = requests.get(url)
#     # 文件写操作
#     with open(f"./videos/{c}.mp4", "wb") as f:  # w：写文本 wb写字节
#         f.write(res.content)
#     print(f"{c}.mp4下载成功！")
#
# c = 1
# t_list = []
# for url in url_list:
#     t = threading.Thread(target=get_one_video, args=(url, c))
#     t.start()
#     t_list.append(t)
#     c += 1
#
# for t in t_list:
#     t.join()
