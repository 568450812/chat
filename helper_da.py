"""
sql　语句
"""

from helper_n import *


# from member import *


class MenberManage:
    def __init__(self):
        self.mysql = Helper()
        self.mysql.open_mysql()  # 连接数据库

    def __del__(self):
        self.mysql.close_mysql()  # 关闭数据库

    # 增加新用户
    def add_member(self, name, passwd):
        value = "insert into members(id,name,passwd) values(NULL,'%s','%s')" % (name, passwd)
        result = self.mysql.update(value)
        if result:
            return True
        else:
            return False

    # 根据编号查询密码
    def select_passwd(self, id, passwd):
        value = "select passwd from members where id = %d" % id
        result = self.mysql.select(value)
        try:
            if passwd in result[0]:
                return True
            else:
                return False
        except Exception:
            print("输入信息有误")

    # 查询表方法
    def select_all(self, data):
        value = "select * from %s " % data
        result = self.mysql.select(value)
        return result

    # 根据编号查询姓名
    def find_name(self, id):
        value = "select name,status from members where id = %d" % id
        result = self.mysql.select(value)
        if result[0][0] and result[0][1]:
            return result[0][0], result[0][1]
        else:
            print("找不到")

    # 增加成员到在线人员列表
    def add_online(self, name, addr, dns, status):
        value = "insert into online values('%s','%s',%d,'%s')" % (name, addr, dns, status)
        result = self.mysql.update(value)
        if result:
            return True
        else:
            return False

    # 根据姓名密码查询用户编号
    def return_id(self, name, passwd):
        value = "select id from members where name = '%s' and passwd = '%s'" % (name, passwd)
        result = self.mysql.select(value)
        try:
            if result[0][0]:
                return result[0][0]
        except Exception:
            print("有误")

    # 根据端口号查询姓名和状态
    def select_name_status(self, dns):
        value = "select name,status from online where dns = %d" % dns
        result = self.mysql.select(value)
        try:
            if result[0][0]:
                return result[0][0],result[0][1]
        except Exception as e:
            print("有误",e)

    # 用户退出从在线列表中删除
    def delete_online(self, dns):
        value = "delete from online where dns = '%d'" % dns
        result = self.mysql.update(value)
        if result:
            return True
        else:
            return False

    # 保存用户聊天信息
    def save(self, name, massage):
        value = "insert into massage values('%s',%s,'%s')" % (name, "now()", massage)
        result = self.mysql.update(value)
        if result:
            return True
        else:
            return False

    # 改变用户状态
    def change_status(self, id, data):
        value = "update members set status = '%s' where id = %d" % (data, id)
        result = self.mysql.update(value)
        if result:
            return True
        else:
            return False
