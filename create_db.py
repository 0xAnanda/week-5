import mysql.connector

connection= mysql.connector.connect(host='localhost',
                                    port = '3306',
                                    user='root',
                                    password='ananda1991',
                                    database='website')

cursor=  connection.cursor()

# 創建資料庫 
# cursor.execute("CREATE DATABASE `testdb`; ")

# 取得資料庫名稱
# cursor.execute("SHOW DATABASES;")
# records= cursor.fetchall()
# for r in records:
#     print(r)


# 選擇資料庫
# cursor.execute("USE testdb;")

# 創建表格
# cursor.execute('CREATE TABLE test(name INT);')

# 取得˙部門表格所有資料
cursor.execute('SELECT * FROM message;')

records= cursor.fetchall()
for r in records:
    print(r)



cursor.close()
connection.commit()
connection.close()