from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user_sql_tutorial:admin@localhost/sql_tutorial'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Aisle(db.Model):
    __tablename__ = 'tbl_aisle'
    aisle_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    aisle_name = db.Column(db.String(200), unique=True)

    def __init__(self, customer, dealer, rating, comments):
        self.aisle_id = aisle_id
        self.aisle_name = aisle_name

class Department(db.Model):
    __tablename__ = 'tbl_department'
    department_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    department_name = db.Column(db.String(200), unique=True)

    def __init__(self, customer, dealer, rating, comments):
        self.department_id = department_id
        self.department_name = department_name

class OrderProduct(db.Model):
    __tablename__ = 'tbl_order_product'
    order_product_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    order_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    add_to_cart_order = db.Column(db.Integer)
    reordered = db.Column(db.Integer)

    def __init__(self, customer, dealer, rating, comments):
        self.order_product_id = order_product_id
        self.order_id = order_id
        self.product_id = product_id
        self.add_to_cart_order = add_to_cart_order
        self.reordered = reordered

class Order(db.Model):
    __tablename__ = 'tbl_order'
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    user_id = db.Column(db.Integer)
    eval_set = db.Column(db.Integer)
    order_number = db.Column(db.Integer)
    order_dow = db.Column(db.Integer)
    order_hour_of_day = db.Column(db.Integer)
    days_since_prior_order = db.Column(db.Integer)

    def __init__(self, customer, dealer, rating, comments):
        self.order_id = order_id
        self.user_id = user_id
        self.eval_set = eval_set
        self.order_number = order_number
        self.order_dow = order_dow
        self.order_hour_of_day = order_hour_of_day
        self.days_since_prior_order = days_since_prior_order

class Product(db.Model):
    __tablename__ = 'tbl_product'
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    product_name = db.Column(db.String(200), unique=True)
    aisle_id = db.Column(db.Integer)
    department_id = db.Column(db.Integer)

    def __init__(self, customer, dealer, rating, comments):
        self.product_id = product_id
        self.product_name = product_name
        self.aisle_id = aisle_id
        self.department_id = department_id