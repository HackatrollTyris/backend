from flask import Flask
from methods import *

app = Flask(__name__)

@app.route("/shop_ids")
def get_shops():
    return get_shops_ids()

