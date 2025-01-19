import sys
import os
import time

# Ajout explicit du chemin du dossier 'template_code'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../template_code')))
from rechTabouEvaluation import evaluate_algorithm, display_results,load_optimal_solution,evaluate_algorithm_for_single_instance
from rechercheTabouImpl import tabu_search
from recuitSimuleEvaluation import evaluate_algorithm as recuit_evaluate_algorithm, display_results as recuit_display_results
from recuitSimuleImpl import simulated_annealing
from Comparaison import  plot_simple_results
from read_instances import read_instance
from verify_solution import verify_solution
from heuristiqueGloutonne import greedy_cvrp
from heuristiqueGloutonneEval import evaluate_algorithm, display_results

def main():
    # Répertoire contenant le script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Chemin vers le fichier d'instance    
    instance_path = os.path.join(script_dir, "../../data/A/A-n32-k5.vrp")
    optimal_solution_path = os.path.join(script_dir, "../../data/A/A-n32-k5.sol")

    # Vérification du fichier d'instance
    if not os.path.exists(instance_path):
        raise FileNotFoundError(f"File {instance_path} does not exist.")
    
    # Chargement des données de l'instance
    instance_data = read_instance(instance_path)
    nodes = instance_data["nodes"]
    demands = instance_data["demands"]
    capacity = instance_data["capacity"]

    # Chargement de la solution optimale
    # optimal_solution = load_optimal_solution(optimal_solution_path)

    # Paramètres de la recherche taboue
    max_iterations = 100
    tabu_tenures = [5, 10, 20]
 #   params = [5, 10, 20]

    # Evaluation globale sur toutes les instances
    data_directory = os.path.join(script_dir, "../../data")
    # results = evaluate_algorithm(data_directory, tabu_search, optimal_solution_path, iterations=max_iterations, tabu_tenures=tabu_tenures)

    # # # Affichage des résultats de l'évaluation globale
    # # display_results(results)

  # Évaluation de l'algorithme glouton
    # print("Évaluation de l'algorithme glouton sur les instances...")
    # results = evaluate_algorithm(data_directory, greedy_cvrp, None, iterations=max_iterations, params=params)

    # # Affichage des résultats
    # print("\nRésultats finaux :")
    # display_results(results)


    taboue_results= evaluate_algorithm_for_single_instance(instance_path, tabu_search, optimal_solution_path, iterations=max_iterations, tabu_tenures=tabu_tenures)

    display_results(taboue_results)

    # plot_simple_results(taboue_results)

    # Comparison des 4 approches
    # generate_plots(taboue_results, recuit_results, locale_results, gloutonne_results)


      # Parameters for Simulated Annealing
    initial_temp = 1000
    final_temp = 5
    alpha = 0.99

#     recuit_results = recuit_evaluate_algorithm(data_directory, simulated_annealing, optimal_solution_path, initial_temp=initial_temp, final_temp=final_temp, alpha=alpha, max_iterations=max_iterations)

#     recuit_display_results(recuit_results)

    # plot_simple_results(recuit_results)


if __name__ == "__main__":
    main()