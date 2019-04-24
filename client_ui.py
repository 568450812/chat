"""
客户端界面
"""

from client_manager import *


class ClientU:
    def __init__(self):
        self.ui = ClientM()

    def displqy(self):
        print("--------------")
        print("----聊天室-----")
        print("----1.登录-----")
        print("----2.注册-----")
        print("----3.退出-----")
        print("---------------")

    def choose(self):
        value = input("请输入：")
        if value == "1":
            self.login_ui(ADDR)
        elif value == "2":
            self.add_member(ADDR)
        elif value == "3":
            return value

    def main(self):
        while True:
            self.displqy()
            a = self.choose()
            if a == "3":
                break
                # self.choose()

    def login_ui(self, addr):
        while True:
            try:
                id = int(input("请输入用户名:"))
            except Exception:
                print("编号必须位数字")
            else:
                passwd = input("请输入密码:")
                break
        self.ui.login(id, passwd, addr)

    def add_member(self, addr):
        while True:
            name = input("请输入姓名:")
            if len(name) <= 2:
                print("名字长度至少两位")
                continue
            passwd = input("请输入密码:")
            new = input("请再次输入密码:")
            if passwd != new or len(passwd) < 6:
                print("两次输入密码不一致,或者密码长度不够")
                continue
            break
        self.ui.new_member(name, passwd, addr)


main = ClientU()
main.main()

