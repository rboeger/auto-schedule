import os
import json

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# loaded from LLM
def load_json_file(file_path):
    data = None
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except json.JSONDecodeError:
      print(f"Error: Invalid JSON format in: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return data


def update_json_file(file_path, new_python_dict):
    loaded_file = load_json_file(file_path)
    with open(file_path, "w") as file:
        json.dump(new_python_dict, file)

