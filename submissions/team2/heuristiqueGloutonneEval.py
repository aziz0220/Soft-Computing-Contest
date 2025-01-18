import os
import random
import sys
import statistics
import time

# Ajout explicite du chemin du dossier 'template_code'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from template_code.read_instances import read_instance
from template_code.verify_solution import verify_solution

# Extraction des routes et coût optimal
def parse_solution_file(solution_path):
    optimal_cost = None
    optimal_routes = []

    with open(solution_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("Route #"):
                route = list(map(int, line.split()[2:]))
                optimal_routes.append(route)
            elif line.startswith("Cost"):
                optimal_cost = int(line.split()[1])

    return optimal_routes, optimal_cost

def calculate_proximity(optimal_cost, generated_cost):
    return (abs(optimal_cost - generated_cost) / optimal_cost) * 100

def evaluate_algorithm(data_path, your_method, solution_path, iterations=100, params=[5, 10, 20]):
    results = {}
    print(f"Evaluating files in directory: {data_path}")

    for root, dirs, files in os.walk(data_path):
        for filename in files:
            if filename.endswith('.vrp'):
                instance_path = os.path.join(root, filename)
                solution_file = instance_path.replace('.vrp', '.sol')
                print(f"Processing instance file: {filename}")

                try:
                    instance_data = read_instance(instance_path)
                    nodes, demands, capacity = instance_data["nodes"], instance_data["demands"], instance_data["capacity"]

                    optimal_routes, optimal_cost = parse_solution_file(solution_file)
                    print(f"Optimal cost loaded: {optimal_cost}")
                except Exception as e:
                    print(f"Error reading instance {filename}: {e}")
                    continue

                instance_results = {}

                costs = []
                valid_solutions = 0
                exec_times = []
                proximities = []
                total_simulations = 5

                for _ in range(total_simulations):
                    try:
                        start_time = time.time()
                        best_solution, best_cost = your_method(nodes, demands, capacity)
                        exec_time = time.time() - start_time

                        proximity = calculate_proximity(optimal_cost, best_cost)
                        proximities.append(proximity)

                        is_valid, _, _ = verify_solution(
                            {'nodes': nodes, 'demands': demands, 'capacity': capacity},
                            best_solution
                        )

                        costs.append(best_cost)
                        exec_times.append(exec_time)

                        if is_valid:
                            valid_solutions += 1
                    except Exception as e:
                        print(f"Error during execution for {filename}: {e}")
                        continue

                if costs:
                    instance_results = {
                        'average_cost': statistics.mean(costs),
                        'min_cost': min(costs),
                        'max_cost': max(costs),
                        'std_cost': statistics.stdev(costs) if len(costs) > 1 else 0,
                        'valid_percentage': (valid_solutions / total_simulations) * 100,
                        'average_execution_time': statistics.mean(exec_times),
                        'average_proximity': statistics.mean(proximities),
                        'num_vehicles': len(best_solution)  # Number of vehicles used
                    }

                results[filename] = instance_results

    print("Final evaluation results:", results)
    return results


def display_results(results):
    """
    Displays the evaluation results in a readable format.

    Args:
        results (dict): Dictionary containing evaluation results for each instance.
    """
    for instance, instance_results in results.items():
        print(f"\nInstance: {instance}")
        print(f"  Average Cost: {instance_results['average_cost']:.2f}")
        print(f"  Min Cost: {instance_results['min_cost']:.2f}")
        print(f"  Max Cost: {instance_results['max_cost']:.2f}")
        print(f"  Std Dev of Cost: {instance_results['std_cost']:.2f}")
        print(f"  Valid Solutions: {instance_results['valid_percentage']:.2f}%")
        print(f"  Average Execution Time: {instance_results['average_execution_time']:.4f} seconds")
        print(f"  Average Proximity: {instance_results['average_proximity']:.2f}%")
        print(f"  Number of Vehicles Used: {instance_results['num_vehicles']}")