from flask import *

import DBmanager
from DBmanager import DBManager
app = Flask(__name__)

app.secret_key = "9919"
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about_us")
def about_us():
    return render_template("about_us.html")
@app.route("/confidence")
def confidence():
    return render_template("confidence.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/register")
def register():
    return render_template("register.html")
@app.route("/profile")
def profile():
    return render_template("profile.html")
@app.route('/cart')
def cart():
    return render_template("cart.html")
@app.route("/products_by_catagory/<id_category>")
def product(id_category):
    dbmanager = DBmanager.DBManager("db_name.sql")
    articles = dbmanager.get_products_by_catalog(id_category)
    return render_template("product.html", items=articles)
@app.route("/product_page/<item_id>")
def product_page(item_id):
    dbmanager = DBmanager.DBManager("db_name.sql")
    article = dbmanager.get_products_by_id(item_id)
    is_registered = True
    return render_template("product_page.html",article=article, is_registered=is_registered)
app.run()