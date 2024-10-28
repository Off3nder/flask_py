from flask import Flask

from flask_login import LoginManager,UserMixin

from data.sql import user_get

import secrets

app = Flask(__name__)
login_manager = LoginManager()

app.config["SECRET_KEY"] = secrets.token_urlsafe(16)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    user_data = user_get(user_id)
    return User(user_data[0],user_data[1])

class User(UserMixin):
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
