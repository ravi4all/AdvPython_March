import pymysql

connection = pymysql.connect(host='localhost',user='root',
                             database='db_demo',port=3306,
                             autocommit = True
                             )
cursor = connection.cursor()
query = 'CREATE TABLE products (p_id int, p_name varchar(100),p_price double)'
cursor.execute(query)
print("Table Created Successfully...")