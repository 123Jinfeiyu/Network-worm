import csv

# with open('douban.csv', 'r', encoding='utf-8-sig') as f:
#     # 1. 创建读取对象
#     reader = csv.reader(f)  # f 文件对象
#     print(reader)  # <_csv.reader object at 0x0000020E24365A00> 返回生成器对象
#     # 生成器或者迭代器取值 通过next()
#     for r in reader:
#         print(r)


with open('douban.csv', 'r', encoding='utf-8-sig') as f:
    # 1. 创建读取对象
    reader = csv.DictReader(f)
    for r in reader:
        print(r['评分'])  # 输出的内容就呈现的是字典格式
