import sys

def dfs(start, goal, adjacencies):
    """
    Perform a depth-first search from start to goal in the adjacency list.

    :param start: The starting city (string)
    :param goal: The destination city (string)
    :param adjacencies: A dictionary representing the adjacency list of cities
    :return: A list representing the path from start to goal, or None if no path is found
    """
    # Stack for storing paths (LIFO)
    stack = [[start]]
    
    # Set to keep track of visited nodes
    visited = set([start])

    while stack:
        # Get the last path from the stack
        path = stack.pop()

        # Get the last city in the path
        city = path[-1]

        # If we've reached the goal, return the path
        if city == goal:
            print(f"\nMemory used for visited set: {sys.getsizeof(visited)} bytes")
            print(f"Memory used for queue: {sys.getsizeof(stack)} bytes")
            return path

        # Otherwise, explore the neighbors
        for neighbor in adjacencies.get(city, []):
            if neighbor not in visited:
                # Mark the neighbor as visited
                visited.add(neighbor)

                # Add the new path to the stack
                stack.append(path + [neighbor])

    # Return None if no path is found
    return None
