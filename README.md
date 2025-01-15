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
- **`/template_code/`**: Contains template Python scripts.
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

   - Testing data is located in the `data/` folder. Use the template scripts in `template_code/` to parse and analyze the datasets.

3. **Submit Your Solutions**
   - Each team should submit their solutions to their respective folder under `/submissions/`.
   - You can also make a pull request, and I'll merge it.

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

## Contributing with Pull Requests

Submit a solution via a pull request (PR):
(pre-requisite: ⭐️ Star this repo)
1. **Fork the Repository**:
   - Go to the repository on GitHub and click the "Fork" button to create your own copy.

2. **Clone the Fork**:
   - Clone your forked repository to your local machine:
     ```bash
     git clone <your_forked_repository_url>
     cd <repository_folder>
     ```

3. **Create a New Branch**:
   - Always work on a new branch to keep your changes organized:
     ```bash
     git checkout -b <branch_name>
     ```

4. **Make Your Changes**:
   - Implement your solution or modifications in the appropriate files.

5. **Commit and Push**:
   - Save your changes with a commit message and push the branch to your fork:
     ```bash
     git add .
     git commit -m "Description of your changes"
     git push origin <branch_name>
     ```

6. **Open a Pull Request**:
   - Go to the original repository on GitHub.
   - Click "Compare & pull request."
   - Provide a clear description of the changes you made and submit the pull request.

7. **Discuss and Revise**:
   - Collaborate with maintainers for any required revisions or discussions.

8. **Merge**:
   - Once approved, your changes will be merged into the main repository.

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

Happy coding and good luck les amis! 🚀
