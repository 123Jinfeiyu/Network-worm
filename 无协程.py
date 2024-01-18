import os
import time
from tqdm import tqdm
import requests
import re

base_url = 'https://vod6.bdzybf7.com'
#  定义要携带的请求头
headers = {
    'User-Agent': 'Mozilla/5.0  (Linux;  Android  6.0;  Nexus  5  Build/MRA58N)  AppleWebKit/537.36  (KHTML,  like  Gecko)  Chrome/120.0.0.0  Mobile  Safari/537.36  Edg/120.0.0.0',
}


def download_ts_files(url, start=0):
    size=0
    #  create  a  directory  named  "ts"  if  it  doesn't  exist
    if not os.path.exists("ts"):
        os.makedirs("ts")

    for i in range(start, len(url)):
        file_url = url[i]
        file_name = f"ts/{i}.ts"

        #  Check  if  the  file  already  exists,  if  it  does,  skip  downloading
        if os.path.exists(file_name):
            print(f"File  {file_name}  already  exists,  skipping...")
        else:
            #  Download  file  using  requests  library
            print(f"Downloading  file:  {file_url}")

            try:
                response = requests.get(file_url, headers=headers,stream=True)
                chunk_size=1024
                content_size = int(response.headers['Content-Length'])
                print(content_size)
                response.raise_for_status()  # Raise  exception  if  the  request  was  not  successful
                print('[文件大小]:%0.2f MB'%(content_size/chunk_size/1024))
            except requests.exceptions.RequestException as e:
                # 打印出异常信息
                print(e)
                # 返回 None 表示请求失败
                return None
            #  Save  file  to  local  directory
            with  open(file_name, 'wb') as file:
                for data in response.iter_content(chunk_size=chunk_size):
                      file.write(data)
                      size+=len(data)
                      print('\r'+'[下载进度]:%s%.2f%%'%('>'*int(size*50/content_size),float(size/content_size*100)),end='')

def getConnectUrl(filename):
    with  open(filename, 'r') as file:
        content = file.read()
        pattern = r'/\d+/\w+/\d+kb/hls/\w+\.ts'
        url = re.findall(pattern, content)
        if url:
            return url
        else:
            return 'Sorry,  no  match  found'
    return content


file_url = getConnectUrl('ts.m3u8')

con_list = []
for i in range(0, len(file_url)):
    connect_url = base_url + file_url[i]
    con_list.append(connect_url)

#  If  you  want  to  implement  a  pause  and  resume  functionality,  you  can  keep  track  of  the  index  where  the  download  was  interrupted
last_index = 0  # Replace  0  with  the  index  where  the  previous  download  was  interrupted
start = time.time()
download_ts_files(con_list, start=last_index)
end = time.time()
finished = end - start
print('Execution  time  without  coroutines:', finished)