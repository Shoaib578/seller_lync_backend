from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_cors import CORS

app = Flask(__name__)

app.config['SECRET_KEY'] = 'uas9du90uasuduu023HAHSduaSHâsdasd'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://cphjoszshwxwdg:5fb112fd5b5da5f2014440c6c8349032d7e3af24935a4181cf2928d5a093749b@ec2-34-192-58-41.compute-1.amazonaws.com:5432/d7acogalgph1eo"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

CORS(app)
from application.main_app.routes import main
app.register_blueprint(main)
from application.admin_panel.routes import admin
app.register_blueprint(admin)
