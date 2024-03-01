# lst = ['任务1', '任务2', '任务3']
# print(*lst)

# def demo(*args):
#     print(args)
#
#
# demo(1, 2, 3, 5, 6, 6)


lst = [1, 2, 3]


lst1 = ['1', '2', '3']

lst12 = ['a', 'b', 'c']

lst1.extend(lst)
lst1.extend(lst12)
print(lst1)