import execjs
#得到node.js的版本号
# print(execjs.get().name)
# eval 和 complie 是要构建一个JS的环境
# e = execjs.eval('a = new Array(1,2,3)')  # 可以直接执行JS代码
# print(e)
# x = execjs.compile('''
#         function add(x,y){
#             return x+y;
#             };
#         ''')
# print(x.call('add', '1', '2'))  # execjs.compile用于执行更复杂的js代码，这里是字符串拼接不是加减法运算
# print(x.call('add', 1, 2))  # execjs.compile用于执行更复杂的js代码，这里是加减法运算
with open('douyin.js','r',encoding='UTF-8') as f:
    jsdata = f.read()

ctx = execjs.compile(jsdata)
print(ctx.call('window.yuan', '12'))

