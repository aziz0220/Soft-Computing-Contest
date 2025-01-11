import math

def euclidean_distance(node1, node2):
    """
    Computes the Euclidean distance between two nodes.

    Args:
        node1 (tuple): Coordinates of the first node (x, y).
        node2 (tuple): Coordinates of the second node (x, y).

    Returns:
        float: Euclidean distance.
    """
    return math.sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2)

def verify_solution(instance_data, solution):
    """
    Verifies the feasibility of a CVRP solution and computes its cost.

    Args:
        instance_data (dict): Parsed .vrp instance data.
        solution (list of lists): Solution routes, e.g., [[1, 2, 3], [4, 5, 6]].

    Returns:d
        tuple: (is_feasible (bool), total_cost (float))
    """
    nodes = instance_data["nodes"]
    demands = instance_data["demands"]
    capacity = instance_data["capacity"]
    depot = instance_data["depot"]

    total_cost = 0
    for route in solution:
        load = 0
        route_cost = 0

        # Start from the depot
        prev_node = depot

        for node in route:
            load += demands[node]
            if load > capacity:
                return False, 0  # Infeasible due to capacity violation

            route_cost += euclidean_distance(nodes[prev_node], nodes[node])
            prev_node = node

        # Return to the depot
        route_cost += euclidean_distance(nodes[prev_node], nodes[depot])
        total_cost += route_cost

    return True, total_cost