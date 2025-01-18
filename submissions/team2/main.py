import sys
import os
import time

# Ajout explicit du chemin du dossier 'template_code'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../template_code')))
from rechTabouEvaluation import evaluate_algorithm, display_results,load_optimal_solution
from rechercheTabouImpl import tabu_search
from read_instances import read_instance

def main():
    # Chemin vers le fichier d'instance    
    instance_path = r"C:\3eme\Soft computing\ContestProject\Soft-Computing-Contest\data\A\A-n32-k5.vrp"
    optimal_solution_path = r"C:\3eme\Soft computing\ContestProject\Soft-Computing-Contest\data\A\A-n32-k5.sol"

    # Vérification du fichier d'instance
    if not os.path.exists(instance_path):
        raise FileNotFoundError(f"File {instance_path} does not exist.")
    
    # Chargement des données de l'instance
    instance_data = read_instance(instance_path)
    nodes = instance_data["nodes"]
    demands = instance_data["demands"]
    capacity = instance_data["capacity"]

    
    # Chargement de la solution optimale
    optimal_solution = load_optimal_solution(optimal_solution_path)

    # Paramètres de la recherche taboue
    max_iterations = 100
    tabu_tenures = [5, 10, 20]

    # Evaluation globale sur toutes les instances
    data_directory = r"C:\3eme\Soft computing\ContestProject\Soft-Computing-Contest\data"
    results = evaluate_algorithm(data_directory, tabu_search, optimal_solution_path, iterations=max_iterations, tabu_tenures=tabu_tenures)

    # Affichage des résultats de l'évaluation globale
    display_results(results)




if __name__ == "__main__":
    main()
