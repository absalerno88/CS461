import csv

# Load cities with their coordinates (latitude, longitude)
def load_coordinates(file_name):
    coordinates = {}
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            city_name = row[0]
            lat, lon = float(row[1]), float(row[2])
            coordinates[city_name] = (lat, lon)
    return coordinates

# Load adjacency list from the text file
def load_adjacencies(file_name):
    adjacencies = {}
    with open(file_name, 'r') as file:
        for line in file:
            city_a, city_b = line.strip().split()
            adjacencies.setdefault(city_a, []).append(city_b)
            adjacencies.setdefault(city_b, []).append(city_a)  # Ensure symmetry
    return adjacencies
