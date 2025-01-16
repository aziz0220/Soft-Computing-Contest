import cProfile
import pstats
import io
import math
import random
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from template_code.read_instances import read_instance
from template_code.verify_solution import verify_solution

# Calcul de la distance entre deux nœuds
def calculate_distance(node1, node2):
    return math.sqrt((node1[0] - node2[0])**2 + (node1[1] - node2[1])**2)

# Calcul du coût total d'une solution (routes)
def calculate_total_cost(routes, distance_matrix, node_index_map):
    cost = 0
    for route in routes:
        for i in range(len(route) - 1):  
            cost += distance_matrix[node_index_map[route[i]]][node_index_map[route[i + 1]]]
    return cost

# Création de la solution initiale
def create_initial_solution(demands, capacity):
    routes = []
    current_route = []
    current_load = 0
    for customer, demand in demands.items():
        if current_load + demand > capacity:
            routes.append(current_route)
            current_route = []
            current_load = 0
        current_route.append(customer)
        current_load += demand
    if current_route:
        routes.append(current_route)
    return routes

# Fonction de génération des voisins d'une solution
def neighborhood_solution(routes, demands, capacity):
    new_routes = [route.copy() for route in routes]
    route1, route2 = random.sample(new_routes, 2)  

    if route1 and route2:
        # Sélectionner un nœud dans chaque route
        node1 = random.choice(route1)
        node2 = random.choice(route2)

        # Calculer les charges actuelles des routes
        load_route1 = sum(demands[node] for node in route1)
        load_route2 = sum(demands[node] for node in route2)

        # Charges après l'échange
        load_route1_after = load_route1 - demands[node1] + demands[node2]
        load_route2_after = load_route2 - demands[node2] + demands[node1]

        # Vérifier les contraintes de capacité pour les deux routes
        if load_route1_after <= capacity and load_route2_after <= capacity:
           
            route1.remove(node1)
            route2.remove(node2)
            route1.append(node2)
            route2.append(node1)

    return new_routes

# Recherche Tabou
def tabu_search(node_coords, demands, capacity, max_iterations, tabu_tenure):
    num_nodes = len(node_coords)
    nodes = list(node_coords.keys())  
    
    # Création d'une correspondance entre les identifiants de nœuds et les indices dans la matrice de distances
    node_index_map = {node: idx for idx, node in enumerate(nodes)}
    
    # Création de la matrice de distances basée sur les indices
    distance_matrix = [[calculate_distance(node_coords[nodes[i]], node_coords[nodes[j]]) 
                        for j in range(num_nodes)] 
                       for i in range(num_nodes)]
    
    initial_solution = create_initial_solution(demands, capacity)
    best_solution = initial_solution
    best_cost = calculate_total_cost(best_solution, distance_matrix, node_index_map)
    
    tabu_list = []
    tabu_iterations = {}

    for iteration in range(max_iterations):
        neighborhood = []
        for _ in range(10):
            neighbor = neighborhood_solution(best_solution, demands, capacity)
            neighborhood.append(neighbor)

        best_candidate = None
        best_candidate_cost = float('inf')

        for candidate in neighborhood:
            cost = calculate_total_cost(candidate, distance_matrix, node_index_map)
            if (candidate not in tabu_list or iteration - tabu_iterations.get(tuple(map(tuple, candidate)), 0) > tabu_tenure) and cost < best_candidate_cost:
                best_candidate = candidate
                best_candidate_cost = cost

        if best_candidate_cost < best_cost:
            best_solution = best_candidate
            best_cost = best_candidate_cost

        tabu_list.append(best_candidate)
        tabu_iterations[tuple(map(tuple, best_candidate))] = iteration

        if len(tabu_list) > tabu_tenure:
            tabu_list.pop(0)

    return best_solution, best_cost

# Fonction pour parser le fichier VRP
def parse_vrp_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    node_coords = {}
    demands = {}
    capacity = 0
    section = None

    for line in lines:
        line = line.strip()
        if line.startswith('CAPACITY'):
            capacity = int(line.split(':')[1].strip())
        elif line.startswith('NODE_COORD_SECTION'):
            section = 'NODE_COORD'
        elif line.startswith('DEMAND_SECTION'):
            section = 'DEMAND'
        elif line.startswith('DEPOT_SECTION'):
            section = 'DEPOT'
        elif line == 'EOF':
            break
        elif section == 'NODE_COORD':
            parts = line.split()
            node_coords[int(parts[0])] = (int(parts[1]), int(parts[2]))
        elif section == 'DEMAND':
            parts = line.split()
            demands[int(parts[0])] = int(parts[1])

    return node_coords, demands, capacity
# Fonction d'affichage de la solution dans le format désiré
def print_solution(routes, cost):
    for i, route in enumerate(routes, start=1):
        print(f"Route #{i}: {' '.join(map(str, route))}")
    print(f"Cost {cost}")

filename = '../../data/A/A-n32-k5.vrp'  
node_coords, demands, capacity = parse_vrp_file(filename)

# Paramètres
max_iterations = 100
tabu_tenure = 10

# Profilage
pr = cProfile.Profile()
pr.enable()

# Résolution
best_solution, best_cost = tabu_search(node_coords, demands, capacity, max_iterations, tabu_tenure)

pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
ps.print_stats()

# Résultats

print(s.getvalue())
# Affichage des résultats
print_solution(best_solution, best_cost)
#verifying the solution
instance_data = read_instance(filename)
# print(best_solution)
print(verify_solution(instance_data, best_solution))

