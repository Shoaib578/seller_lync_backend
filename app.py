from application import app,db

from application.admin_panel.models import Users

from werkzeug.security import generate_password_hash,check_password_hash

db.create_all()



if __name__ == '__main__':
    app.run()