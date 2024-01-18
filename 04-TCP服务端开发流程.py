# 1. 先导入socket模块
from socket import *

# 2. 创建tcp的socket对象
tcp_socket = socket(AF_INET, SOCK_STREAM)

# 3. 设置端口复用，程序退出，端口号需要释放
tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

# 绑定ip和端口
ip_post = ('', 8080)
tcp_socket.bind(ip_post)

# 设置监听:128最大等待连接数
tcp_socket.listen(128)

# 若有新的客户端来链接这个服务端，产生一个新的对象专门为客户端服务
client_socket, client_addr = tcp_socket.accept()
# print(client_socket)
# print(client_addr)
# 接收服务器分配的服务的socket信息
res_data = client_socket.recv(1024)
print(f'客户端发来：{res_data.decode("gbk")}')

# 关闭
client_socket.close()