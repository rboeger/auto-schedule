import os
import json

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except json.JSONDecodeError:
      print(f"Error: Invalid JSON format in: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def update_json_file(file_path, new_python_dict):
    loaded_file = load_json_file(file_path)
    with open(file_path, "w") as file:
        json.dump(new_python_dict, file)


