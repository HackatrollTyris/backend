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



def load_equipamientos_municipales(path: str =  "./data/EquipamientosMunicipales.csv") -> pd.DataFrame:
    """Carga los datos de negocios en barrios y devuelve el df.
    Convierte las coordenadas a lat/long

    Args:
        path (str, optional): _description_. Defaults to "./data/EquipamientosMunicipales.csv".

    Returns:
        pd.DataFrame: _description_
    """
    df = pd.read_csv(path)
    df = df[["X","Y","equipamien","idclase"]]
    # df[["X","Y"]].apply(lambda x: print(x[0],x[1]),axis=1)
    coordenadas = df[["X","Y"]].apply(lambda x: XY_To_LatLon(x[0],x[1]),axis=1)
    x = [c[0] for c in coordenadas]
    y = [c[1] for c in coordenadas]
    df["X"]=x
    df["Y"]=y
    return df
    
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
