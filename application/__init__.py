from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_cors import CORS

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://dtcgzzurvhmyok:8ce9d739907569d618ebfe80185834d85268479b01ac47c41632c6e12854166a@ec2-54-87-112-29.compute-1.amazonaws.com:5432/dbbelahmo011t8"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

CORS(app)
from application.main_app.routes import main
app.register_blueprint(main)
from application.admin_panel.routes import admin
app.register_blueprint(admin)
