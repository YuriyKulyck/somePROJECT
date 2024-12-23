from flask import *

from DBmanager import DBManager
app = Flask(__name__)

app.secret_key = "9919"
@app.route("/")
def index():

    return render_template("index.html")
app.run()