#!C:/Users/Surya/AppData/Local/Programs/Python/Python310/python.exe

print("content-type:text/html \r\n\r\n")


print("""<html>
<head>
  <title> Register Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f4f4;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }

    .container {
      background: white;
      padding: 20px 30px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.2);
      width: 300px;
    }

    h2 {
      text-align: center;
      margin-bottom: 20px;
      color: #333;
    }

    label {
      display: block;
      margin: 10px 0 5px;
      font-size: 14px;
    }

    input {
      width: 100%;
      padding: 8px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    button {
      width: 100%;
      padding: 10px;
      background: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }

    button:hover {
      background: #0056b3;
    }

    .link {
      text-align: center;
      margin-top: 10px;
    }

    .link a {
      color: #007bff;
      text-decoration: none;
    }

    .link a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>

  <!-- Registration Form -->
  <div class="container" id="registerForm">
    <h2>Register</h2>
    <form method="post" enctype="multipart/form-data">
      <label for="name">Full Name</label>
      <input type="text" id="name" placeholder="Enter your name" name="u_name"  required>

      <label for="email">Email</label>
      <input type="email" id="email" placeholder="Enter your email" name="u_mail" required>

      <label for="password">Password</label>
      <input type="password" id="password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" placeholder="Enter password" name="usr_pwd" required>
    
      <label for="email">Profile Pic</label>
      <input type="file" id="img"  name="img" required>
     
      <button type="submit" name="submit_btn" >Register</button>
      <p> I Already Have An Account <a href="log.py">Login ?</a></p>
    </form>
  </div>
</body>
</html>
""")

import pymysql
import cgi,cgitb
import os


cgitb.enable()
conn = pymysql.connect(host="localhost",user="root",password="",database="my_app")
curr = conn.cursor()

form = cgi.FieldStorage()

if len(form) != 0:
    try:
        usr_name = form.getvalue("u_name")
        usr_mail = form.getvalue("u_mail")
        usr_password = form.getvalue("usr_pwd")
        img = form['img']
        register_btn = form.getvalue("submit_btn")

        if img.filename:
            pfp = os.path.basename(img.filename)
            file_path = os.path.join("Media", pfp)

            with open(file_path, "wb") as f:
               user_pfp = f.write(img.file.read())

            query = """ INSERT INTO user_info(Name,Email,Password,Image) VALUES ('%s','%s','%s','%s') """% (usr_name,usr_mail,usr_password,pfp)
            curr.execute(query)
            conn.commit()

            print("""
                <script>
                    location.href="log.py";
                </script>
            """)

    except InterruptedError as e:
        print("""
                <script>
                    alert(" unexpected error")
                </script>
                    """)
    finally:
        conn.close()
