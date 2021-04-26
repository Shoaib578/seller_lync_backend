from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_cors import CORS

app = Flask(__name__)

app.config['SECRET_KEY'] = 'assdasdaiahsidha8s6e82ugaugsd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dmrqejlvdfecit:b76cf94be74ad2c20b6e93297172f68d31caf12ebbe261f183c71b5c1c9a5785@ec2-3-233-43-103.compute-1.amazonaws.com:5432/d80fnc1h5ocupb'


db = SQLAlchemy(app)
Migrate(app,db)

CORS(app)
from application.main_app.routes import main
app.register_blueprint(main)
from application.admin_panel.routes import admin
app.register_blueprint(admin)
