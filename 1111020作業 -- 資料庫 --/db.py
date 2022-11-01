# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:09:18 2022

@author: Administrator
"""

import pymysql

dbsetting = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'123456789',
    'db':'jobs',
    'charset':'utf8'
    
    }

conn = pymysql.connect(**dbsetting)