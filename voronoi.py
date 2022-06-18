from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np
import math


def get_voronoi_intersections(points: np.array) -> list:
    """Obtiene los puntos de intersección de un diagrama de Voronoi
    sobre los puntos dados.

    Args:
        points (np.array): _description_

    Returns:
        np.array: _description_
    """
    vor = Voronoi(points)
    return vor.vertices

def get_furthest_point(points: np.array) -> tuple:
    """Encuentra el punto más distante a los dados en base
    al diagrama de Voronoi de éstos.

    Args:
        points (np.array): _description_

    Raises:
        ValueError: _description_

    Returns:
        tuple: _description_
    """
    if len(points>2):
        raise ValueError("Mínimo dos valores.")
    voronoi_intersections = get_voronoi_intersections(points)
    total_distances = []
    for vi in voronoi_intersections:
        total_distance = 0
        for point in points:
            total_distance+=math.dist(vi,point)
        total_distances.append(total_distance)
    idx = total_distances.index(min(total_distances))
    return voronoi_intersections[idx]

# points = np.array([[0,0],[0,1]])
# print(get_furthest_point(points))