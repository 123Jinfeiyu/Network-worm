lst = [{'domain': '.user.qzone.qq.com', 'expiry': 1711888177, 'httpOnly': False, 'name': 'qz_screen', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1920x1080'}, {'domain': '.qzone.qq.com', 'expiry': 1709308800, 'httpOnly': False, 'name': 'Loading', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'Yes'}, {'domain': '.qzone.qq.com', 'httpOnly': False, 'name': 'p_skey', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '8N84IlG96oLZuMcZtV-PNHhUdpe0FKMbyIx8DQ*UXBI_'}, {'domain': '.qzone.qq.com', 'httpOnly': False, 'name': 'pt4_token', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'hovMUKuJR46jrpkcjdh02rNjf0qFgTpbNBE0lQmK5DA_'}, {'domain': '.qzone.qq.com', 'httpOnly': False, 'name': 'p_uin', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'o3561774713'}, {'domain': '.qq.com', 'httpOnly': False, 'name': '_qpsvr_localtk', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '0.6208639806534602'}, {'domain': '.qq.com', 'expiry': 1743856175, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '4e1de6048e72c5088117424b5854f1d87008910e0a4488e1b1c0684eb4667714'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'uin', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'o3561774713'}, {'domain': '.qq.com', 'expiry': 1743856175, 'httpOnly': False, 'name': 'RK', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1vU1ELvz+X'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'skey', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '@wpRtJFuV0'}]
# 获取的cookie 获取name值 value值
'''
qz_screen=1920x1080; Loading=Yes
每一组字典当中的name值和value取出，拼接
1. 把每一组字典当中name值，value取值
'''
li = []
for cookie in lst:
    # print(cookie)
    name = cookie.get('name')
    value = cookie.get('value')
    li.append(name+'='+value)
cookies = '; '.join(li)
print(cookies)