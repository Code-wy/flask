#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 20:32
# @Author  : 王洋
# @FileName: config.py
# @Software: PyCharm

#encoding:utf-8
HOST = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
PASSWORD = 'root'
DATABASE = 'u1'
DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4'.format(username=USERNAME,
                                                                                        password=PASSWORD,
                                                                                        host=HOST,
                                                                                        port=PORT,
                                                                                        db=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False