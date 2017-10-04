from flask import Flask, request, redirect, render_template
import cgi
import os 
import jinja2

app = Flask(__name__)
app.config["DEBUG"] = True 

@app.route("/")
def index():
    return render_template("indexpage.html")

@app.route("/", methods=["POST"])
def validate():

    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if len(username) < 3 or len(username) > 20:
        username_error = "Invalid username"
        username = ""
    else:
        if " " in str(username):
            username_error = "Invalid space in username"
            username = ""
    
    if len(password) < 3 or len(password) > 20:
        password_error = "Invalid password length"
        password = ""
    else:
        if " " in str(password):
            password_error = "Invalid space in password"
            password = ""

    if password != verify:
        verify_error = "Passwords do not match"
        verify = ""
    
    elif len(verify) < 3 or len(verify) > 20:
        verify_error = "Invalid verification length"
        verify = ""
    else:
        if " " in verify:
            verify_error = "Invalid space in verification"
            verify = ""
        
    if "." not in email and "@" not in email:
        email_error = "Invalid Email"
        email = ""

    if not username_error and not password_error and not verify_error and not email_error:
        username = str(username)
        return redirect("/welcome?username={0}".format(username))
    else:
        return render_template("indexpage.html",
            username_error=username_error,
            password_error=password_error,
            verify_error=verify_error,
            email_error=email_error)  

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template("welcomepage.html", username=username)  

if __name__ == "__main__":
    app.run()