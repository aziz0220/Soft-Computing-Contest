# Soft Computing Contest: Capacitated Vehicle Routing Problem (CVRP)

## Overview

This repository is the central workspace for the Soft Computing Contest. The focus of this contest is solving the **Capacitated Vehicle Routing Problem (CVRP)** using various optimization techniques.

### Problem Description

The CVRP involves designing the most efficient routes for a fleet of vehicles to deliver goods to customers, ensuring:

- Each vehicle starts and ends at the depot.
- Each customer is visited exactly once.
- The total demand on a route does not exceed the vehicle's capacity.
- The objective is to minimize the total travel cost (distance).

For more details on CVRP, see [Augerat Instances](http://vrp.galgos.inf.puc-rio.br/index.php/en/).

---

## Repository Structure

- **`/data/`**: Contains the testing datasets (e.g., `.vrp` and `.sol` files).
  - Augerat's instances from Set A and Set B are provided here.
- **`/templates/`**: Contains template Python scripts.
  - `read_instance.py`: Reads `.vrp` files and extracts data like node coordinates, demands, and capacities.
  - `verify_solution.py`: Checks the feasibility of a solution and calculates its cost.
- **`/submissions/`**: Directories for each team to submit their solutions:
  - `/submissions/team1/`: Team 1 submissions.
  - `/submissions/team2/`: Team 2 submissions.
  - `/submissions/team3/`: Team 3 submissions.

---

## Getting Started

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Explore the Data**

   - Testing data is located in the `data/` folder. Use the template scripts in `templates/` to parse and analyze the datasets.

3. **Submit Your Solutions**
   - Each team should submit their solutions to their respective folder under `/submissions/`.

---

## Provided Tools

### Template Scripts

1. **`read_instance.py`**:

   - Simplifies loading and parsing `.vrp` files.
   - Provides access to node coordinates, demands, and other problem parameters.

2. **`verify_solution.py`**:
   - Checks if a solution is feasible (capacity constraints met, all customers visited).
   - Computes the total cost of a solution (e.g., distance).

Use these scripts to reduce implementation overhead and focus on your optimization techniques.

---

## Rules

- Each team is responsible for:
  - Implementing their assigned approaches.
  - Submitting their solutions in the correct format.
- The provided datasets and scripts are mandatory for consistency across teams.

---

## Questions?

For any inquiries or issues, please contact your friend Ahmed (hehe).

---

Happy coding and good luck! 🚀
