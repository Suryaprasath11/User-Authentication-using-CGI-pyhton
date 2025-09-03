#!C:/Users/Surya/AppData/Local/Programs/Python/Python310/python.exe

print("content-type:text/html \r\n\r\n")
import cgi, cgitb
import pymysql
cgitb.enable()


conn = pymysql.connect(host="localhost", user="root", password="", database="my_app")
curr = conn.cursor()



query = """ SELECT `id`, `Name`, `Email`, `Password`, `Image` FROM `user_info` WHERE 1 """
curr.execute(query)
result = curr.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

    <style>
        body{
            background-color: rgb(248, 250, 250);
        }
        .usr_list{
            margin-top: 1%;
            padding: 5%;
        }
        .usr_list table {
            padding: 50px;
            border-radius: 3%;
        }
        .usr_list table th {
            padding: 8px 15px;
        }
        .usr_list table td{
            padding: 20px 30px;
        }
    </style>

<body>
    
    <center>
        <div class="usr_list">
        <h1>USERS LIST</h1>
            <table border="1px" type="dashed">
            <br>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>EMAIL</th>
                <th>PROFILE</th>
            </tr>
      """)
for i in result :
    id = i[0]
    name =  i[1]
    email =  i[2]
    pfp = "Media/" + i[4]

    print(f"""
    <tr>
    <td>{id}</td>
    <td>{name}</td>
    <td>{email}</td>
    <td><img src="{pfp}" alt="Profile" width="50"></td>
    </tr>
    """)

print("""
            </tr>
        </table>
        </div>
    </center>
</body>
</html>
""")
conn.close()