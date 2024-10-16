import time
import os
from algorithms.breadth_first_search import bfs
from algorithms.depth_first_search import dfs
from algorithms.iddfs_search import iddfs
from algorithms.best_first_search import best_first_search
from algorithms.a_star_search import a_star_search
from utils.distance import haversine_distance
from utils.load_data import load_coordinates, load_adjacencies
from utils.distance import haversine_distance

def calculate_total_distance(route, coordinates):
    total_distance = 0
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        total_distance += haversine_distance(city1, city2, coordinates)
    return total_distance

def get_valid_city_input(coordinates):
    """
    Keep asking the user to enter valid start and goal cities
    until both are found in the coordinates database.
    """
    while True:
        start = input("Enter the starting city: ")
        goal = input("Enter the destination city: ")
        if start not in coordinates:
            print(f"'{start}' is not in the database. Please enter a valid city.")
        elif goal not in coordinates:
            print(f"'{goal}' is not in the database. Please enter a valid city.")
        else:
            return start, goal


def main():
    # Load the cities and adjacencies
    script_dir = os.path.dirname(os.path.abspath(__file__))
    coordinates_file = os.path.join(script_dir, 'data', 'coordinates.csv')
    adjacencies_file = os.path.join(script_dir, 'data', 'Adjacencies.txt')
    
    coordinates = load_coordinates(coordinates_file)
    adjacencies = load_adjacencies(adjacencies_file)

    start, goal = get_valid_city_input(coordinates)

    while True:

        print("Select search method:")
        print("1. Breadth-First Search")
        print("2. Depth-First Search")
        print("3. ID-DFS Search")
        print("4. Best-First Search")
        print("5. A* Search")
        
        method = input("Enter the number of your choice: ")

        if method == '1':
            start_time = time.time()
            route = bfs(start, goal, adjacencies)
            end_time = time.time()
        elif method == '2':
            start_time = time.time()
            route = dfs(start, goal, adjacencies)
            end_time = time.time()
        elif method == '3':
            start_time = time.time()
            route = iddfs(start, goal, adjacencies)
            end_time = time.time()
        elif method == '4':
            start_time = time.time()
            route = best_first_search(start, goal, adjacencies, coordinates)
            end_time = time.time()
        elif method == '5':
            start_time = time.time()
            route = a_star_search(start, goal, adjacencies, coordinates)
            end_time = time.time()

            
        else:
            print("Invalid method selected.")
            continue
        
        # Display results
        if route:
            print("\nRoute found:", ' -> '.join(route))
            total_distance = calculate_total_distance(route, coordinates)
            print(f"\nTotal distance: {total_distance:.2f} kilometers")
            print(f"Time taken: {end_time - start_time:.4f} seconds\n")
        else:
            print("No route found.")
        
        # Return to the search method selection if desired
        another = input("Do you want to try another search method? (y/n): ")
        if another.lower() != 'y':
            change_cities = input("Do you want to change cities? (y/n): ")
            if change_cities.lower() == 'y':
                start, goal = get_valid_city_input(coordinates)
            else:
                break

if __name__ == "__main__":
    main()
