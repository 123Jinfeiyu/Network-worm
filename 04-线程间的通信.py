import threading

num = 100


def task1():
    global num  # 声明全局num变量
    num = num + 100
    print(f'task1-------num={num}')


def task2():
    print(f'task2-------num={num}')  # 101


if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()

    print(f'main------{num}')

'''
线程之间的资源可以共享的
'''