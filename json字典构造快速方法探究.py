import requests
import re
import time
url = "https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAA-M6jFNRwiUa72YLWcnMJT_BoIdP8Vf1SZIfm-YrV-08&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7307940414392387084&msToken=tMiGohEMwsR5851tcP9tG-ORYL9voS-6ZZ-5s-1WUgUsWGhaaZb_SxmcIPeBRVR0w3zDt9CTa2jcMiFLPA117kpRyngoFqla0XcwzLV43ugLUjxv1biBD4aKq4_mvbw=&X-Bogus=DFSzswVO5RvANcd9tim3z/D4OFIh"
my_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}
mycookie1="passport_csrf_token=ee9d9c9972d1f65b1230289745b1ef27; passport_csrf_token_default=ee9d9c9972d1f65b1230289745b1ef27; s_v_web_id=verify_lpnwlr2m_cxWnmD1y_YgpU_4p0h_Aq5K_nxTXYJMu7CEt; bd_ticket_guard_client_web_domain=2; MONITOR_WEB_ID=3218aa7d-68da-4824-a1a1-7150729bb537; ttwid=1%7CldCU8QnWijKXtBf45_sFfbetH1I5dNEjWttZrSwnppE%7C1704780594%7C99390f956dde76a868811ab51b9f86f15be776e2623aa8c85d7ad84cc36a5fcc; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; architecture=amd64; dy_swidth=1280; dy_sheight=720; csrf_session_id=0a210e3c4eac5964c5cf9ae4a93ea1d4; strategyABtestKey=%221705985315.431%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.977%7D; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; download_guide=%221%2F20240123%2F0%22; passport_assist_user=CjzfeioaI7kJX-_UKGTBu_2_k07FCGsc7wamVCFX612GBqixZl00dIoMKT3IQdZDyZ08Hn1oaRs6UaVYPNMaSgo8rDG02me-BWk-5PsUnnR0KFGV5K3tZsVwSEf43Jj69twp14qC_hLlPLrgAX07oSB69kf0nFjhjiZJ-sj9EPW0xw0Yia_WVCABIgEDjsYmGw%3D%3D; n_mh=fi9IriIEgxeLgqnH5yLY8vaM0QT7-KyqDHaUSPlVzVg; sso_uid_tt=fdc792cdc3dbfd6ed2670e859a9c39e2; sso_uid_tt_ss=fdc792cdc3dbfd6ed2670e859a9c39e2; toutiao_sso_user=b31b3a8fccde5bfcc33da27b667b9513; toutiao_sso_user_ss=b31b3a8fccde5bfcc33da27b667b9513; sid_ucp_sso_v1=1.0.0-KGM2YjBhNDE5NDNlY2UyNzY0NWJjOGI2NTllZDA5ZTJiYTAyYTcxYmYKHQjGnr3vowIQpou9rQYY7zEgDDDUjIXRBTgGQPQHGgJscSIgYjMxYjNhOGZjY2RlNWJmY2MzM2RhMjdiNjY3Yjk1MTM; ssid_ucp_sso_v1=1.0.0-KGM2YjBhNDE5NDNlY2UyNzY0NWJjOGI2NTllZDA5ZTJiYTAyYTcxYmYKHQjGnr3vowIQpou9rQYY7zEgDDDUjIXRBTgGQPQHGgJscSIgYjMxYjNhOGZjY2RlNWJmY2MzM2RhMjdiNjY3Yjk1MTM; passport_auth_status=d91d144fa849da9d816b484303444976%2C; passport_auth_status_ss=d91d144fa849da9d816b484303444976%2C; uid_tt=a28f4a03e1ca885c4b93b49e4e1ccbbc; uid_tt_ss=a28f4a03e1ca885c4b93b49e4e1ccbbc; sid_tt=301163c7aded4c9c33337ca7c8d801fa; sessionid=301163c7aded4c9c33337ca7c8d801fa; sessionid_ss=301163c7aded4c9c33337ca7c8d801fa; LOGIN_STATUS=1; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=9a95360c3af5320f4c37fbb2914ff1e7; __security_server_data_status=1; my_rd=2; store-region=cn-ha; store-region-src=uid; d_ticket=048fcbd308c97e734ade35139898b4a15b74f; sid_guard=301163c7aded4c9c33337ca7c8d801fa%7C1705985484%7C5183966%7CSat%2C+23-Mar-2024+04%3A50%3A50+GMT; sid_ucp_v1=1.0.0-KDg0Y2MwNjBhMzE5OTVjODE4YTIzZDZkMjMyZWVjZDMxNTY1ZThkMDIKGQjGnr3vowIQzIu9rQYY7zEgDDgGQPQHSAQaAmxxIiAzMDExNjNjN2FkZWQ0YzljMzMzMzdjYTdjOGQ4MDFmYQ; ssid_ucp_v1=1.0.0-KDg0Y2MwNjBhMzE5OTVjODE4YTIzZDZkMjMyZWVjZDMxNTY1ZThkMDIKGQjGnr3vowIQzIu9rQYY7zEgDDgGQPQHSAQaAmxxIiAzMDExNjNjN2FkZWQ0YzljMzMzMzdjYTdjOGQ4MDFmYQ; xg_device_score=7.658235294117647; publish_badge_show_info=%221%2C0%2C0%2C1705985778350%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1280%2C%5C%22screen_height%5C%22%3A720%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAA-M6jFNRwiUa72YLWcnMJT_BoIdP8Vf1SZIfm-YrV-08%2F1706025600000%2F0%2F0%2F1705989322034%22; __ac_nonce=065af578100471a6beb01; __ac_signature=_02B4Z6wo00f01UoCTggAAIDBvGtHL0tyrclKIkqAADczClEfB6D7pMccq.NmWDVbJ809y1VdCU9jKMMj6hAW7QJYDHFsD0XzeMQMJwY-aXpx3LeDJ.sLXJMN.Ph8rRE.g-s5es6DIQsytSYK42; odin_tt=87e6494f2187f12bcee09b4ed843419fde6ec06adb21c81698a7d8f82f3cfd84b9cb9c0a3650fe536d739647006ec405; tt_scid=lbjd9dHhsPLKz4PhSe-wmmyk9wDMT9daeRbVo9D6Fo24n4njx.yo5vyMq6gWv5dHfc17; msToken=lxGRaEmHdsaBdrVqeov7ivHLenDju2yxrZcbRz6HVMPlUwTphD9NHJb7ZAHP-OmVC0J_Lu50O9POB_hHvlieOJW3y_QGacTS6nlfMOvbATbi20Eu2s3Qrw==; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRnI2WjBjNVVWbzE0QithYnFVbnJ2S1NVNHNLQ2hkemMrQy9Ucno3NG4wUEZYNXNrK1pSN1JkcC9oNDRkZTNjeDVHUVljV1cwQkgxWHZpc1JpbS9XaFk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA-M6jFNRwiUa72YLWcnMJT_BoIdP8Vf1SZIfm-YrV-08%2F1706025600000%2F0%2F0%2F1705990706392%22; msToken=tMiGohEMwsR5851tcP9tG-ORYL9voS-6ZZ-5s-1WUgUsWGhaaZb_SxmcIPeBRVR0w3zDt9CTa2jcMiFLPA117kpRyngoFqla0XcwzLV43ugLUjxv1biBD4aKq4_mvbw=; passport_fe_beating_status=true;"
#转成json格式，使用正则
def TurnJson(mycookie):
      res=re.split('([^=]+)=([^;]+);?\s*',mycookie)
      [res.remove(i) for i in res if i=='']
      even_list = [res[i] for i in range(0, len(res)) if i % 2 == 0]
      odd_list = [res[i] for i in range(0, len(res)) if i % 2 == 1]
      dic = dict(zip(even_list,odd_list))
      print(dic)
    # for i in res:
    #     if i=='':
    #         res.remove(i)
    #     else:
    #         print('没问题，开始构造json字典')
    #         even_list = [res[i] for i in range(0, len(res)) if i % 2 == 0]
    #         odd_list = [res[i] for i in range(0, len(res)) if i % 2 == 1]
    #         dic = dict(zip(even_list,odd_list))
    # print(dic)
my_time=[]
for i in range(0,100):
    start=time.time()
    TurnJson(mycookie1)
    end=time.time()
    mid=end-start
    my_time.append(mid)
print('我的执行时间记录',my_time)
#方法2：直接构造
#错误写法如下
# dict = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in mycookie1.split('; ')}
#正确写法

your_time=[]
for i in range(0,100):
    start=time.time()
    cookie_dict = {item.split("=")[0]: item.split("=")[1] for item in mycookie1.split(";") if "=" in item}
    end=time.time()
    mid=end-start
    your_time.append(mid)
print('你的执行时间记录',your_time)

count=[]
countor=0
countor2=0
for i in range(0,len(my_time)):
    if my_time[i]<=your_time[i]:
        count.append('我快')
        countor+=1
    else:
        count.append('我不快')
        countor2+=1
print('比你快的次数',countor)
print('比你慢的次数',countor2)




# my_cookie={
# "passport_csrf_token":"ee9d9c9972d1f65b1230289745b1ef27",
# "passport_csrf_token_default":"ee9d9c9972d1f65b1230289745b1ef27"}
# res = requests.get(url,headers=my_headers)
# # res = requests.post(url)
#
# print(res.content)  # res.text:文本数据

# 文件写操作
# with open("1.mp4", "wb") as f:  # w：写文本 wb写字节
#     f.write(res.content)
