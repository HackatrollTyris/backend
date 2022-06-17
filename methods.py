import pyproj
import math
import pandas as pd
import requests
import json


def XY_To_LatLon(x,y):
    P = pyproj.Proj(proj='utm', zone=30, ellps='WGS84', preserve_units=True)
    G = pyproj.Geod(ellps='WGS84')

    (lat, lon) = P(x,y,inverse=True)    
    return (lat, lon)



def load_data_barrios(path: str =  "./data/EquipamientosMunicipales.csv") -> pd.DataFrame:
    """Carga los datos de negocios en barrios y devuelve el df.

    Args:
        path (str, optional): _description_. Defaults to "./data/EquipamientosMunicipales.csv".

    Returns:
        pd.DataFrame: _description_
    """
    df = pd.read_csv(path)
    df = df[["X","Y","equipamien","idclase"]]
    return df

