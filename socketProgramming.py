from socket import *
udp_socket=socket(AF_INET,SOCK_DGRAM)
DEST_ADDR=('192.168.1.3',8080)
SEND_DATA=input("请输入要发送的数据")
udp_socket.sendto(SEND_DATA.encode('gbk'),DEST_ADDR)
udp_socket.close()
