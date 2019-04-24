"""
服务器端用户处理
"""

from helper_da import *
from connect import *
from time import ctime

addr = ("0.0.0.0", 10010)


class ServerM:
    def __init__(self):
        self.mysql = MenberManage()  # 连接数据库
        self.sockfd = Connect()  # 调用连接
        self.sockfd.bind(addr)
        self.data = None

    # 给在线列表里所有人发消息
    def send_all(self, data):
        for i in self.mysql.select_all("online"):
            self.sockfd.send(data, (i[1], i[2]))

    # 登录操作
    def do_login(self, id, passwd, addr):
        if self.mysql.select_passwd(id, passwd):  # 查询用户名密码是否匹配　匹配返回TRUE
            name, status = self.mysql.find_name(id)  # 根据编号查找账户状态
            if status == "1":
                value = "帐号已经被封"
                self.sockfd.send(value, addr)
                return
            else:
                value = "OK"
            self.sockfd.send(value, addr)
            msg = "欢迎%s进入聊天室" % name
            self.mysql.add_online(name, addr[0], addr[1], status)  # 加入在线人员列表　姓名　ｉｐ地址　端口号　状态
            self.send_all(msg)

        else:
            value = "登录失败帐号或密码错误"
            self.sockfd.send(value, addr)
            return

    # 添加新用户
    def do_new(self, name, passwd, addr):
        if self.mysql.add_member(name, passwd):  # 增加新用户到列表
            result = self.mysql.return_id(name, passwd)
            value = "创建成功,您的编号为%d" % result
            self.sockfd.send(value, addr)
        else:
            value = "创建失败"
            self.sockfd.send(value, addr)

    # 聊天功能
    def chat(self, msglist, addr):
        list01 = ' '.join(msglist)
        name, status = self.mysql.select_name_status(addr[1])  # 根据用户编号查找姓名
        if status == "3":
            self.sockfd.send("您已被禁言", addr)
        else:
            self.mysql.save(name, list01[2:])  # 保存聊天内容
            msg = "%s\n%s:%s" % (ctime(), name, list01[2:])
            self.send_all(msg)  # 给所有人传递消息

    # 从在线用户列表中删除
    def del_mem(self, addr):
        name,status = self.mysql.select_name_status(addr[1])
        if self.mysql.delete_online(addr[1]):  # 如果删除成功
            value = "%s退出聊天室" % name
            self.send_all(value)

    def manager_msg(self):
        value = "管理员消息"
        msg = "%s:%s" % (value, self.data)  # 利用value给所有人发送信息
        self.send_all(msg)

    # 查询操作
    def members(self, data):
        return self.mysql.select_all(data)

    # 更改用户状态
    def provent(self, id, data):
        return self.mysql.change_status(id, data)

    # 处理用户请求
    def requst(self):
        try:
            while True:
                data, addr = self.sockfd.recv()
                msglist = data.split(' ')
                if msglist[0] == "L":
                    self.do_login(eval(msglist[1]), msglist[2], addr)
                elif msglist[0] == "N":
                    self.do_new(msglist[1], msglist[2], addr)
                elif msglist[0] == "C":
                    self.chat(msglist, addr)
                elif msglist[0] == "Q":
                    self.del_mem(addr)
        except Exception:
            return


if __name__ == "__main__":
    s = ServerM()
    s.requst()
