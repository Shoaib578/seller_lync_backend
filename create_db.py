from application import db
from application.admin_panel.models import Users

from werkzeug.security import generate_password_hash,check_password_hash
db.create_all()


admin_user = Users.query.filter_by(is_admin=1)
if admin_user.count() == 0:
    psw = generate_password_hash('admin2589')
    admin = Users(name='Admin',email='theadmin287@gmail.com',password=psw,phone_no='0333434',is_admin=1,user_cityname='india')
    db.session.add(admin)
    db.session.commit()
else:
    pass

