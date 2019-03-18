import pymysql

connection = pymysql.connect(host='localhost',user='root',
                             database='db_demo',port=3306,
                             autocommit = True
                             )
cursor = connection.cursor()
# query = 'SELECT * FROM products'
query = 'SELECT p_name FROM products WHERE p_price < 50000'
cursor.execute(query)
data = cursor.fetchall()
print(data)