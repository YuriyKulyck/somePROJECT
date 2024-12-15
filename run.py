from flask import *

from DBmanager import DBManager
app = Flask(__name__)

app.secret_key = "123"
@app.route("/")
def index():
    db_manager = DBManager()
    return render_template("index.html")
app.run()