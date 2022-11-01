# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:11:37 2022

@author: Administrator
"""

import db
from datetime import datetime 

item = int(input('請輸入 : 1. 新增員工資料 2. 修改員工電話及性別  3. 輸入員工編號，查詢員工基本資料 4. 輸入員工編號，印出員工姓名及工作項目、工作詳述 : '))
print()

# 新增員工資料
if item == 1:
    name = input('請輸入姓名: ')
    sex = input('請輸入性別 ( M / F): ')
    tel = input('請輸入電話: ')
    now = datetime.now()
    assume = datetime.strftime(now, '%Y-%m-%d')
    
    sql = 'insert into employee(name, sex, tel, assume) values("{}","{}","{}","{}")'.format(name, sex, tel, assume)
    
    cursor = db.conn.cursor()
    cursor.execute(sql)
    cursor = db.conn.commit()

    items = input("請輸入工作項目: ")
    info = input("請輸入工作詳述: ")

    sql = 'insert into works(items, info) values("{}","{}")'.format(items, info)

    cursor = db.conn.cursor()
    cursor.execute(sql)
    cursor = db.conn.commit()

    db.conn.close()
    
# 修改員工電話及性別
elif item == 2:
    
    employee = input("請輸入想要修改的員工 ID: ")
    tel = input("請輸入欲修改電話: ")
    sex = input("請輸入欲修改性別 (M/F): ")
    
    sql = 'update employee set tel = "{}" , sex = "{}" where id="{}" '.format(tel, sex, employee)
    
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    
    db.conn.close()


# 查詢員工基本資料
elif item == 3:

    sql = 'select id, name from employee'

    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()

    allemp = cursor.fetchall()

    for row in allemp:
        print("員工id: ",row[0])
        print("員工姓名: ",row[1])
        print()
        
    empid = input("請輸入員工ID: ")
    
    sql = 'select name, sex, tel from employee where id="{}"'.format(empid)
    
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    
    result = cursor.fetchall()
    
    for row in result:
        print('員工姓名: ',row[0])
        print("員工性別: ",row[1])
        print("員工電話: ",row[2])
        print()
    
    db.conn.close()

# 印出員工姓名及工作項目、工作詳述
elif item == 4:

    sql = 'select id, name from employee'

    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()

    allemp = cursor.fetchall()

    for row in allemp:
        print("員工id: ",row[0])
        print("員工姓名: ",row[1])
        print()
    
    empid = input("請輸入員工編號: ")
    
    sql = 'select e.name, w.items, w.info from employee e inner join works w on e.id = w.id where e.id="{}"'.format(empid)
    
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    
    result = cursor.fetchall()
    
    for row in result:
        print('員工姓名: ',row[0])
        print('員工工作項目: ',row[1])
        print('員工工作詳述: ',row[2])
        print()
    
    db.conn.close()
    
else:
    print("請重新輸入數字")
    
    
    




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    