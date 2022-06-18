from crypt import methods
from flask import Flask
from methods import *

app = Flask(__name__)

@app.route("/shop_ids", methods=['GET'])
def get_shops():
    return get_shops_ids()

