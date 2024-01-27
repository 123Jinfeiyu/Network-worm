trs = input("请输入你翻译的内容：")
'''
trs[0]: 取的是第一个值,进行编码，求长度
如果长度为1：输入英文，英译汉
如果长度为3：输入中文，汉译英
'''
length = len(trs[0].encode('utf-8'))
if length == 3:
    eng = 0
else:
    eng = 1
print(length)