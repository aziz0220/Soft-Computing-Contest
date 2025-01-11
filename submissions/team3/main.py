import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from template_code.read_instances import read_instance
from template_code.verify_solution import verify_solution

if __name__ == "__main__":
    # Example: Reading an instance
    instance_path = "../../data/A/A-n32-k5.vrp"
    instance_data = read_instance(instance_path)
    