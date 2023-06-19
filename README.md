# Hybrid Dragonfly Algorithm for Traveling Salesman Problem (TSP)

## Hybrid Dragonfly Algorithm
The Hybrid Dragonfly Algorithm is a metaheuristic optimization algorithm inspired by the behavior of dragonflies. It combines the exploration capabilities of the Dragonfly Algorithm with the local search improvement of the 2-opt algorithm to solve combinatorial optimization problems such as the Traveling Salesman Problem (TSP).

## Dragonfly Algorithm:
The Dragonfly Algorithm is a swarm-based optimization algorithm that simulates the collective behavior of dragonflies in nature. It consists of a population of dragonflies that move and interact with each other to search for an optimal solution. Dragonflies communicate through attractive and repulsive forces, which guide their movements towards promising regions of the search space.

## 2-opt Local Search:
The 2-opt algorithm is a local search heuristic commonly used to improve solutions for the TSP. It iteratively swaps pairs of edges in the tour to eliminate crossovers and reduce the total distance. This local search process continues until no further improvements can be made.

## Hybridization:
The Hybrid Dragonfly Algorithm combines the Dragonfly Algorithm's exploration capabilities with the 2-opt local search's exploitation capabilities. It utilizes the local search mechanism to refine the solutions obtained during the exploration phase. By incorporating both global exploration and local exploitation, the algorithm aims to strike a balance between exploration and exploitation to find high-quality solutions efficiently.

## Algorithm Steps:

1. Distance Matrix Generation: A distance matrix is generated that represents the distances between cities in the TSP problem. In this implementation, random distances within a specified range are used.

2. Total Distance Calculation: The total distance of a tour is calculated based on the distance matrix. It sums the distances between consecutive cities and adds the distance from the last city back to the starting city.

3. 2-opt Local Search: The 2-opt local search is applied to each dragonfly's tour to improve its quality. The algorithm iteratively swaps pairs of edges in the tour to reduce the total distance until no further improvement can be made.

4. Dragonfly Movements: Dragonfly movements are performed to explore the solution space. Each dragonfly attempts two random swaps in its tour. If the resulting tour has a lower total distance than the original tour, it is accepted as the new tour.

5. Best Tour Update: The best tour and its corresponding cost are updated whenever a better solution is found. The best tour represents the overall best solution found so far.

6. Iteration Loop: The above steps are repeated for a specified number of iterations to iteratively improve the solutions and explore the search space.

The Hybrid Dragonfly Algorithm offers a trade-off between global exploration and local exploitation, allowing it to efficiently explore the search space while refining solutions using the 2-opt local search. This combination makes it effective in finding near-optimal or optimal solutions for the Traveling Salesman Problem and other similar combinatorial optimization problems.

## View the output
```python
Best tour: [4, 0, 8, 7, 2, 3, 5, 9, 1, 6]
Cost: 129.5455546492563
```
