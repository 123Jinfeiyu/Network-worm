def t1():
    print('t1')


def t2():
    print('t2')


# 程序主入口
'''
if: 判断
__name__: 当前文件下执行，__main__
__name__: 作为模块导入执行，当前py的文件名字
'''
print(__name__)
if __name__ == '__main__':  # __main__  '__main__'
    t1()
    t2()
