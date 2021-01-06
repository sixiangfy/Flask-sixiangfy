# -*- coding=utf-8 -*-
# @Time : 2021/1/3 19:28
# @Author : siaingfy
# @File : config.py
# @Software : PyCharm

HOST = '127.0.0.1'
PORT     = '3306'  #（默认3306端口）
DATABASE = 'flask_dome1'#（shangchuan为我要连接的数据库的名字）
USERNAME = 'root'#（root权限登录）
PASSWORD = 'root'#（密码）
DIALECT = 'mysql'
DRIVER = 'pymysql'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)


SQLALCHEMY_TRACK_MODIFICATIONS = False