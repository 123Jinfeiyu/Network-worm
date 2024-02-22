from queue import Queue

# 设置了大小（设置了最多存放了5个内容，数据可以是任意类型, 超过他的大小会阻塞)
q = Queue(5)
# 往队列里面存放数据
q.put(5)  # 往队列里面存放数据
q.put({"name": "浅安"})  # 往队列里面存放数据
q.put([1, 2, 3])  # 往队列里面存放数据
# print(q.qsize())  # 查看当前队列的大小（存放数据的大小）
q.put('[1, 2, 3]')  # 往队列里面存放数据
q.put(True)  # 往队列里面存放数据
# print(q.qsize())
# q.put(True)  # 往队列里面存放数据

# 从队列里面取数据
'''
取出一个删除一个
'''
print(q.get())  # 先进先出
print(q.get())  # 先进先出
print(q.qsize())
q.put('1111')
print(q.qsize())

print(q.full())  # 判断队列是否满了，如果满了返回是True，否则返回False
print(q.empty())  # 判断队列是否是空的，如果是空的返回True，否则返回False

'''
https://fabiaoqing.com/biaoqing/lists/page/1.html
'''
