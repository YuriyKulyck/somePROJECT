from flask import *

import DBmanager
from DBmanager import DBManager
app = Flask(__name__)

app.secret_key = "9919"
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/products_by_catagory/<id_category>")
def product(id_category):
    dbmanager = DBmanager.DBManager("db_name.sql")
    articles = dbmanager.get_products_by_catalog(id_category)
    return render_template("product.html", items=articles)
@app.route("/product_page/<item_id>")
def product_page(item_id):
    dbmanager = DBmanager.DBManager("db_name.sql")
    article = dbmanager.get_products_by_id(item_id)
    return render_template("product_page.html",article=article)
app.run()