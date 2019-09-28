<!-- TOC -->

- [在线词典](#在线词典)
- [1.确定技术点](#1确定技术点)
- [2.mysql 数据库设计 dict](#2mysql-数据库设计-dict)
- [3.结构设计，功能模块划分](#3结构设计功能模块划分)
- [4.通信搭建](#4通信搭建)
- [5.注册](#5注册)
- [6.登录](#6登录)
- [7.查询](#7查询)
- [8.协议](#8协议)
- [9.cookie](#9cookie)

<!-- /TOC -->
# 在线词典
# 1.确定技术点
>* 并发模型和网络模型：
>  多进程tcp 并发模型
>* 确定细节功能，注册要注册什么，注册后是否直接登录：
>注册 ： 用户名密码， 加密存储，注册后直接登录
>历史记录 ： 最近的前10个
>* 一级界面，二级界面如何切换
# 2.mysql 数据库设计 dict
>* words ：  id   　  word 　  mean

>* user: id  　name 　 passwd
>例：
>create table user (id int primary key auto_increment,name varchar(32) not null,passwd char(128) not null);

>* hist :  id  name  word   time
>例：
> create table hist (id int primary key auto_increment,name varchar(32) not null,word varchar(32) not null,time datetime default now());

# 3.结构设计，功能模块划分
>如何封装，客户端和服务端工作流程，有几个功能模块
> * 函数封装
> * 功能模块： 通信，登录，注册，查询，历史记录
# 4.通信搭建
>* tcp传输协议
# 5.注册
>客户端：
>* 输入用户名密码
>* 发送请求
>* 接收反馈

>服务端：
>* 接收请求，判断请求类型
>* 判定用户可否注册
>* 给客户端反馈
# 6.登录
>客户端：
>* 输入用户名密码
>* 发送请求
>* 接收反馈

>服务端：
>* 接收请求
>* 验证信息
>* 发送结果
# 7.查询
>客户端：
>* 输入单词
>* 发送请求 （套接字）
>* 接收结果

>服务端：
>* 接收请求
>* 查找单词
>* 插入历史记录
>* 发送给客户端
# 8.协议
>*登录   L
>*注册   R
>*查单词  Q
>*历史记录  H
>*退出   E

# 9.cookie
>* getpass模块
pwd = getpass.getpass()
功能: 隐藏输入内容
>* hashlib模块
hash = hashlib.md5()
功能： 生产md5对象
参数 ： 盐（自定义的字节串）

>hash.update(passwd.encode())
    功能: 进行加密处理
    参数: 密码转换为字节串

>new_passwd = hash.hexdigest()
    功能： 得到转换后的密码