import asyncio
import csv
import aiohttp
from lxml import etree


# 得到网页源码内容
async def get_html(session, url):
    '''
        使用aiohttp客户端会话异步获取网页的html内容
    '''
    async with session.get(url) as res:
        # 获取到网页源码了，才能返回
        return await res.text()


# 解析数据
async def parse_html(page):
    # 解析数据page
    tree = etree.HTML(page)
    # 通过xpath语法做解析 返回的数据类型是列表，
    divs = tree.xpath('//div[@class="info"]')
    # print(len(divs))  # 长度为25，这个页面的25部电影数据已拿到
    lst = []
    for div in divs:
        dic = {}
        # a//text(): 获取a标签下面的所有的文本内容
        title = div.xpath('./div[@class="hd"]/a//text()')
        # 电影名称
        dic["电影名称"] = ''.join(title).replace(' ', '').replace('\n', '')
        # 电影类型 [1, 2, 3] lst[-1]  strip(): 默认去除前后的空格
        dic["电影类型"] = div.xpath('./div[@class="bd"]/p/text()')[1].split('/')[-1].strip()
        # 电影评分
        dic["电影评分"] = div.xpath('./div[@class="bd"]/div[@class="star"]/span[2]/text()')[0]
        # 电影标语
        '''
        电影标语：有的有，有的是没有标语
        条件判断：如果有标语，正常取值，如果没有，赋值空字符串
        '''
        quote = div.xpath('./div[@class="bd"]/p[@class="quote"]/span/text()')
        if quote:
            dic["电影标语"] = quote[0]
        else:
            dic["电影标语"] = ''
        lst.append(dic)
    # 将列表返回出去
    return lst


# 主函数
async def main():
    '''
    主函数，用于执行整个异步任务的流程
    '''
    # 创建客户端会话
    async with aiohttp.ClientSession() as session:
        # 构造要抓取的页面url
        # 创建任务列表，
        tasks = []
        for page in range(1, 11):
            # 数据所在的url
            url = f'https://movie.douban.com/top250?start={(page - 1) * 25}&filter='
            # 将异步获取网页的任务添加到任务列表
            tasks.append(get_html(session, url))
        # 开始并发执行所有任务，等待任务完成
        '''
        并发的运行传递给gather的所有异步任务,
        await 等待所有的任务完成，并获取每个任务的结果
        '''
        pages = await asyncio.gather(*tasks)
        # print(pages)  # 列表里面存放的是网页源码
        movie_lst = []
        for page in pages:
            # 等待获取解析的数据
            movie = await parse_html(page)
            movie_lst.extend(movie)
        # 循环完成，10页的数据就获取完成
        save_data(movie_lst)


# 保存数据
def save_data(movie_lst):
    with open('豆瓣电影.csv', 'w', encoding='utf-8-sig', newline='') as f:
        write = csv.DictWriter(f, fieldnames=("电影名称", "电影类型", "电影评分", "电影标语"))
        # 写入表头
        write.writeheader()
        # 写入数据
        write.writerows(movie_lst)


if __name__ == '__main__':
    # 创建事件循环对象
    loop = asyncio.get_event_loop()
    # 执行异步任务
    loop.run_until_complete(main())

'''
requests库本身是同步的，不能直接再异步环境中使用，因为他会阻塞事件循环的执行
aiohttp 第三方库，pip install aiohttp
'''
