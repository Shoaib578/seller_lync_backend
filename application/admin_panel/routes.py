from flask import Blueprint,jsonify,request
from application import db,app
from werkzeug.security import generate_password_hash,check_password_hash
from application.admin_panel.models import Users,Vendors,Vendor_Categories,UsersSchema,Vendor_CategoriesSchema,VendorsSchema
import os
from sqlalchemy import text
from datetime import datetime
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash,check_password_hash
import random

admin = Blueprint('admin', __name__,static_folder='../static')

n = random.randint(0,1000)


def save_file(file, type):
    file_name = secure_filename(str(n)+file.filename)
    file_ext = file_name.split(".")[1]
    folder = os.path.join(app.root_path, "static/" + type + "/")
    file_path = os.path.join(folder, file_name)
    try:
        file.save(file_path)
        return True, file_name
    except:
        return False, file_name




def remove_file(file, type):
    file_name = file
    folder = os.path.join(app.root_path, "static/" + type + "/"+file_name)
    os.remove(folder)
    return 'File Has Been Removed'


@admin.route('/login', methods=['POST'])
def Login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    user= Users.query.filter_by(email=email).first()
    
    if user and check_password_hash(user.password,password):
        user_schema = UsersSchema()
        user = user_schema.dump(user)
        return jsonify({'msg':'you are successfully logged in','user':user})
    else:
        return jsonify({'msg':'Wrong Email or Password'})




@admin.route('/register',methods=['POST'])
def Register():
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    phone_no = request.form.get('phone_no')
    zipcode_or_cityname = request.form.get('zipcode_or_cityname')

    hash_password = generate_password_hash(password)
    email_exists = Users.query.filter_by(email=email).first()

    if email_exists:
        return jsonify({'msg':'Email Already Exists Try Another One'})
    else:
        user = Users(email=email,password=hash_password,name=name,phone_no=phone_no,user_zipcode_or_cityname=zipcode_or_cityname,is_admin=0)
        db.session.add(user)
        db.session.commit()
        return jsonify({'msg':'You are Successfully Registered'})
        

@admin.route('/forgot_password',methods=['POST'])
def ForgotPassword():
    check_email = request.form.get('check_email')
    check_password = request.form.get('check_password')
    email = request.form.get('email')
    

    if check_email == 'true' and check_password != 'true':
        
        email_exists = Users.query.filter_by(email=email).first()
        if email_exists:
            return jsonify({'msg':'found'})
        else:
            return jsonify({'msg':'Wrong Email Try Again'})

    elif check_password == 'true' and check_email != 'true':
            password = request.form.get('password')
            email_exists = Users.query.filter_by(email=email).first()
            hash_password = generate_password_hash(password)
            email_exists.password = hash_password
            db.session.commit()
            return jsonify({'msg':'Your Password Sucessfully Reset'})
                


    
@admin.route('/add_vendorcategory',methods=['POST'])
def AddVendorCategory():
    vendor_category_name = request.form.get('vendor_category_name')
    vendor_category_image = request.files.get('vendor_category_image')
    
    category = Vendor_Categories(category=vendor_category_name,picture=str(n)+vendor_category_image.filename)
    save_file(vendor_category_image,'category_images')
    db.session.add(category)
    db.session.commit()
    return jsonify({'msg':'Category Added'})

@admin.route('/get_all_categories')
def Get_AllVendor_Categories():
    get_categories = Vendor_Categories.query.all()
    vendor_categories_schema = Vendor_CategoriesSchema(many=True)
    all_categories =vendor_categories_schema.dump(get_categories)
    return jsonify({'all_categories':all_categories})


@admin.route('/delete_category')
def Delete_Category():
    category_id = request.args.get('category_id')
    category = Vendor_Categories.query.filter_by(vendor_category_id=category_id).first()

    remove_file(category.picture,'category_images')
    db.session.delete(category)
    db.session.commit()
    return jsonify({'msg':'Category Has Been Deleted'})







@admin.route('/add_vendor',methods=['POST'])
def AddVendor():
    zipcode = request.form.get('zipcode')
    city_name = request.form.get('city_name')
    name = request.form.get('name')
    vendor_category = request.form.get('vendor_category')
    phone_no = request.form.get('phone_no')
    price = request.form.get('price')
    
    vendor = Vendors(name=name, city_name=city_name,vendor_zip_code=zipcode,phone_no=phone_no,price=price,vendor_category=vendor_category)
    db.session.add(vendor)
    db.session.commit()
    return jsonify({'msg':'Vendor Has Been Added'})


@admin.route('/all_vendors')
def AllVendors():
    all_vendors_sql = text("SELECT * FROM vendors LEFT JOIN vendor__categories on vendor__categories.vendor_category_id=vendors.vendor_category")
    all_vendors_query = db.engine.execute(all_vendors_sql)
    vendors_schema = VendorsSchema(many=True)
    all_vendors = vendors_schema.dump(all_vendors_query)
    return jsonify({'all_vendors':all_vendors})

@admin.route('/delete_vendor')
def Delete_Vendor():
    vendor_id = request.args.get('vendor_id')
    
    vendor = Vendors.query.filter_by(vendor_id=vendor_id).first()
    
    db.session.delete(vendor)
    db.session.commit()
    return jsonify({'msg':'Vendor Has Been Deleted'})



@admin.route('/get_allusers')
def GetAll_Users():
    all_users = Users.query.filter_by(is_admin=0).all()
    users_schema = UsersSchema(many=True)
    users = users_schema.dump(all_users)
    return jsonify({'all_users':users})


@admin.route('/delete_user')
def DeleteUser():
    user_id = request.args.get('user_id')
    user = Users.query.filter_by(user_id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({'msg':'User Has Been Deleted'})
