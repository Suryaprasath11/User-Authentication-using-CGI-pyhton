#!C:/Users/Surya/AppData/Local/Programs/Python/Python310/python.exe

print("content-type:text/html \r\n\r\n")



import cgi ,cgitb
import pymysql


cgitb.enable()

conn = pymysql.connect(host="localhost",user="root",password="",database="my_app")
curr = conn.cursor()


form = cgi.FieldStorage()

uid = form.getvalue("id")
query = """SELECT * FROM user_info WHERE id= '%s'""" % uid
curr.execute(query)

result = curr.fetchall()
for i in result:
    name = i[1]
    email = i[2]
    pfp = i[4]

show_pfp = "Media/" + pfp
print(f"""
<!DOCTYPE html>
<html>
<head>
  <title>Home Page</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 0;
      background: #f4f4f4;
      color: #333;
    }}
      
    /* Navbar */
    .navbar {{
      background: #007bff;
      padding: 15px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: white;
    }}
    .navbar h1 {{
      margin: 0;
      font-size: 22px;
    }}
    .navbar ul {{
      list-style: none;
      display: flex;
      margin: 0;
      padding: 0;
    }}

    .navbar ul li {{
      margin-left: 30px;
    }}
      .navbar ul li a {{
        color: white;
        text-decoration: none;
        font-size: 16px;
      }}

    .navbar ul li a:hover {{
      text-decoration: underline;
    }}

    /* Hero Section */
    .hero {{
      text-align: center;
      padding: 60px 20px;
      background: white;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}

    .hero h2 {{
      font-size: 28px;
      margin-bottom: 15px;
    }}

    .hero p {{
      font-size: 16px;
      color: #555;
      max-width: 600px;
      margin: 0 auto;
    }}
    
    .PFP {{
      text-align: center;
      text-align: center;
      background: white;
      
    }}

  </style>
</head>
<body>

  <!-- Navbar -->
  <div class="navbar">
    <center><h1>My App</h1></center>
      <ul>
        <li><a href='./admin_log.py'>Admin</a></li><br>
        <li><a href='./user_profile.py?id={uid}'>Profile</a></li>
        <li><a href='./log.py'>Logout</a></li><br>

      </ul>
  </div>

  <!-- Hero Section -->
  <div class="hero">
    <h2>Welcome {name} </h2>
    <p>CONGRATULATION DUDE ! You are Now into the home page of the application </p>
  </div>
  <div class="PFP">
      <img src="{show_pfp}"height= "300px" width="fit-content">
  </div>
    <center>
</body>
</html>
""" )