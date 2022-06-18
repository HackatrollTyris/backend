import pyproj
import math
import requests
import json
import pandas as pd


def XY_To_LatLon(x,y):
    P = pyproj.Proj(proj='utm', zone=30, ellps='WGS84', preserve_units=True)
    G = pyproj.Geod(ellps='WGS84')

    (lat, lon) = P(x,y,inverse=True)    
    return (lat, lon)

def getDistricts():
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
    


getDistricts()