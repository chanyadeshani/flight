from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin()
bootstrap = Bootstrap()
