import sys
import heapq
from utils.distance import haversine_distance

def best_first_search(start, goal, adjacencies, coordinates):
    """
    Perform a best-first search from start to goal using the straight-line distance heuristic.

    :param start: The starting city (string)
    :param goal: The destination city (string)
    :param adjacencies: A dictionary representing the adjacency list of cities
    :param coordinates: A dictionary with city coordinates (lat, lon)
    :return: A list representing the path from start to goal, or None if no path is found
    """
    # Priority queue for paths to explore (priority, path)
    queue = [(0, [start])]  # Initial path with heuristic value 0
    visited = set([start])  # Set to track visited cities

    while queue:
        # Get the path with the lowest heuristic value
        _, path = heapq.heappop(queue)
        current_city = path[-1]

        # If we've reached the goal, return the path
        if current_city == goal:
            print(f"\nMemory used for visited set: {sys.getsizeof(visited)} bytes")
            print(f"Memory used for priority queue: {sys.getsizeof(queue)} bytes")
            return path

        # Explore neighbors
        for neighbor in adjacencies.get(current_city, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                priority = haversine_distance(neighbor, goal, coordinates)
                heapq.heappush(queue, (priority, new_path))

    # Return None if no path is found
    return None
