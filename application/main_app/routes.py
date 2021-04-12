from flask import Blueprint,jsonify,request
from application import db,app
from werkzeug.security import generate_password_hash,check_password_hash
from application.admin_panel.models import Vendors,Vendor_Categories,Vendor_CategoriesSchema,VendorsSchema
import os
from sqlalchemy import text
from datetime import datetime
from werkzeug.utils import secure_filename


main = Blueprint('main', __name__,static_folder='../static')


@main.route('/get_all_categories_for_normal_users')
def GetAllCategoriesForNormalUsers():
    user_default_location = request.args.get('user_default_location')
    if type(user_default_location) == str:
        user_default_location = user_default_location.lower()
    else:
        pass

    get_categories_sql = text("SELECT *,(SELECT count(*) FROM vendors WHERE  vendor_zip_code='"+str(user_default_location)+"' OR city_name ='"+str(user_default_location)+"' AND vendor_category=vendor_category_id ) as home_page_vendors_count  from vendor__categories")
    get_categories_query = db.engine.execute(get_categories_sql)
    vendor_categories_schema = Vendor_CategoriesSchema(many=True)
    all_categories =vendor_categories_schema.dump(get_categories_query)
    return jsonify({'all_categories':all_categories})

@main.route('/view_category_by_user_default_location')
def view_category_by_user_default_location():
    category_id = request.args.get('category_id')
    user_default_location = request.args.get('user_default_location')
    
    if type(user_default_location) == str:
        user_default_location = user_default_location.lower()
    else:
        pass

    vendors_sql = text("Select * from vendors WHERE  vendor_zip_code='"+str(user_default_location)+"' OR city_name ='"+str(user_default_location)+"' AND vendor_category="+str(category_id)+"")

    

    vendors_query = db.engine.execute(vendors_sql)
    vendors_schema = VendorsSchema(many=True)
    vendors = vendors_schema.dump(vendors_query)



    category_sql = text("Select *,(SELECT count(*) FROM vendors WHERE  vendor_zip_code='"+str(user_default_location)+"' OR city_name ='"+str(user_default_location)+"' AND vendor_category=vendor_category_id ) as vendors_count from vendor__categories where vendor_category_id="+str(category_id)+"")
    category_query = db.engine.execute(category_sql)
    category_schema = Vendor_CategoriesSchema(many=True)
    category_info = category_schema.dump(category_query)

    return jsonify({'all_vendors':vendors,'category':category_info})



@main.route('/view_vendor')
def ViewVendor():
    vendor_id = request.args.get('vendor_id')
    getting_vendor = Vendors.query.filter_by(vendor_id=vendor_id).first()
    vendor_schema = VendorsSchema()
    vendor = vendor_schema.dump(getting_vendor)
    return jsonify({'vendor':vendor})



@main.route('/get_all_category_by_search')
def GetAllCategoriesBySearch():
    location = request.args.get('location')
    item = request.args.get('item')

    if type(location) == str:
        location = location.lower()
    else:
        pass
    
    get_categories_sql = text("SELECT *,(SELECT count(*) FROM vendors WHERE  vendor_zip_code='"+str(location)+"' OR city_name='"+str(location)+"' AND vendor_category='"+str(item)+"' ) as search_page_vendors_count  from vendor__categories WHERE category ='"+str(item)+"'")
    get_categories_query = db.engine.execute(get_categories_sql)
    vendor_categories_schema = Vendor_CategoriesSchema(many=True)
    all_categories =vendor_categories_schema.dump(get_categories_query)
    
    return jsonify({'all_categories':all_categories})


@main.route('/view_searched_category')
def ViewSearchedCategory():
    location = request.args.get('location')
    category_id = request.args.get('category_id')

    if type(location) == str:
        location = location.lower()
    else:
        pass
    vendors_sql = text("Select * from vendors WHERE  vendor_zip_code='"+str(location)+"' OR city_name='"+str(location)+"' AND vendor_category="+str(category_id)+"")

    

    vendors_query = db.engine.execute(vendors_sql)
    vendors_schema = VendorsSchema(many=True)
    vendors = vendors_schema.dump(vendors_query)



    category_sql = text("Select *,(SELECT count(*) FROM vendors WHERE  vendor_zip_code='"+str(location)+"' OR city_name ='"+str(location)+"' AND vendor_category=vendor_category_id ) as vendors_count from vendor__categories where vendor_category_id="+str(category_id)+"")
    category_query = db.engine.execute(category_sql)
    category_schema = Vendor_CategoriesSchema(many=True)
    category_info = category_schema.dump(category_query)

    return jsonify({'all_vendors':vendors,'category':category_info})


@main.route('/dropdown_vendors')
def dropdown_vendors():
    location = request.args.get('location')
    category_id = request.args.get('category_id')

    if type(location) == str:
        location = location.lower()
    else:
        pass
        
    vendors_sql = text("Select * from vendors WHERE  vendor_zip_code='"+str(location)+"' OR city_name ='"+str(location)+"' AND vendor_category="+str(category_id)+" LIMIT 0, 5")

    

    vendors_query = db.engine.execute(vendors_sql)
    vendors_schema = VendorsSchema(many=True)
    vendors = vendors_schema.dump(vendors_query)
    return jsonify({'all_vendors':vendors})
