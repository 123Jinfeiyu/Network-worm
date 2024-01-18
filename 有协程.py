import os
import time
import requests
import re
import asyncio
import aiohttp
from tqdm import tqdm
base_url='https://vod6.bdzybf7.com'
# 定义要携带的请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 Edg/120.0.0.0',
}
last_index = 473
def download_ts_files(url,start=0):
    # create a directory named "ts" if it doesn't exist
    if not os.path.exists("ts1"):
        os.makedirs("ts1")
    for i in range(start, len(url)):
        file_url = url[i]
        file_name = f"ts1/{i}.ts"
        #  Check  if  the  file  already  exists,  if  it  does,  skip  downloading
        if os.path.exists(file_name):
            print(f"File  {file_name}  already  exists,  skipping...")
        else:
            #  Download  file  using  requests  library
            print(f"Downloading  file:  {file_url}")
        #  Download  file  using  requests  library
        print('过滤成功,开始发送请求')
        time.sleep(1.5)
        try:
            response = requests.get(file_url, headers=headers,stream=True)
            content_size=int(response.headers['Content-Length'])/1024
            response.raise_for_status()  # Raise  exception  if  the  request  was  not  successful
        except requests.exceptions.RequestException as e:
            # 打印出异常信息
            print(e)
            # 返回 None 表示请求失败
            return None
        last_index=i
        #  Save  file  to  local  directory
        with  open(file_name, 'wb') as file:
            for data in tqdm(iterable=response.iter_content(1024),
                total=content_size,
                unit='k',
                desc='视频下载'):
                file.write(data)

def getConnectUrl(filename):
    with open(filename,'r') as file:
        content=file.read()
        pattern = r'/\d+/\w+/\d+kb/hls/\w+\.ts'
        #返回的是一个列表
        url=re.findall(pattern,content)
        if url:
            return url
        else:
             return '对不起没找到'
    return content
    #返回的是一个列表
file_url=getConnectUrl('ts.m3u8')
# print(file_url)
con_list=[]
for i in range(0, len(file_url)):
    connect_url=base_url+file_url[i]
    # print(connect_url)
    con_list.append(connect_url)
#异步请求,加速下载,创建任务列表
tasks=[]
async def get_ts(url):
   async with await aiohttp.ClientSession() as sess:
       async with sess.get(url=url,headers=headers) as response:
            ts_data=await response.read()
            return ts_data
#最后的索引

for url in con_list:
            c=get_ts(url)
            task=asyncio.ensure_future(c)
            start = time.time()
            task.add_done_callback(download_ts_files(con_list,start=last_index))
            end = time.time()
            finished = end - start
            print('协程执行时间为', finished)
            tasks.append(task)
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))


# download_ts_files(con_list)
#  create  a  directory  named  "ts"  if  it  doesn't  exist


