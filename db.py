
import pymysql


conn = pymysql.connect(host="localhost", user="root", password="", database="my_app")
curr = conn.cursor()

query = """ SELECT `id`, `Name`, `Email`, `Password`, `Image` FROM `user_info` WHERE 1 """
curr.execute(query)
result = curr.fetchall()


print(result)

for i in result :
    id = i[0]
    name =  i[1]
    email =  i[2]
    pfp = "Media/" + i[4]

    
print(id)
print(pfp)



# for i in result :
#     id = i[0]
#     name = i[1]

# print(id)
# print(name)