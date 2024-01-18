from socket import *
from threading import Thread


# 定义函数，处理多个客户端发送过来的请求信息
def handle_client_request(client_socket, client_addr):
    # 接收服务器分配的服务的socket信息
    try:
        while True:
            res_data = client_socket.recv(1024)
            print(res_data)
            if res_data:
                print(f'客户端发来：{res_data.decode("gbk")}')
            else:
                print(1111)
                break
    finally:
        client_socket.close()


# 创建tcp socket对象
tcp_socket = socket(AF_INET, SOCK_STREAM)
# 设置端口复用
# SOL_SOCKET:正在设置与socket的基本操作和行为相关的选项
# SO_REUSEADDR：允许重用本地地址和端口
tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
# 绑定ip
ip_port = ('', 8080)
tcp_socket.bind(ip_port)

# 设置最大监听数
tcp_socket.listen(128)
# 死循环
while True:
    # 如果有新的客户端链接这个服务端，产生一个新的套接字专门为这个客户端服务
    client_socket, client_addr = tcp_socket.accept()
    # 生成一个线程对象
    # target=handle_client_request 指定是执行的是哪一个函数
    # args 传递参数， 要求的元组数据类型
    t1 = Thread(target=handle_client_request, args=(client_socket, client_addr))
    # 启动线程
    t1.start()
