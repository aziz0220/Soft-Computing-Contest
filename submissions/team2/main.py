import sys
import os

# Ajout explicite du chemin du dossier 'template_code'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Importation des fonctions nécessaires
from template_code.read_instances import read_instance
from template_code.verify_solution import verify_solution
from heuristiqueGloutonne import greedy_cvrp
from heuristiqueGloutonneEval import evaluate_algorithm, display_results

def main():
    # Répertoire contenant le script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Répertoire contenant les instances
    data_directory = os.path.join(script_dir, "../../data")

    # Paramètres pour l'évaluation
    max_iterations = 100
    params = [5, 10, 20]

    # Vérification de l'existence du répertoire
    if not os.path.exists(data_directory):
        raise FileNotFoundError(f"Le répertoire {data_directory} n'existe pas.")

    # Évaluation de l'algorithme glouton
    print("Évaluation de l'algorithme glouton sur les instances...")
    results = evaluate_algorithm(data_directory, greedy_cvrp, None, iterations=max_iterations, params=params)

    # Affichage des résultats
    print("\nRésultats finaux :")
    display_results(results)

if __name__ == "__main__":
    main()
