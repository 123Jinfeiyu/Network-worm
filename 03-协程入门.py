from greenlet import greenlet

'''
greenlet  协程模块 第三方的  早期的模块
pip install greenlet
'''


def func1():
    print(1)
    gr2.switch()  # 切换到了func2函数，会记录上次执行的位置
    print(2)
    gr2.switch()


def func2():
    print(3)
    gr1.switch()
    print(4)


# 生成一个协程对象
gr1 = greenlet(func1)  # 传递的是函数名
gr2 = greenlet(func2)

# 通过switch触发
gr1.switch()
