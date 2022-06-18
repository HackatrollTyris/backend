import string
import pyproj
import requests
import pandas as pd
import json
from scipy.spatial import Voronoi, voronoi_plot_2d
import ast
from voronoi import *


def XY_To_LatLon(x,y):
    P = pyproj.Proj(proj='utm', zone=30, ellps='WGS84', preserve_units=True)
    G = pyproj.Geod(ellps='WGS84')

    (lat, lon) = P(x,y,inverse=True)    
    return (lat, lon)

def get_shops() -> None:
    """
    Carga los datos de las tiendas disponibles de la API
    """
    shops_pd = pd.DataFrame(columns=['shop_id', 'name', 'class_id', 'coordinates'])
    open_data_url = 'https://geoportal.valencia.es/apps/OpenData/SociedadBienestar/v_infociudad.json'
    resp = requests.get(url = open_data_url)
    data = resp.json()
    for shop in data['features']:
        try:
            shop_id = shop['properties']['objectid']
            name = shop['properties']['equipamien']
            class_id = shop['properties']['idclase']
            coordinates = shop['geometry']['coordinates']
            
            shops_pd = shops_pd.append({'shop_id' : shop_id,
                                                'class_id' : class_id,
                                                'name' : name, 
                                                'coordinates' : coordinates}, ignore_index=True)
        except:
            # Algunos de los locales no tiene coordenadas por lo que si salta error se pasa al siguiente dato
            continue
        
    shops_pd.to_csv('data/shops.csv', index=False)
    
def get_districts() -> None:
    """
    Carga los datos de los barrios y guarda el df como csv en la carpeta data
    """
    districts_pd = pd.DataFrame(columns=['district_id', 'name', 'coordinates'])
    open_data_url = 'https://geoportal.valencia.es/apps/OpenData/UrbanismoEInfraestructuras/DISTRITOS.json'
    resp = requests.get(url = open_data_url)
    data = resp.json()
    for district in data['features']:
        name = district['properties']['nombre']
        district_id = district['properties']['coddistrit']
        coordinates = district['geometry']['coordinates']
        districts_pd = districts_pd.append({'district_id' : district_id, 
                                            'name' : name, 
                                            'coordinates' : coordinates[0]}, ignore_index=True)
    
    districts_pd.to_csv('csv/districts.csv', index=False)

def get_shops_ids() -> json :
    f = open('shops.json')
    ids = json.load(f)
    return ids


def get_shops_coordinates_by_id(id: string) -> pd.DataFrame:
    shops = pd.read_csv('data/shops.csv')
    shops_filtered = shops.loc[shops['class_id'] == int(id)]['coordinates']
    shops_filtered = shops_filtered.apply(eval)
    return shops_filtered.to_list()

# id = 1
# shops = get_shops_coordinates_by_id(id)
# # print(shops)
# # shops = np.array([[-1,2],[3,-15.4],[3.2,2],[1,5]])
# best_point = get_furthest_point(shops)
# print(best_point)