from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os 
from flask_cors import CORS

app = Flask(__name__)

app.config['SECRET_KEY'] =  os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

CORS(app)
from application.main_app.routes import main
app.register_blueprint(main)
from application.admin_panel.routes import admin
app.register_blueprint(admin)
