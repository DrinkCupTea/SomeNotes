from socket import *

serverPort = 12000
# 使用IPV4，且为TCP套接字
# 这里的serverSocket就是欢迎套接字
serverSocket = socket(AF_INET, SOCK_STREAM)
# 绑定端口
serverSocket.bind(('', serverPort))
# 等待连接，这里定义请求连接最大数为 1
serverSocket.listen(1)
print('The server is ready to receive.')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
