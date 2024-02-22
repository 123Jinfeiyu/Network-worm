import threading
import time


# 普通的类具备线程的特性（继承线程类，具备线程的特性)
class MyThead1(threading.Thread):
    def run(self):
        for i in range(5):
            print(f'MyThead1===={i}')
            time.sleep(1)  # 模拟I/O操作


class MyThead2(threading.Thread):
    def run(self):
        for i in range(5):
            print(f'MyThead2===={i}')
            time.sleep(1)  # 模拟I/O操作


if __name__ == '__main__':
    mt1 = MyThead1()  # 实例化对象
    mt2 = MyThead2()  # 实例化对象

    # mt1.run()
    # mt2.run()
    # 真正启动线程  start
    mt1.start()
    mt2.start()