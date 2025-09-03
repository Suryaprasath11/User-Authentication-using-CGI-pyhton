#!C:/Users/Surya/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")


print("""
<html>
<head>
  <title> Login Form </title>
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
  <!-- Login Form -->
  <div class="container" id="loginForm" style="display:block;">
    <h2>Admin Login</h2>
    <form method="post">
      <label for="loginEmail">Email</label>
      <input type="email" id="loginEmail" placeholder="Enter your email" name="usr_mail" required>

      <label for="loginPassword">Password</label>
      <input type="password" id="loginPassword" placeholder="Enter password" name="usr_password" required>

      <button type="submit" name="login_btn" >Login</button>
    </form>
  </div>
</body>
</html>
""")


import pymysql
import cgi,cgitb


cgitb.enable()


form = cgi.FieldStorage()

if len(form) != 0:
    try:
        Email = form.getvalue("usr_mail")
        password = form.getvalue("usr_password")
        submit_btn = form.getvalue("login_btn")

        if Email =="Admin@gmail.com" and password == "Admin@12345":
          print("""
                <script>
                    location.href ="admin.py";
                </script>
            """)
        else :
            print(f"""
                    <script>
                        alert("Invalid Username Password");
                    </script>
                        """)

    except InterruptedError as e:
        print("""
                <script>
                    alert("Unexpected error: {str(e)}");
                </script>
                    """)