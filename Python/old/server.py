# #服务端
import socket
#指定通信协议：socket.SOCK_DGTAM,UDP协议；socket.SOCK_STREAM,TCP协议
#指定IP协议版本：spcket.AF_INET,IPV4;socket.AF_INET,IPV4 IPV4的地址是32位长度ipv6是128位
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定IP与端口
ip = '127.0.0.1'#IP不会找，本地连接使用locahost或者127.0.0.1
port = 9000#端口，范围0-65535
soc.bind((ip,port))
#设置监听
soc.listen(5)#五个监听

#连接客户端连接请求：
client_obj,client_addr = soc.accept()#因为会返回socket客户端对像和地址所以得设置两个变量接收
#输出客户端信息，向客户端发送一句话
print(f'>>>{client_addr}')#打印客户端地址
client_obj.send('服务器说：'.encode('utf8'))#用客户端对象调用send方法，并进行编码
msg = client_obj.recv(1024)
print(f'>>>{msg.decode("utf8")}')#打印并解码
