"""服务端界面"""

from server_manager import *
from threading import Thread


class ServerU:
    def __init__(self):
        self.ui = ServerM()

    def displqy(self):
        print("-------------------")
        print("---1.查看在线人员---")
        print("---2.查看所有人员---")
        print("---3.查看聊天内容---")
        print("--4.发送管理员消息--")
        print("---5.修改账户状态---")
        print("------6.退出------")
        print("------------------")

    def choose(self):
        value = input("请输入选项:")
        if value == "1":
            self.select_online()
        elif value == "2":
            self.select_members()
        elif value == "3":
            self.select_massage()
        elif value == "4":
            self.send_msg()
        elif value == "5":
            self.arrange_status()
        elif value == "6":
            return value
        else:
            print("输入有误")

    def arrange_status(self):
        print("1.封号,2.解封,3.禁言,4.解言")
        value = input("请输入:")
        if value == "1":
            id = int(input("请输入封杀编号:"))
            self.ui.provent(id, "1")
        elif value == "2":
            id = int(input("请输入解封编号:"))
            self.ui.provent(id, "0")
        elif value == "3":
            id = int(input("请输入禁言编号:"))
            self.ui.provent(id, "3")
        elif value == "4":
            id = int(input("请输入解言编号:"))
            self.ui.provent(id, "0")
        else:
            return

    def send_msg(self):
        value = input("请输入想要发送的消息：")
        self.ui.data = value
        self.ui.manager_msg()

    def select_online(self):
        for i in self.ui.members("online"):
            print("用户姓名:%s 用户端口:%d 用户状态:%s" % (i[0], i[2], i[3]))

    def select_members(self):
        for i in self.ui.members("members"):
            print("用户编号:%d 用户姓名:%s 用户密码:%s 用户状态:%s" % (i[0], i[1], i[2], i[3]))

    def select_massage(self):
        for i in self.ui.members("massage"):
            print("用户姓名:%s 时间:%s 聊天内容%s" % (i[0], i[1], i[2]))

    def main(self):
        t = Thread(target=self.ui.requst)
        t.daemon = True
        t.start()
        while True:
            self.displqy()
            if self.choose() == "6":
                break


s = ServerU()
s.main()
