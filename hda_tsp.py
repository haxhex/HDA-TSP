import random
import numpy as np

import matplotlib.pyplot as plt

# Generate coordinates for each city
def generate_city_coordinates(num_cities):
    coordinates = []
    for _ in range(num_cities):
        x, y = random.uniform(0, 100), random.uniform(0, 100)
        coordinates.append((x, y))
    return coordinates

# Generate the distance matrix for TSP problem using coordinates
def generate_distance_matrix(coordinates):
    num_cities = len(coordinates)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = np.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance
    return distance_matrix

# Calculate the total distance of a tour
def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    num_cities = len(tour)
    for i in range(num_cities - 1):
        current_city = tour[i]
        next_city = tour[i + 1]
        total_distance += distance_matrix[current_city][next_city]
    total_distance += distance_matrix[tour[-1]][tour[0]]  # Return to the starting city
    return total_distance

# 2-opt local search to improve solutions
def two_opt_local_search(tour, distance_matrix):
    num_cities = len(tour)
    best_tour = tour.copy()
    best_cost = calculate_total_distance(tour, distance_matrix)

    improved = True
    while improved:
        improved = False
        for i in range(1, num_cities - 1):
            for j in range(i + 1, num_cities):
                if j - i == 1:
                    continue
                new_tour = best_tour[:i] + best_tour[i:j][::-1] + best_tour[j:]
                new_cost = calculate_total_distance(new_tour, distance_matrix)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour
                    improved = True
    return best_tour

# Perform dragonfly movements
def dragonfly_movement(tour, best_tour, distance_matrix):
    num_cities = len(tour)
    new_tour = tour.copy()
    for _ in range(2):  # Try two random swaps
        i, j = random.sample(range(num_cities), 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    if calculate_total_distance(new_tour, distance_matrix) < calculate_total_distance(tour, distance_matrix):
        return new_tour  # Accept the new tour if its cost is lower
    return tour  # Otherwise, return the original tour

# Perform dragonfly movements
def hybrid_dragonfly_algorithm(num_dragonflies, num_cities, num_iterations):
    # Generate the city coordinates
    coordinates = generate_city_coordinates(num_cities)

    # Generate the distance matrix
    distance_matrix = generate_distance_matrix(coordinates)

    # Initialize the dragonflies population
    population = []
    for _ in range(num_dragonflies):
        tour = random.sample(range(num_cities), num_cities)
        population.append(tour)

    # Initialize the best tour and its cost
    best_tour = population[0]
    best_cost = calculate_total_distance(best_tour, distance_matrix)

    # Perform iterations
    for iteration in range(num_iterations):
        # Perform local search on a subset of dragonflies
        for i in range(num_dragonflies):
            population[i] = two_opt_local_search(population[i], distance_matrix)

        # Perform dragonfly movements
        for i in range(num_dragonflies):
            population[i] = dragonfly_movement(population[i], best_tour, distance_matrix)

        # Update the best tour if a better solution is found
        for tour in population:
            cost = calculate_total_distance(tour, distance_matrix)
            if cost < best_cost:
                best_tour = tour
                best_cost = cost

    return best_tour, best_cost

def plot_tour(coordinates, best_tour):
    x = [coordinates[i][0] for i in best_tour] + [coordinates[best_tour[0]][0]]
    y = [coordinates[i][1] for i in best_tour] + [coordinates[best_tour[0]][1]]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, '-o', color='blue', linewidth=1, markersize=5)
    plt.ylabel('Y-Coordinates')
    plt.xlabel('X-Coordinates')
    plt.title('Best TSP Tour')
    plt.grid()
    plt.show()

# Example usage
num_cities = 10

# Generate city coordinates
coordinates = generate_city_coordinates(num_cities)

# Generate distance matrix using coordinates
distance_matrix = generate_distance_matrix(coordinates)

num_iterations = 1000
best_tour, best_cost = hybrid_dragonfly_algorithm(100, num_cities, num_iterations)

print("Best tour:", best_tour)
print("Cost:", best_cost)

# Plot the best tour
# plot_tour(coordinates, best_tour)