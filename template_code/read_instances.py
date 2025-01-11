def read_instance(file_path):
    """
    Reads a .vrp file and extracts problem data.

    Args:
        file_path (str): Path to the .vrp file.

    Returns:
        dict: Contains the following keys:
            - name (str): Name of the instance.
            - comment (str): Additional information.
            - dimension (int): Number of nodes.
            - capacity (int): Vehicle capacity.
            - nodes (dict): Node coordinates as {node_id: (x, y)}.
            - demands (dict): Node demands as {node_id: demand}.
            - depot (int): Depot node ID.
    """
    data = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()

    section = None
    nodes = {}
    demands = {}

    for line in lines:
        line = line.strip()
        if line.startswith("NAME"):
            data["name"] = line.split(":")[1].strip()
        elif line.startswith("COMMENT"):
            data["comment"] = line.split(":")[1].strip()
        elif line.startswith("DIMENSION"):
            data["dimension"] = int(line.split(":")[1].strip())
        elif line.startswith("CAPACITY"):
            data["capacity"] = int(line.split(":")[1].strip())
        elif line.startswith("NODE_COORD_SECTION"):
            section = "nodes"
        elif line.startswith("DEMAND_SECTION"):
            section = "demands"
        elif line.startswith("DEPOT_SECTION"):
            section = "depot"
        elif line.startswith("EOF"):
            break
        elif section == "nodes":
            parts = line.split()
            node_id, x, y = int(parts[0]), float(parts[1]), float(parts[2])
            nodes[node_id] = (x, y)
        elif section == "demands":
            parts = line.split()
            node_id, demand = int(parts[0]), int(parts[1])
            demands[node_id] = demand
        elif section == "depot":
            data["depot"] = int(line)

    data["nodes"] = nodes
    data["demands"] = demands
    return data
