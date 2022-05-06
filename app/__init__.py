from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import Config
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
mail = Mail(app)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = '请您登录进入页面！'
login.login_message_category = 'info'

from app.routes import *

