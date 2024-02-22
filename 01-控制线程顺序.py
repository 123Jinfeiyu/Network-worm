import threading
import time


def download_data():
    print('开始下载数据。。。')
    time.sleep(1)  # 模拟数据下载
    print('数据下载完成。。。')


if __name__ == '__main__':
    lst = []
    for i in range(5):
        t = threading.Thread(target=download_data)
        # 开启子线程
        t.start()
        lst.append(t)
        # join(): 等待子线程结束，再往后执行代码
    for t in lst:
        t.join()  #
    '''必须等待数据下载完成才能进行数据处理'''
    print('开始数据处理。。。。。。。。。。。。')

    print('数据处理完成。。。。。。。。。。。。')
