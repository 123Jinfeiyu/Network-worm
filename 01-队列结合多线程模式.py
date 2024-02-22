import threading
import time
from queue import Queue

num = 0
q = Queue(2)  # 队列大小存放两个数据
q.put(num)


def task1():
    for i in range(100):
        number = q.get()  # 从队列里面取出数据，赋值给number
        print(number, 'task1......................')
        number += 1
        q.put(number)


def task2():
    for i in range(100):
        number = q.get()  # 从队列里面取出数据，赋值给number
        print(number, 'task2......................')
        number += 1
        q.put(number)


if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
