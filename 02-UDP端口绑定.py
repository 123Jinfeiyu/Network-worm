# 1.借助socket传输数据，需要导入socket模块（内置模块）
from socket import *  # * 导入所有

# 2. 创建socket对象
# AF_INET: ipv4地址类型  AF_INET6
# SOCK_DGRAM：用udp通信
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 3.绑定端口
local_add = ('192.168.0.101', 7799)
udp_socket.bind(local_add)
'''
3. 准备接收方的地址
ip地址
端口号
注意：需要元组数据类型
'''
address = ('192.168.0.101', 8080)
# 4. 准备要发送的数据
send_data = input("请输入要发送的数据：")
# 5.发送数据, 要求传递的数据字节(二进制数据)
udp_socket.sendto(send_data.encode('gbk'), address)

# 6. 接收数据
res_data = udp_socket.recvfrom(1024)  # 1024 表示本次最大接收的字节数
'''
接收的数据类型是元组，通过下标取值
b'\xcf\xc2\xd3\xea'， 字节流
'''
print(res_data)
# ('192.168.0.101', 8080)
print(res_data[0].decode('gbk'))
# 6. 关闭
udp_socket.close()

'''
TypeError: a bytes-like object is required, not 'str'
要求传递是字节而不是字符串

编码：字符串转为二进制数据，encode()
解码：二进制数据转为字符串, decode()
'''
