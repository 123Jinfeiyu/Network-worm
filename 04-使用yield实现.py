def func2():
    yield 3
    yield 4


def func1():
    yield 1
    # 切换到func2函数
    yield from func2()
    yield 2


# 创建了func1生成器对象
f1 = func1()  # 1
# print(f1)
# print(next(f1))  #
# print(next(f1))  #
# print(next(f1))  #
# print(next(f1))  #
for item in f1:
    print(item)