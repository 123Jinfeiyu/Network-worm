# 1.借助socket传输数据，需要导入socket模块（内置模块）
from socket import *  # * 导入所有
#启动socket套接字，用udp通信
udp_scoket=socket(AF_INET,SOCK_DGRAM)
#绑定端口在这里，注意这是客户端的的端口绑定
local_add=('192.168.1.3',7799)
udp_scoket.bind(local_add)
#准备注意这是服务端的的端口绑定,元组？列表？
address=('192.168.1.3',8080)
# address=['192.168.1.3',8080]
#列表用列表可以吗?（TypeError: sendto(): AF_INET address must be tuple, not list）
send_data=input('请输入你要发送的数据,按回车发送：')
#服务端【Receive from 192.168.1.3 : 7799】：你好
#发送数据,TypeError:
# a bytes-like object is required, not 'str'
#bytes是二进制的字节，不是字符串，所以要求的数据类型是二进制bit/字节,windows默认是gbk
udp_scoket.sendto(send_data.encode('gbk'),address)
#接收数据
res_data=udp_scoket.recvfrom(1024)
#(b'http://www.cmsoft.cn QQ:10865600', ('192.168.1.3', 8080))
#收到的是元组类型b=byte字节流,元组本身是个大集合,所以特定的字符解码，用元组的索引取值
print(res_data[0].decode())
#AttributeError: 'tuple' object has no attribute 'decode'
#close
udp_scoket.close()





