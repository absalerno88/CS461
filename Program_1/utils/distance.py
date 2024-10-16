from math import radians, sin, cos, sqrt, atan2

def haversine_distance(city1, city2, cities):
    """
    Calculate the Haversine distance between two cities using their coordinates.
    """
    R = 6371  # Radius of the Earth in kilometers
    lat1, lon1 = cities[city1]
    lat2, lon2 = cities[city2]

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c
