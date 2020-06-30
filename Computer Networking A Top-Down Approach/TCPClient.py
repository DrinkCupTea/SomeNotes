from socket import *

serverName = '127.0.0.1'
serverPort = 12000
# 这里的FF_INET表示底层网络为IPV4
# SOCK_STREAM指出了套接字的类型，表明这是一个TCP套接字。
clientSocket = socket(AF_INET, SOCK_STREAM)
# 这行代码就是和服务器发起TCP连接。
# 这行代码执行完后，执行三次握手，并建立器一条TCP连接。
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')
# 因为已经建立了连接，所以只要发送即可。
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()
