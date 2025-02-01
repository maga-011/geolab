from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# Initialize the database and login manager
db = SQLAlchemy()
login_manager = LoginManager()

# Initialize the Flask app here
app = Flask(__name__)

# Set app configurations
app.config['SECRET_KEY'] = 'wdwwfwfwfesfgesedge2'
instance_path = os.path.join(os.getcwd(), 'instance')
if not os.path.exists(instance_path):
    os.makedirs(instance_path)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{instance_path}/mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
login_manager.init_app(app)

# Set login view for Flask-Login
login_manager.login_view = "login"