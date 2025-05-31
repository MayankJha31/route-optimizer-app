from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from utils.distance import compute_distance_matrix
import pandas as pd

def solve_tsp(df: pd.DataFrame, warehouse: dict):
    """
    Solves the TSP for a group of customers + warehouse.
    Returns the ordered list of stops and total distance.
    """
    locations = [(warehouse['lat'], warehouse['lon'])] + list(zip(df['Latitude'], df['Longitude']))
    distance_matrix = compute_distance_matrix(locations)

    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_idx, to_idx):
        return int(distance_matrix[manager.IndexToNode(from_idx)][manager.IndexToNode(to_idx)] * 1000)

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_params = pywrapcp.DefaultRoutingSearchParameters()
    search_params.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    solution = routing.SolveWithParameters(search_params)

    route = []
    total_distance = 0
    if solution:
        index = routing.Start(0)
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            lat, lon = locations[node_index]
            route.append({'lat': lat, 'lon': lon})
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            total_distance += distance_callback(previous_index, index) / 1000.0
        # Append warehouse again at end
        route.append({'lat': warehouse['lat'], 'lon': warehouse['lon']})
    return route, total_distance
