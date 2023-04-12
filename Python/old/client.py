import socket

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = '127.0.0.1'#IP不会找，本地连接使用locahost或者127.0.0.1
port = 9000#端口，范围0-65535

'''需要再写一个客户端导入创建'''
soc.connect((ip,port))#连接服务端  

#接受服务端消息、
msg = soc.recv(1024)#表示一次最多接受1024个字节
print(f'>>>{msg.decode("utf8")}')#打印并解码
soc.send('你好'.encode('utf8'))#用客户端对象调用send方法，并进行编码
