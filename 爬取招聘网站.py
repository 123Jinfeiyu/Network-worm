import csv
from collections import defaultdict
from itertools import groupby

import requests
from jsonpath import jsonpath

url='https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job'
headers= {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8;",
        "Cookie": "inited_user=7201bf4be6900fcb9a1f13198c0380b4; acw_tc=ac11000117066209743503008e5e44b7a3cbc1a680317e3ea9d9404dabe03f; XSRF-TOKEN=AlhjXKkgRzGIGCq_6MNMdg; __gc_id=39bc5497b96c4712ba25dd1364ecc991; _ga=GA1.1.1051223600.1706620977; __uuid=1706620977691.05; __tlog=1706620977835.06%7C00000000%7C00000000%7C00000000%7C00000000; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1706620978; UniqueKey=ed7e741c54a9028941344312b1f2ca2b; liepin_login_valid=0; lt_auth=6egIbyYGzVr8snKIjzdf4ahE246pBWTP9XgKgxkFi4XvWKDm4P%2FnRA6BrbUC%2BioIqxN9I%2FQzMLf%2BM%2B78yHND60YR%2BFGkk565t%2FPr1XsKHOFhLf%2Bk1%2Fz0m8zYFJZxlyoDwSBk9C0Rkx31sy0yW5fT2WP1t5nX342my%2FP0iCyWqBg8; access_system=C; user_roles=0; need_bind_tel=false; new_user=true; c_flag=9929dc235827e736946115ac12ebbb8a; hpo_role-sec_project=sec_project_liepin; hpo_sec_tenant=0; user_photo=5f8fa3a78dbe6273dcf85e2608u.png; user_name=%E9%9D%B3%E9%A3%9E%E5%AE%87; inited_user=7201bf4be6900fcb9a1f13198c0380b4; imId=5f4e94079062ddb4e85047fcbbd6575d; imId_0=5f4e94079062ddb4e85047fcbbd6575d; imClientId=5f4e94079062ddb4f119516a6d573454; imClientId_0=5f4e94079062ddb4f119516a6d573454; imApp_0=1; __session_seq=13; __uv_seq=13; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1706621369; fe_im_socketSequence_new_0=9_8_8; __tlg_event_seq=215; fe_im_opened_pages=; fe_im_connectJson_0=%7B%220_ed7e741c54a9028941344312b1f2ca2b%22%3A%7B%22socketConnect%22%3A%222%22%2C%22connectDomain%22%3A%22liepin.com%22%7D%7D; _ga_54YTJKWN86=GS1.1.1706620977.1.1.1706621570.0.0.0",
        "Origin": "https://www.liepin.com",
        "Referer": "https://www.liepin.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "X-Client-Type": "web",
        "X-Fscp-Bi-Stat": "{\"location\": \"https://www.liepin.com/zhaopin/?city=410&dq=410&pubTime=&currentPage=0&pageSize=40&key=python&suggestTag=&workYearCode=&compId=&compName=&compTag=&industry=&salary=&jobKind=&compScale=&compKind=&compStage=&eduLevel=&otherCity=&sfrom=search_job_pc&ckId=hwmufbahh4eacxrzevqwbxwfh36ui9d9&scene=input&skId=hwmufbahh4eacxrzevqwbxwfh36ui9d9&fkId=hwmufbahh4eacxrzevqwbxwfh36ui9d9&suggestId=\"}",
        "X-Fscp-Fe-Version": "",
        "X-Fscp-Std-Info": "{\"client_id\": \"40108\"}",
        "X-Fscp-Trace-Id": "264cd22b-6f0f-40da-b699-c7fd37f59b25",
        "X-Fscp-Version": "1.1",
        "X-Requested-With": "XMLHttpRequest",
        "X-XSRF-TOKEN": "AlhjXKkgRzGIGCq_6MNMdg",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
cookie={
        "inited_user": "7201bf4be6900fcb9a1f13198c0380b4",
        "acw_tc": "ac11000117066209743503008e5e44b7a3cbc1a680317e3ea9d9404dabe03f",
        "XSRF-TOKEN": "AlhjXKkgRzGIGCq_6MNMdg",
        "__gc_id": "39bc5497b96c4712ba25dd1364ecc991",
        "_ga": "GA1.1.1051223600.1706620977",
        "__uuid": "1706620977691.05",
        "__tlog": "1706620977835.06%7C00000000%7C00000000%7C00000000%7C00000000",
        "Hm_lvt_a2647413544f5a04f00da7eee0d5e200": "1706620978",
        "UniqueKey": "ed7e741c54a9028941344312b1f2ca2b",
        "liepin_login_valid": "0",
        "lt_auth": "6egIbyYGzVr8snKIjzdf4ahE246pBWTP9XgKgxkFi4XvWKDm4P%2FnRA6BrbUC%2BioIqxN9I%2FQzMLf%2BM%2B78yHND60YR%2BFGkk565t%2FPr1XsKHOFhLf%2Bk1%2Fz0m8zYFJZxlyoDwSBk9C0Rkx31sy0yW5fT2WP1t5nX342my%2FP0iCyWqBg8",
        "access_system": "C",
        "user_roles": "0",
        "need_bind_tel": "false",
        "new_user": "true",
        "c_flag": "9929dc235827e736946115ac12ebbb8a",
        "hpo_role-sec_project": "sec_project_liepin",
        "hpo_sec_tenant": "0",
        "user_photo": "5f8fa3a78dbe6273dcf85e2608u.png",
        "user_name": "%E9%9D%B3%E9%A3%9E%E5%AE%87",
        "imId": "5f4e94079062ddb4e85047fcbbd6575d",
        "imId_0": "5f4e94079062ddb4e85047fcbbd6575d",
        "imClientId": "5f4e94079062ddb4f119516a6d573454",
        "imClientId_0": "5f4e94079062ddb4f119516a6d573454",
        "imApp_0": "1",
        "__session_seq": "13",
        "__uv_seq": "13",
        "Hm_lpvt_a2647413544f5a04f00da7eee0d5e200": "1706621369",
        "fe_im_socketSequence_new_0": "9_8_8",
        "__tlg_event_seq": "215",
        "fe_im_opened_pages": "",
        "fe_im_connectJson_0": "%7B%220_ed7e741c54a9028941344312b1f2ca2b%22%3A%7B%22socketConnect%22%3A%222%22%2C%22connectDomain%22%3A%22liepin.com%22%7D%7D",
        "_ga_54YTJKWN86": "GS1.1.1706620977.1.1.1706621570.0.0.0"
    }
data={
        "data": {
            "mainSearchPcConditionForm": {
                "city": "410",
                "dq": "410",
                "pubTime": "",
                "currentPage": "0",
                "pageSize": 40,
                "key": "python",
                "suggestTag": "",
                "workYearCode": "",
                "compId": "",
                "compName": "",
                "compTag": "",
                "industry": "",
                "salary": "",
                "jobKind": "",
                "compScale": "",
                "compKind": "",
                "compStage": "",
                "eduLevel": ""
            },
            "passThroughForm": {
                "scene": "input",
                "skId": "hwmufbahh4eacxrzevqwbxwfh36ui9d9",
                "fkId": "hwmufbahh4eacxrzevqwbxwfh36ui9d9",
                "ckId": "t9jutdho4guj1vrbdu71yajkh42jx5ra",
            }


        },
    "compressed": True,
}
#发送post请求数据
r=requests.post(headers=headers,url=url,json=data,cookies=cookie)
# print(r.text)
#转json字典
dict=r.json()
empty_list1=[]
empty_list2=[]
empty_list3=[]
#jsonpath提取,循环下整一群
for i in range(0,len(jsonpath(dict,'$..jobCardList')[0])-1):
    ret_child_dict=jsonpath(dict,'$..jobCardList')[0][i]
    compName=jsonpath(ret_child_dict,'$..compName')
    salary=jsonpath(ret_child_dict,'$..salary')
    title=jsonpath(ret_child_dict,'$..title')
    #两次循环就可以了
    for index, value in enumerate(compName):
        # index 索引  value值
        # print(value, compName[index])
        empty_list1.append(compName[index])
    for index, value in enumerate(salary):
        # index 索引  value值
        # print(value, salary[index])
        empty_list2.append(salary[index])
    for index, value in enumerate(title):
        # index 索引  value值
        # print(value, title[index])
        empty_list3.append(title[index])
# print(empty_list1,empty_list2,empty_list3)
# 设置表头
head = ['公司名','薪资','职位名称']
# head = ('公司名','薪资','职位名称')
name_pre=[]
salary_pre=[]
compName_pre=[]
for i in range(0,len(empty_list1)-1):
          name_pre.append('公司名')
for i in range(0,len(empty_list2)-1):
          salary_pre.append('薪资')
for i in range(0,len(empty_list3)-1):
          compName_pre.append('职位名称')
#快乐列表'公司名',
d1=[i for i in empty_list1]
dic1 = zip(name_pre, d1)
Final_dict1 = {'公司名': d1}
del dict,headers,cookie,data
Final_list2=list(dic1)
print(Final_list2)
#{'公司名': '某专业技术服务公司'}
print(Final_dict1)
# print(dict(Final_dict2))#只能转一个公司
#字典推导式
# 使用字典推导式将列表转为字典if key == '公司名'不要
# 使用 defaultdict 创建一个以公司名为键的字典
# company_dict = {}
#这种会覆盖剩余最后一个
# company_dict = {key: value for key, value in Final_list2}
# 创建一个字典，结构元组之后装下来
company_dict = {company[1]: company[0] for company in Final_list2}
print(company_dict)
# 将每个元组的值添加到对应公司名的列表中
# for key, value in Final_list2:
#     company_dict[key].append(value)

# 将 defaultdict 转为普通的字典,可以任意取的
# company_dict = dict(company_dict)
# company_dict = {key: values[1] for key, values in company_dict.items()}

#反之
# for key, value in Final_list2:
#     # print(key,value)
#     company_dict[key] = value
    # 创建一个字典
# data_dict = {}
# for key, value in data_list:
#     if key not in data_dict:
#         data_dict[key] = []
#     data_dict[key].append(value)
#
# print(data_dict)
# data_dict = {key: [value for k, v in Final_dict1 if k == key] for key, _ in Final_dict1}
# new={key: [item[1] for item in group] for key, group in groupby(sorted(Final_dict1, key=lambda x: x[0]), key=lambda x: x[0])}
# print(new)
d2=[i for i in empty_list2]
dic2 = zip(salary_pre, d2)
Final_list3=list(dic2)
company_dict1 = {company[1]: company[0] for company in Final_list3}
print(company_dict1)


d3=[i for i in empty_list3]
dic3 = zip(compName_pre, d3)
Final_list4=list(dic3)
company_dict2 = {company[1]: company[0] for company in Final_list4}
print(company_dict2)
# 保存数据
with open('douban.csv', 'w', encoding='utf-8-sig', newline='') as f:
    # 1. 创建csv对象
    write = csv.writer(f)  # f指的是文件对象
    # 2. 写入表头
    '''
    writerow: 写入一行
    writerows：写入多行
    '''
    # 2. 写入表头横着的
    # write.writerow(['公司名'] + d1)
    # write.writerow(['薪资'] + d2)
    # write.writerow(['职位名称'] + d3)
    # 3. 写入内容
    # write.writerows(zip(compName_pre, d2, d3))
    #竖着的
    write.writerow(head)
    #zip对象可以直接写入csv
    # write.writerows(zip(d1, d2, d3))
#not look good
    # write.writerows(company_dict)
    # write.writerows(company_dict1)
    # write.writerows(company_dict2)
    #字典也是可以解包的，会覆盖表头
    write.writerows(zip(company_dict,company_dict1,company_dict2))
    # write.wri    # write.writerow(company_dict2)terow(company_dict1)
    # 3. 写入内容
    # write.writerows(compName,salary,title)
'''
Permission denied: 'douban.csv': 文件是不是没有关闭
'''