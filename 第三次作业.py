import requests

url = 'https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job'

# 准备请求头参数
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Client-Type': 'web',
    'X-Fscp-Bi-Stat': '{"location": "https://www.liepin.com/zhaopin/?city=410&dq=410&pubTime=&currentPage=0&pageSize=40&key=python&suggestTag=&workYearCode=&compId=&compName=&compTag=&industry=&salary=&jobKind=&compScale=&compKind=&compStage=&eduLevel=&otherCity=&sfrom=search_job_pc&ckId=hwmufbahh4eacxrzevqwbxwfh36ui9d9&scene=input&skId=hwmufbahh4eacxrzevqwbxwfh36ui9d9&fkId=hwmufbahh4eacxrzevqwbxwfh36ui9d9&suggestId="}',
    'X-Fscp-Fe-Version': '',
    'X-Fscp-Std-Info': '{"client_id": "40108"}',
    'X-Fscp-Trace-Id': '9a4abef8-c7cb-47e7-bd5b-98dd7e4e1981',
    'X-Fscp-Version': '1.1',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'itDydOE2RRCP_eOf3RsQmA',
}
'''
currentPage 
第一页：0
第二页：1
第三页：2
'''
for page in range(0, 3):
    # 准备post请求参数
    data = {"data": {
        "mainSearchPcConditionForm": {"city": "410", "dq": "410", "pubTime": "", "currentPage": page, "pageSize": 40,
                                      "key": "python", "suggestTag": "", "workYearCode": "", "compId": "", "compName": "",
                                      "compTag": "", "industry": "", "salary": "", "jobKind": "", "compScale": "",
                                      "compKind": "", "compStage": "", "eduLevel": ""},
        "passThroughForm": {"scene": "input", "skId": "hwmufbahh4eacxrzevqwbxwfh36ui9d9",
                            "fkId": "hwmufbahh4eacxrzevqwbxwfh36ui9d9", "ckId": "3rhurrtyl2b5nhe9yf37w8vyyywbi389"}}}
    # 发请求，获取响应
    res = requests.post(url, headers=head, json=data)
    # 打印响应内容
    # print(res.text)
    result = res.json()  # 第一步
    job_list = result['data']['data']['jobCardList']  # [{},{},{}]
    for job in job_list:
        # print(job)
        # 公司名称
        compName = job['comp']['compName']
        # 薪水
        salary = job['job']['salary']
        # 职位
        work_name = job['job']['title']
        print(compName, salary, work_name)
    print(f'第{page+1}页爬取完毕！！！！！！！！！！！！！！！！！！！！！！！！')
