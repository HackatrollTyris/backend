import pyproj
import math


def XY_To_LatLon(x,y):
    P = pyproj.Proj(proj='utm', zone=30, ellps='WGS84', preserve_units=True)
    G = pyproj.Geod(ellps='WGS84')
    
    (lat, lon) = P(x,y,inverse=True)    
    return (lon, lat)


