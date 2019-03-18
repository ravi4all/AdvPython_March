import pymysql

connection = pymysql.connect(host='localhost',user='root',
                             database='db_demo',port=3306,
                             autocommit = True
                             )
cursor = connection.cursor()
p_id = 103
p_name = 'Samsung Galaxy'
p_price = 65000
query = "INSERT INTO products VALUES (%s,%s,%s)"
cursor.execute(query, (p_id, p_name, p_price))
print("Data Inserted Successfully...")