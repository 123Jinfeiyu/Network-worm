import threading

num = 0


def task1(number):
    global num  # 声明全局num变量

    for i in range(number):  #
        # mutex.acquire()
        mutex.acquire()  # 上锁
        num += 1  # 1000
        # mutex.release()  # 解锁
        mutex.release()  # 解锁
    print(f'task1-------num={num}')


def task2(number):
    global num  # 声明全局num变量

    for i in range(number):  #
        mutex.acquire()  # 上锁
        num += 1  # 2000

        mutex.release()  # 解锁
    print(f'task2-------num={num}')  # 101


if __name__ == '__main__':
    # 创建一把锁 必须上了一把锁，必须解一把锁
    mutex = threading.Lock()  # 实例化了锁对象
    # 线程之间的传参, 数据类型必须是元组
    t1 = threading.Thread(target=task1, args=(1000,))
    t2 = threading.Thread(target=task2, args=(1000,))

    t1.start()
    t2.start()

    print(f'main------{num}')

'''
线程之间的资源可以共享的
num = num + 1 不让切换到其他线程
上锁
解锁
20:53上课
'''
