import time
import threading  # 内置模块，直接导入就可以使用了


# def sing():
#     for i in range(3):
#         print(f'在唱歌{i}')
#         time.sleep(1)  # 3
#
#
# def dance():
#     for i in range(3):
#         print(f'在跳舞{i}')
#         time.sleep(1)  # 3
#
#
# if __name__ == '__main__':
#     sing()
#     dance()


# 分配任务（定义了一个子线程）
def task():
    print("hello python")
    time.sleep(1)
    print("hello world")


if __name__ == '__main__':
    start = time.time()
    for i in range(5):
        # 通过主线程来调度子线程, 循环了五次，创建了5个子线程
        t = threading.Thread(target=task)  # 只填写对应的函数名，指定子线程执行哪一个函数
        # 线程开始进入到开始工作的状态，具体每个线程任务什么时候开始执行，取决于操作系统的调度和cpu
        t.start()
    end = time.time()
    print(end-start)
