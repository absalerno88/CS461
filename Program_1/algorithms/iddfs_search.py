import sys

def depth_limited_search(start, goal, adjacencies, limit):
    """
    Perform a depth-limited search (DFS with depth limit).

    :param start: The starting city (string)
    :param goal: The destination city (string)
    :param adjacencies: A dictionary representing the adjacency list of cities
    :param limit: The current depth limit
    :return: A list representing the path from start to goal, or None if no path is found within the limit
    """
    # Stack for storing paths (LIFO)
    stack = [(start, [start], 0)]  # (city, path, depth)
    
    # Set to keep track of visited nodes
    visited = set([start])

    while stack:
        city, path, depth = stack.pop()

        # If we've reached the goal, return the path
        if city == goal:
            print(f"\nMemory used for visited set: {sys.getsizeof(visited)} bytes")
            print(f"Memory used for stack: {sys.getsizeof(stack)} bytes")
            return path

        # Only proceed if we're within the depth limit
        if depth < limit:
            for neighbor in adjacencies.get(city, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, path + [neighbor], depth + 1))

    return None  # No path found within the depth limit

def iddfs(start, goal, adjacencies):
    """
    Perform iterative deepening depth-first search from start to goal.

    :param start: The starting city (string)
    :param goal: The destination city (string)
    :param adjacencies: A dictionary representing the adjacency list of cities
    :return: A list representing the path from start to goal, or None if no path is found
    """
    depth = 0
    while True:
        print(f"Searching with depth limit: {depth}")
        result = depth_limited_search(start, goal, adjacencies, depth)
        if result is not None:
            return result
        depth += 1  # Increase depth limit and search again
