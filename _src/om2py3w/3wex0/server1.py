# coding:utf-8
import socket
import sys


host = '127.0.0.1'
port = 5678

def server_con():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# 创建对象

    s.bind((host, port))#绑定端口

    s.listen(1)#监听连接


    clientSocket,clientAdrr = s.accept()#接受请求

    print 'Client conneted!'
    ip = raw_input()

    clientSocket.sendall(ip)#数据收发(怎么让 client 连续接受？)
    data, addr = s.recvfrom(1024)
    print "已接受信息：", data, "来自：",addr

    clientSocket.close()#关闭端口
while True:
	server_con()