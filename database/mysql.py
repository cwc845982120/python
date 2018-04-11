# -*- coding: UTF-8 -*-

import MySQLdb
import config_data

# 打开数据库连接
try:
    db = MySQLdb.connect(config_data.DB_HOST, config_data.DB_USER, config_data.DB_PASSWORD, config_data.DB_NAME)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM T_users"

    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        uid = row[0]
        name = row[1]
        sex = row[2]
        age = row[3]
        # 打印结果
        print ("id=%d, name=%s, sex=%s, age=%d" % (uid, name, sex, age))

    # 关闭数据库连接
    db.close()

except IOError:
    print ("Error: unable to fetch data")
