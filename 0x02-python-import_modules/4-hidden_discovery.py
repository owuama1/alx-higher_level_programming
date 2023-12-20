#!/usr/bin/python3
import importlib.util

def get_module_names(module_path):
    # Load the module
    module_spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)

    # Get names from the module and filter out those starting with '__'
    names = [name for name in dir(module) if not name.startswith("__")]

    return names

if __name__ == "__main__":
    module_path = "hidden_4.pyc"
    module_names = get_module_names(module_path)

    # Print names in alphabetical order
    for name in sorted(module_names):
        print(name)
