"""
The flask application package.
"""

from distutils.command.config import config
import imp
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

from .config import Config

app = Flask(__name__)
app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = "LKJHOIHoih98y98"

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
#login_manager.login_view = "home"


db = SQLAlchemy(app)
ma = Marshmallow(app)

# setting up views
import small_group_app.view
import small_group_app.views.home_view
import small_group_app.views.prayer_request_view
import small_group_app.views.directory_view
import small_group_app.views.user_settings_view
