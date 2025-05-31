from geopy.distance import geodesic

def compute_distance_matrix(locations):
    """
    Compute a distance matrix between all locations using geodesic (Haversine) distance.
    :param locations: List of (latitude, longitude) tuples
    :return: 2D list representing distance matrix
    """
    distance_matrix = []
    for from_loc in locations:
        row = []
        for to_loc in locations:
            distance = geodesic(from_loc, to_loc).km
            row.append(distance)
        distance_matrix.append(row)
    return distance_matrix
