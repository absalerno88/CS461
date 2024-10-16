import sys
import heapq
from utils.distance import haversine_distance

def a_star_search(start, goal, adjacencies, coordinates):
    """
    Perform an A* search from start to goal using the straight-line distance heuristic.

    :param start: The starting city (string)
    :param goal: The destination city (string)
    :param adjacencies: A dictionary representing the adjacency list of cities
    :param coordinates: A dictionary with city coordinates (lat, lon)
    :return: A list representing the path from start to goal, or None if no path is found
    """
    # Priority queue for paths to explore (priority, path, cost-so-far)
    queue = [(0, [start], 0)]  # (f(n), path, g(n))
    visited = {start: 0}  # Track the best cost to reach each city

    while queue:
        # Get the path with the lowest f(n)
        _, path, g_cost = heapq.heappop(queue)
        current_city = path[-1]

        # If we've reached the goal, return the path
        if current_city == goal:
            print(f"\nMemory used for visited set: {sys.getsizeof(visited)} bytes")
            print(f"Memory used for visited set: {sys.getsizeof(queue)} bytes")
            return path

        # Explore neighbors
        for neighbor in adjacencies.get(current_city, []):
            # Calculate the g(n) for reaching the neighbor
            new_g_cost = g_cost + haversine_distance(current_city, neighbor, coordinates)

            # If this path to neighbor is better (lower cost) than any previous one
            if neighbor not in visited or new_g_cost < visited[neighbor]:
                visited[neighbor] = new_g_cost
                f_cost = new_g_cost + haversine_distance(neighbor, goal, coordinates)
                heapq.heappush(queue, (f_cost, path + [neighbor], new_g_cost))

    # Return None if no path is found
    return None
