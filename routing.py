from flask import render_template,redirect,request
from tomlkit import key_value

from app import app,User

from data.sql import user_create, user_twin_checker, authenticate, user_get
from flask_login import current_user,login_user

@app.get('/')
def index():
    print(current_user)
    return render_template('index.html')


@app.route('/register', methods = ['POST', 'GET'])
def register_page():
    if request.method == "GET":
        return render_template('register.html')
    data = request.form.to_dict()
    username = data["username"]
    password = data["password"]
    if user_twin_checker(username):
        return redirect('/register')
    user_create(data["username"], data["password"])
    return redirect('/login')

@app.route('/login', methods = ['POST', 'GET'])
def login_page():
    if request.method == "GET":
        return render_template('login.html')
    data = request.form.to_dict()
    username = data["username"]
    password = data["password"]
    user = authenticate(username,password)
    if user:
        login_user(User(user[0],user[1]))
        return redirect('/')
    return redirect('/login')


app.run(debug=True)