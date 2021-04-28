from application import db
from marshmallow_sqlalchemy import ModelSchema


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(200),nullable=False)
    password = db.Column(db.String(200),nullable=False)
    phone_no = db.Column(db.String(200),nullable=False)
    
    user_cityname = db.Column(db.String(200),nullable=False)
    is_admin = db.Column(db.Integer(),nullable=False)
class UsersSchema(ModelSchema):
    class Meta:
        fields = ('user_id','name','email','password','phone_no','user_cityname','is_admin')

class Vendor_Categories(db.Model):
    vendor_category_id = db.Column(db.Integer, primary_key=True)
    picture = db.Column(db.String(300))
    category = db.Column(db.String(300))

class Vendor_CategoriesSchema(ModelSchema):
    class Meta:
        fields = ('vendor_category_id','picture','category','vendors_count','home_page_vendors_count','vendor_id','name','vendor_category','password','phone_no','user_cityname','price','category','search_page_vendors_count')
    



class Vendors(db.Model):
    vendor_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    

    phone_no = db.Column(db.String(200),nullable=False)
    vendor_city_name = db.Column(db.String(200),nullable=False)
    vendor_category = db.Column(db.Integer(),nullable=False)
    price = db.Column(db.String(200),nullable=False)

class VendorsSchema(ModelSchema):
    class Meta:
        fields = ('vendor_id','name','vendor_category','password','phone_no','vendor_city_name','price','category','vendor_category_id','picture','category','user_cityname')





class Cities(db.Model):
    city_id = db.Column(db.Integer(),primary_key=True)
    city = db.Column(db.String(200))
    province = db.Column(db.String(200))
    district = db.Column(db.String(200))

class Cities_Schema(ModelSchema):
    class Meta:
        fields =('city_id','city','province','district')
