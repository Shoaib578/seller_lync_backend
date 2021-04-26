
from application.admin_panel.models import Users
import os
from werkzeug.security import generate_password_hash,check_password_hash

print(os.getenv('admin_gmail'))
admin_user = Users.query.filter_by(is_admin=1)
if admin_user.count() == 0:
    psw = generate_password_hash(os.getenv('admin_password'))
    admin = Users(name='Admin',email=os.getenv('admin_gmail'),password=psw,phone_no='0333434',is_admin=1,user_cityname='india')
    db.session.add(admin)
    db.session.commit()
else:
    pass



