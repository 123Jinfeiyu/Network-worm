import requests

url = 'https://user.qzone.qq.com/3561774713'
# 添加反爬参数
head = {
    'Cookie': 'pgv_pvid=8207345324; eas_sid=L1B6m9b6f6P5T9V0k571C8F1N8; LW_uid=X13659Z6b6I5N9r0K5Z2g0Y083; RK=MmV9Ervot1; ptcz=ce05dac4641e6f2c8c2a3987f5be5a025f960dd0982395c023d8382556efeb2f; QZ_FE_WEBP_SUPPORT=1; __Q_w_s__QZN_TodoMsgCnt=1; fqm_pvqid=97f50048-3e68-4c23-a87f-f79980a2a9a7; LW_sid=b1l7Y0j3J7L6h4L5X8X0t3w2s9; _clck=5t1qei|1|fij|0; _qpsvr_localtk=0.8358527219139718; pgv_info=ssid=s8697964720; Loading=Yes; qz_screen=1920x1080; 3561774713_todaycount=0; 3561774713_totalcount=12; uin=o3561774713; skey=@fhtrIpKC0; p_uin=o3561774713; pt4_token=eShYvhBcvbrYHMQtLV5YkkZpq42pSYw9PtJcFppMjxM_; p_skey=vEaXP7Ic6vp1AGefws9VLxWLVt8ZC9RbHkT0JbUhjK4_; cpu_performance_v8=2',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 发请求，获取响应内容
res = requests.get(url, headers=head)

# 打印响应内容
print(res.text)


'''
pgv_pvid=8207345324; eas_sid=L1B6m9b6f6P5T9V0k571C8F1N8; LW_uid=X13659Z6b6I5N9r0K5Z2g0Y083; RK=MmV9Ervot1; ptcz=ce05dac4641e6f2c8c2a3987f5be5a025f960dd0982395c023d8382556efeb2f; QZ_FE_WEBP_SUPPORT=1; __Q_w_s__QZN_TodoMsgCnt=1; fqm_pvqid=97f50048-3e68-4c23-a87f-f79980a2a9a7; LW_sid=b1l7Y0j3J7L6h4L5X8X0t3w2s9; _clck=5t1qei|1|fij|0; _qpsvr_localtk=0.8358527219139718; pgv_info=ssid=s8697964720; Loading=Yes; qz_screen=1920x1080; 3561774713_todaycount=0; 3561774713_totalcount=12; uin=o3561774713; skey=@fhtrIpKC0; p_uin=o3561774713; pt4_token=eShYvhBcvbrYHMQtLV5YkkZpq42pSYw9PtJcFppMjxM_; p_skey=vEaXP7Ic6vp1AGefws9VLxWLVt8ZC9RbHkT0JbUhjK4_; cpu_performance_v8=2
dic = {"pgv_pvid":"8207345324", "eas_sid":"L1B6m9b6f6P5T9V0k571C8F1N8"}
split结合循环
'''