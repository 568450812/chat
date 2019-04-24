"""
客户端业务处理
"""

from connect import *
from select import select
import sys

ADDR = ("0.0.0.0", 10010)


class ClientM:
    def __init__(self):
        self.sockfd = Connect()  # 建立连接
        self.rlist = [self.sockfd.sockfd, sys.stdin]  # 创建监控对象
        self.wlist = []
        self.xlist = []
        self.data = None  # 全局变量

    # 与服务器交互登录
    def login(self, id, passwd, addr):
        msg = "L %d %s" % (id, passwd)
        self.sockfd.send(msg, addr)
        data, addr = self.sockfd.recv()
        if data == "OK":
            print("您已进入聊天室")
            self.chat(addr)
        else:
            print(data)

    # 创建新用户
    def new_member(self, name, passwd, addr):
        msg = "N %s %s" % (name, passwd)
        self.sockfd.send(msg, addr)
        data, addr = self.sockfd.recv()
        print(data)

    # 聊天过程
    def chat(self, addr):
        while True:
            try:
                rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            except KeyboardInterrupt:
                self.sockfd.send("Q ",addr)
                return
            else:
                for i in rs:
                    if i is self.sockfd.sockfd:  # 监听接收消息
                        data, addr = i.recvfrom(1024)
                        print(data.decode())
                    elif i is sys.stdin:
                        try:
                            msg = i.readline()  # 监控发消息如果报错返回退出指令
                        except KeyboardInterrupt:
                            value = "Q "
                        else:
                            if msg == "exit\n":
                                value = "Q " + msg
                            else:
                                value = "C " + msg
                        self.data = value  # 将发送的消息转给全局变量
                        self.wlist.append(self.sockfd.sockfd)  # 调用ｗｓ执行发送操作
                for w in ws:
                    if w is self.sockfd.sockfd:
                        w.sendto(self.data.encode(), addr)  # 将内容内容发送到服务端
                        self.wlist.clear()  # 清空执行列表
                        if self.data[0] == "Q":  # 读取内容第一个字符
                            print("退出聊天室")
                            return

