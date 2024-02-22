import threading

num = 0


def task1(number):
    global num  # 声明全局num变量

    for i in range(number):  #
        mutex.acquire()
        mutex.acquire()  # 上锁
        num += 1  # 1000
        mutex.release()  # 解锁
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
    # 可重入锁
    mutex = threading.RLock()  # 实例化了锁对象
    # 线程之间的传参, 数据类型必须是元组
    t1 = threading.Thread(target=task1, args=(1000,))
    t2 = threading.Thread(target=task2, args=(1000,))

    t1.start()
    t2.start()

    print(f'main------{num}')

'''
lock：适用于锁的获取和释放可以明确配对的情况，每次获取后都需要是否，否则其他线程将无法获取锁
Rlock：适用于锁可能需要再同一线程中获取多次情况。比如递归。运行同一个线程多次获取锁。只有再获取次数和释放次数相等时才能
真正释放给其他线程
'''
