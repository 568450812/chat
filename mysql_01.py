"""
create table members(
id int(11) primary key auto_increament,
name varchar(32) not null,
passwd varchar(32) not null,
status varchar(4) default '0')default charset=utf8;

create table online(
name varchar(32) not null,
addr varchar(32) not null,
dns int(11) primary key,
status varchar(32))default charset=utf8;

create table massage(
name varchar(32) not null,
time datetime,
massage varchar(1024))default charset=utf8;
"""

host = "localhost"
user = "root"
passwd = "123456"
name = "chat"

# 编写第一种方案
# hellow world