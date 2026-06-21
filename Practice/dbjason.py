import mysql.connector
import json

try : 
    conn = mysql.connector.connect(
        user = 'root',
        password = 'Showmenew23#',
        host = 'localhost',
        port = 3306,
        database = "python"
    )
    if conn.is_connected():
        print("connect")

except:
    print("DB not connected")

cur = conn.cursor()

with open('Practice/db.json','r') as data:
    content = json.load(data)
    print(content)

createsql = "create table if not exists vegetables(id int primary key , name varchar(100) not null , color varchar(100) not null , price_per_kg int not null , in_stock boolean)"
insertsql = "insert into vegetables(id , name , color , price_per_kg , in_stock) value(%s,%s,%s,%s,%s)"

cur.execute(createsql)

for iteam in content:
    val = (iteam['id'],iteam['name'],iteam['color'],iteam['price_per_kg'],iteam['in_stock'])
    print(val)
    cur.execute(insertsql , val)
    conn.commit()

cur.close()
conn.close()