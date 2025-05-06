import cmdLists
import sys
import functions
import json


def run():
    while True:
        print("---TASKS---")
        user_input = input("Please enter a command: ").lower()

        match user_input:
            case "help":
                functions.clear_screen()
                cmdLists.generate_cmd_list("tasks")
            case "back" | "home":
                break
            case "exit":
                sys.exit()
            case "new":
                create_new_task()
            case "list":
                cmdLists.generate_cmd_list("task list")
            case _:
                print("Invalid command")


def create_new_task():
    name_input = input("Task Name: ")
    description = input("Description: ")
    color = input("Color: ")
    category = input("Category: ")
    section = input("Section: ")
    est_time = input("Estimated Time: ")
    new_task_dict = {
        "name": name_input,
        "description": description,
        "color": color,
        "category": category,
        "section": section,
        "est time": est_time,
        "comp time": "0m",
        "rem time": est_time,
        "recurring": "false"
    }
    loaded_dict = functions.load_json_file("./database.json")
    loaded_dict['tasks'].append(new_task_dict)
    functions.update_json_file("./database.json", loaded_dict)
    
    
# TODO: need to create function to add new tasks to json file
def add_task_to_json(new_task_dict):
    pass
    

# TODO: need to create way to add recurring tasks
