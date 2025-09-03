#!C:/Users/Surya/AppData/Local/Programs/Python/Python310/python.exe

print("content-type:text/html \r\n\r\n")
import cgi, cgitb
import pymysql
cgitb.enable()


conn = pymysql.connect(host="localhost", user="root", password="", database="my_app")
curr = conn.cursor()


form = cgi.FieldStorage()
uid = form.getvalue("id")


name = ""
email = ""

try:
   
    query = "SELECT * FROM user_info WHERE id = %s"
    curr.execute(query, (uid,))
    result = curr.fetchone()

    if result:
        name = result[1]  
        email = result[2]
        user_pfp = result[4]  

        show_pfp = "Media/" + user_pfp 
    else:
        print("<h1>Error: User not found.</h1>")

except Exception as e:
    print(f"<h1>Error: {e}</h1>")

finally:
    conn.close()


# Output the HTML
print(f"""
<html>
<head>
  <meta charset="UTF-8">
  <title>User Profile</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      background: #f4f4f4;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }}

    .profile-container {{
      background: white;
      padding: 30px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      width: 320px;
      text-align: center;
    }}

    h2 {{
      margin-bottom: 15px;
      color: #333;
    }}

    .info {{
      margin: 10px 0;
      font-size: 16px;
      color: #555;
    }}

    label {{
      display: block;
      margin: 15px 0 5px;
      font-size: 14px;
      color: #333;
    }}

    input[type="file"] {{
      display: block;
      margin: 0 auto;
      padding: 5px;
      border: 1px solid #ccc;
      border-radius: 4px;
      cursor: pointer;
    }}

    button {{
      margin-top: 15px;
      width: 100%;
      padding: 10px;
      background: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }}

    button:hover {{
      background: #0056b3;
    }}
  </style>
</head>
<body>

  <div class="profile-container">
    <h2>User Profile</h2>
    <div class="info"><strong>Name: {name}</strong></div>
    <div class="info"><strong>Email: {email}</strong></div>
    <div class="info"><img src="{show_pfp}"</div>
  </div>

</body>
</html>
""")