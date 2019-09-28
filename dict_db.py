"""
数据库处理操作
"""

import pymysql
import hashlib

# 对密码进行加密处理
def jm(passwd):
    salt = "^&5#Az$"
    hash = hashlib.md5(salt.encode())  # 生产加密对象
    hash.update(passwd.encode())  # 加密处理
    return hash.hexdigest()

class User:
    def __init__(self, host='localhost',
                 port = 3306,
                 user = 'root',
                 passwd = '123456',
                 charset='utf8',
                 database=None):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.database = database
        self.connect_db()

    # 链接数据库
    def connect_db(self):
        self.db = pymysql.connect(host = self.host,
                                  port = self.port,
                                  user=self.user,
                                  passwd=self.passwd,
                                  database=self.database,
                                  charset=self.charset)

    # 创建游标对象
    def create_cursor(self):
        self.cur = self.db.cursor()

    def register(self,name,passwd):
        sql = "select * from user where name=%s"
        self.cur.execute(sql, [name])
        r = self.cur.fetchone()
        # 查找到说明用户存在
        if r:
            return False

        # 插入用户名密码
        sql = "insert into user (name,passwd) \
                values (%s,%s)"
        passwd = jm(passwd) # 加密处理
        try:
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def login(self,name,passwd):
        passwd = jm(passwd)  # 加密处理
        sql = "select * from user \
                where name=%s and passwd=%s"
        self.cur.execute(sql, [name, passwd])
        r = self.cur.fetchone()
        # 查找到则登录成功
        if r:
            return True
        else:
            return False

    def query(self,word):
        sql = "select mean from words where word=%s"
        self.cur.execute(sql,[word])
        r = self.cur.fetchone()
        if r:
            return r[0]

    def insert_history(self,name,word):
        sql = "insert into hist (name,word) \
        values (%s,%s)"
        try:
            self.cur.execute(sql,[name,word])
            self.db.commit()
        except:
            self.db.rollback()

    def history(self,name):
        sql = "select name,word,time from hist \
        where name=%s order by time desc limit 10"

        self.cur.execute(sql,[name])
        return self.cur.fetchall()








