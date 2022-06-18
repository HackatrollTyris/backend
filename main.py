from crypt import methods
from flask import Flask
from flask import request
from methods import *
from voronoi import *

app = Flask(__name__)

@app.route("/shop_ids", methods=['GET'])
def get_shops():
    return get_shops_ids()

@app.route("/get_best_location", methods=['GET'])
def get_best_shop_location():
    data = request.get_json()
    id = data['id']
    shops = get_shops_coordinates_by_id(id)
    best_point = get_furthest_point()
    
