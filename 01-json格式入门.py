s1 = 'hello'
s2 = {"name": "python"}
s3 = '{"name": "python"}'  # json格式的数据, 本质上数据类型是字符串
s4 = 'jquery:[{"name":"python"}]'  # str, json格式的数据？

# <class 'str'> <class 'dict'> <class 'str'> res.text: 字符串
# print(type(s1), type(s2), type(s3),type(s4))
#
# # 提取json格式的数据
import json
import re
# data = json.loads(s3)  # 将json格式的字符串数据转变对应python数据类型(字典)
data = eval(s3)
print(type(data), data['name'])
result = re.match(r'jquery:(.*)', s4)
# group(1), 取的是第一个括号里面的内容
print(result.group(1))
# data1 = json.loads(result.group(1))
data1 = eval(result.group(1))
# '''
# # json格式 里面的内容是用双引号引起
# json.decoder.JSONDecodeError:Expecting property name enclosed in double quotes
# # 不是一个json格式的数据
# json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
# '''

print(data1[0]['name'])

# print(dict(s3))  # key:value 强制转换成字典报错
# data = eval(s3)
# print(type(data))  # key:value

print(eval('1+1'))  # 2

'''
dumps(): 将python对象转变成json格式字符串数据
'''
# import json

s2 = {'name': 'python'}
s3 = [{'name': 'python'}]
res1 = json.dumps(s2)
res2 = json.dumps(s3)
f=open('data.json','w',encoding='utf-8')
res3 = json.dump(s3,f)
print(res1, res2, type(res1), type(res2),type(s4))


'''
json.dump(): 将Python中的对象转换成Json字符串存储到文件中
TypeError: write() argument must be str, not dict
write:写入的数据必须是字符串类型的数据
'''
# import json
# data = {'name': 'python', 'name1': '浅安'}
# # json格式数据写入文件，如果包含中文，
# f = open('data.json', 'w', encoding='utf-8')
# # f.write(data)
# # 第一个参数：数据
# # 第二个参数：文件对象，写入哪一个文件当中
# json.dump(data, f, ensure_ascii=False)  # 中文不默认用Ascii编码写入ensure_ascii=False

'''
json.load():将文件中的Json字符串转换成Python对象提取出来
'''
import json

#
# f = open('data.json', 'r', encoding='utf-8')
# # print(type(f.read()))  # 默认read(),数据类型是字符串
# result = json.load(f)
# print(result, type(result))

'''
sort_keys:
'''
data = [{('a',): 1, 'c': 3, 'b': 2}]
print(data)
# 排序  sort_keys=True 根据key做对应的排序
# print('排序之后的结果：', json.dumps(data, sort_keys=True))

# 设置显示效果  indent=2: 缩进两个字符
# print('INDENT：', json.dumps(data, indent=1))

# 设置分隔符
# print('分隔符：', json.dumps(data, separators=(',', ':')))
'''
keys must be str, int, float, bool or None, not tuple
json需要字典的键是字符串，整形，浮点数，布尔类型
'''


def encode_data(data, skip_keys=False):
    # 在这里进行一些操作，使用了 skip_keys 参数
    if skip_keys:
        # 如果 skip_keys 为 True，则跳过键的处理
        encoded_result = json.dumps(data, skipkeys=True)
    else:
        # 否则按照正常处理方式进行
        encoded_result = json.dumps(data)

    return encoded_result


# 使用例子
my_data = {("key1","key2"): "value1", "key2": "value2", "key3": "value3"}
result_with_skip = encode_data(my_data, skip_keys=True)
result_without_skip = encode_data(my_data, skip_keys=True)

print("Result with skip keys:", result_with_skip)
print("Result without skip keys:", result_without_skip)
