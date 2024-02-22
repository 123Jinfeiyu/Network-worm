import threading
import time


def task1():
    for i in range(5):
        print(f'task1...{i}')


def task2():
    for i in range(5):
        print(f'task2----{i}')


if __name__ == '__main__':
    # 实例化了两次: 创建了两个子线程+主线程
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    # 启动线程
    t1.start()
    t2.start()

    # 打印线程数量（当前活动的线程数量)
    print(threading.enumerate())
