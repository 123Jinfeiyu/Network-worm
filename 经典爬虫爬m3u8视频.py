import os
import asyncio
import aiohttp
import re
from tqdm import tqdm

base_url = 'https://vod6.bdzybf7.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 Edg/120.0.0.0',
}

async def download_ts_file(session, file_url, file_name, max_retries=5):
    retries = 0
    while retries < max_retries:
        if os.path.exists(file_name):
            print(f"File {file_name} already exists, skipping...")
            return
        try:
            async with session.get(file_url, headers=headers) as response:
                response.raise_for_status()
                with open(file_name, 'wb') as file:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        file.write(chunk)
                print(f"Downloaded {file_name}")
                return  # 成功下载后返回
        except aiohttp.ClientError as e:
            retries += 1
            print(f"Error downloading {file_name}: {e}. Retry {retries}/{max_retries}")
            await asyncio.sleep(2**retries)  # 指数退避策略


async def download_ts_files(url_list):
    if not os.path.exists("ts"):
        os.makedirs("ts")
    async with aiohttp.ClientSession() as session:
        tasks = [download_ts_file(session, url, f"ts/{i}.ts") for i, url in enumerate(url_list)]
        await asyncio.gather(*tasks)

def get_connect_url(filename):
    with open(filename, 'r') as file:
        content = file.read()
        pattern = r'/\d+/\w+/\d+kb/hls/\w+\.ts'
        url = re.findall(pattern, content)
        return [base_url + u for u in url] if url else []

async def main():
    file_url = get_connect_url('ts.m3u8')
    await download_ts_files(file_url)

# 运行异步主函数
loop = asyncio.get_event_loop()  # 获取当前事件循环
try:
    loop.run_until_complete(main())  # 运行主函数直到完成
finally:
    loop.close()  # 关闭事件循环

