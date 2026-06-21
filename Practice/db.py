import mysql.connector

try:
    conn = mysql.connector.connect(
            user="root",
            password="Showmenew23#",
            host="localhost",
            port=3306,
            database="python"
        )
    if conn.is_connected():
        print("Connected")

except Exception as obj:
    print("cannot connect")

cur = conn.cursor(prepared=True)
# cur.execute("create database python")
# cur.execute("show databases")

# for data in cur:
#     print(data[0])

# cur.execute("use python")
# cur.execute("create table if not exists tutorial(video_id int primary key , video_nm varchar(100) not null , video_views int , watchtime float)")
# insertsql = "insert into tutorial(video_id,video_nm,video_views,watchtime) values(104,'oops basics', 1500, 100),(105,'oops basics', 1500, 100),(106,'oops basics', 1500, 100)"
# update = "update tutorial set video_nm='new oops basic' where video_id=101"
# delete = "delete from tutorial where video_id=104"
# try:
#     cur.execute(delete)
#     conn.commit()
#     print("Succesfully data delete")
#     print(f"{cur.rowcount} row delete")

# except:
#     conn.rollback()
#     print("somthing went wrong")

# cur.execute(select)
# data = cur.fetchall()
# for ele in data:
#     print(ele)
# for ele in data:
#     print(ele)
# print(list(data))
# print(len(data))

select = "select * from tutorial"
cur.execute(select)
# try:
#     while True:
#         data1 = cur.fetchone()
#         if data1==None:
#             break
#         print(data1)      
#     cur.close()
# except:
#     print("unread result found exception occured")

try:
    data1 = cur.fetchmany(3)
    print(data1)
    # cur.close()
except:
    print("unread result found exception occured")

# for i in range(3):
#     inp1 = input("new name : ")
#     inp2 = int(input("new video id : "))
#     updatesql = "update tutorial set video_nm= %s where video_id= %s"
#     cur.execute(updatesql , (inp1 , inp2))
#     conn.commit()

insertsql = "insert into tutorial(video_id,video_nm,video_views,watchtime) values(%s,%s, %s, %s)"
n = int(input("Enter number of video : "))
for i in range(n):
    inp1 = int(input("new video id : "))
    inp2 = input("video name : ")
    inp3 = int(input("video view : "))
    inp4 = int(input("video watch time : "))
    
    cur.execute(insertsql , (inp1 , inp2 , inp3 , inp4))
    conn.commit()

select = "select * from tutorial"
cur.execute(select)

# try:
#     data1 = cur.fetchmany(3)
#     print(data1)
#     cur.close()
# except:
#     print("unread result found exception occured")

cur.close()
conn.close()