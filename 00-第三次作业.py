'''
目标url：https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job

响应数据类型：json

请求方式：post请求
'''
import requests

url = 'https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job'

# 请求头参数
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'X-Client-Type': 'web',
    'X-Fscp-Bi-Stat': '{"location": "https://www.liepin.com/zhaopin/?city=410&dq=410&pubTime=&currentPage=0&pageSize=40&key=python&suggestTag=&workYearCode=&compId=&compName=&compTag=&industry=&salary=&jobKind=&compScale=&compKind=&compStage=&eduLevel=&otherCity=&sfrom=search_job_pc&ckId=hwmufbahh4eacxrzevqwbxwfh36ui9d9&scene=input&skId=hwmufbahh4eacxrzevqwbxwfh36ui9d9&fkId=hwmufbahh4eacxrzevqwbxwfh36ui9d9&suggestId="}',
    'X-Fscp-Std-Info': '{"client_id": "40108"}',
    'X-Fscp-Trace-Id': '727dbd84-2e41-4961-a72b-7b06f89d06c2',
    'X-Fscp-Version': '1.1',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': '3MGW8kbOREatGn4-uw51yw',
}
lst = []
for page in range(0, 7):  # 0 1 2 就是三页数据
    data = {"data": {
        "mainSearchPcConditionForm": {"city": "410", "dq": "410", "pubTime": "", "currentPage": page, "pageSize": 40,
                                      "key": "python", "suggestTag": "", "workYearCode": "", "compId": "", "compName": "",
                                      "compTag": "", "industry": "", "salary": "", "jobKind": "", "compScale": "",
                                      "compKind": "", "compStage": "", "eduLevel": ""},
        "passThroughForm": {"scene": "input", "skId": "hwmufbahh4eacxrzevqwbxwfh36ui9d9",
                            "fkId": "hwmufbahh4eacxrzevqwbxwfh36ui9d9", "ckId": "uplvva1ixxc9vp696cc8sv3y684cfc8b",
                            }}}
    # 发请求，获取响应  ctrl+atl+L
    res = requests.post(url, json=data, headers=head)

    # 打印响应内容 "信息有误"普通的文本能调用json方法？
    '''
    确定url是正确的，代码没有问题——数据少了或者不正确(反爬了)
    '''
    result = res.json()  # 字典
    lsts = result['data']['data']['jobCardList']
    print(len(lsts))
    # 循环遍历每一组的职位信息
    for i in lsts:
        dic = {}
        dic['name'] = i['job']['title']
        dic['salary'] = i['job']['salary']
        dic['compName'] = i['comp']['compName']
        lst.append(dic)
    print(f'第{page+1}页数据爬取完毕---------------------------------------------')
print(lst)