"""
dict 客户端

功能: 发起请求,接收结果
"""

from socket import *
import sys
import getpass

# 服务器地址
ADDR = ('127.0.0.1',8888)
s = socket()
s.connect(ADDR)

# 注册功能
def do_register():
    while True:
        name = input("User:")
        pwd = getpass.getpass()
        pwd1 = getpass.getpass("Again:")
        if pwd != pwd1:
            print("两次密码不一致！")
            continue
        if (' ' in name) or (' ' in pwd):
            print("用户名或密码不能含有空格")
            continue

        msg = "R %s %s"%(name,pwd)
        s.send(msg.encode()) # 发送请求
        data = s.recv(128).decode() # 反馈
        if data == 'OK':
            print("注册成功")
            login(name)
        else:
            print("注册失败")
        return

# 登录
def do_login():
    name = input("User:")
    passwd = getpass.getpass()

    msg = "L %s %s"%(name,passwd)
    s.send(msg.encode())  # 发请求
    data = s.recv(128).decode() # 得到反馈
    if data == 'OK':
        print("登录成功")
        login(name)
    else:
        print("登录失败")

#　查单词
def do_query(name):
    while True:
        word = input("单词:")
        if word == '##':
            break
        msg = "Q %s %s"%(name,word)
        s.send(msg.encode())
        #　得到结果
        data = s.recv(2048).decode()
        print(data)

def do_history(name):
    msg = "H "+name
    s.send(msg.encode())
    while True:
        data = s.recv(1024).decode()
        if data == '##':
            break
        print(data)

# 登录后的二级界面
def login(name):
    while True:
        print("""
        ==============%s Query ============
          1.查单词     2.历史记录     3.注销
        ===================================
        """%name)
        cmd = input("选项(1,2,3):")
        if cmd == '1':
            do_query(name)
        elif cmd == '2':
            do_history(name)
        elif cmd == '3':
            return  # 二级界面结束
        else:
            print("请输入正确命令")


# 搭建网络
def main():
    while True:
        print("""
        ========== Welcome ============
          1.注册     2.登录     3.退出
        ===============================
        """)
        cmd = input("选项(1,2,3):")
        if cmd == '1':
            do_register()
        elif cmd == '2':
            do_login()
        elif cmd == '3':
            s.send(b'E')
            sys.exit("谢谢使用")
        else:
            print("请输入正确命令")

if __name__ == '__main__':
    main()








