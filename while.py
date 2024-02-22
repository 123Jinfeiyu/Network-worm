from queue import Queue
import queue

q = Queue(100)
q.put(5)  # 往队列里面存放数据
q.put(5)  # 往队列里面存放数据
q.put(5)  # 往队列里面存放数据
q.put(5)  # 往队列里面存放数据
q.put(None)#如果在我们获取数据中put了一个None,破坏了数据的完整性
q.put({"name": "浅安"})  # 往队列里面存放数据
# print(q.qsize())  # 查看当前队列的大小（存放数据的大小）
q.put('[1, 2, 3]')  # 往队列里面存放数据
q.put('[1, 2, 3]')  # 往队列里面存放数据
q.put('[1, 2, 3]')  # 往队列里面存放数据
q.put('[1, 2, 3]')  # 往队列里面存放数据
q.put('[1, 2, 3]')  # 往队列里面存放数据
q.put(None)
while True:
    data = q.get()
    if data is None:
    #程序会提前终止
        break
    else:
        print(data)