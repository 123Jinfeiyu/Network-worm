# 1. 导入socket模块
from socket import *

# 2. 创建socket对象
# SOCK_STREAM tcp协议
tcp_socket = socket(AF_INET, SOCK_STREAM)

# 3. 建立和服务器连接  ip地址 端口号
ip_port = ('192.168.0.101', 8080)
tcp_socket.connect(ip_port)

'''
将数据从客户端发送给服务器  20:42上课
'''
for i in range(4):
    # 字符串类型数据可以跟整数拼接不？
    data = '你好'+str(i)
    # 需要将传递的数据转为二进制
    data_bytes = data.encode('gbk')
    # 将数据发生给服务器
    tcp_socket.send(data_bytes)

'''
接收服务器传递过来的数据
udp recvfrom
tcp recv 
发送方信息不可用
'''
res_data = tcp_socket.recv(1024)  # 最大接收的字节数
print(res_data.decode('gbk'))  # b'\xcf\xc2\xd3\xea'

# 关闭套接字
tcp_socket.close()