import asyncio  # 内置模块，直接导入 在python3.5以后的版本
import time


# 定义异步函数func1
async def func1():
    print(1)
    # 假设碰上了i/o
    # time.sleep(2)
    # 暂停当前的协程，自动切换到tasks中的其他任务
    await asyncio.sleep(2)
    print(2)


# 定义一个异步函数 func2
async def func2():
    print(3)
    # 假设碰上了i/o
    # time.sleep(2)
    await asyncio.sleep(2)
    print(4)


# 将func1()和func2() 包装成Future对象，并放到一个列表中
tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2()),
]

# 获取当前上下文的事件循环（指挥中心)
loop = asyncio.get_event_loop()
# 运行事件循环
loop.run_until_complete(asyncio.wait(tasks))
