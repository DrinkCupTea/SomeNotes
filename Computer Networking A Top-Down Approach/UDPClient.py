# 该socket模块形成了在Python中所有网络通信的基础
from socket import *

# 这里是"hostname"，可以是IP地址，也可以是主机名
serverName = '127.0.0.1'
serverPort = 12000
# 下行创建了客户的套接字。
# 第一个参数只是了地址簇；特别是AF_INET指示了底层网络使用IPV4。
# 第二个参数指示了该套接字是SOCK_DGRAM类型的，这意味着它是一个UDP套接字。
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('input lowercase setence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
# 接收消息和消息源地址
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
