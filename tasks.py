import cmdLists
import sys
import functions


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
            case "edit":
                print("this will eventually edit a task")
            case _:
                print("Invalid command")


def create_new_task():
    print("type list for a list of possible options")
    name_input = new_task_input_loop("Task Name: ", "name")
    description = input("Description: ")
    color = new_task_input_loop("Color: ", "name")
    category = new_task_input_loop("Category: ", "name")
    section = new_task_input_loop("Section: ", "name")
    est_time = input("Estimated Time: ")
    due_date = input("Due Date: ")
    new_task_dict = {
        "name": name_input,
        "description": description,
        "color": color,
        "category": category,
        "section": section,
        "due date": due_date,
        "est time": est_time,
        "comp time": "0m",
        "rem time": est_time,
        "recurring": "false"
    }
    loaded_dict = functions.load_json_file("./database.json")
    loaded_dict['tasks'].append(new_task_dict)
    functions.update_json_file("./database.json", loaded_dict)
    
def new_task_input_loop(input_prompt, input_type):
    while True:
        user_input = input(input_prompt)
        if user_input.lower() == "list":
            print("list all tasks")
        else:
            break
    return user_input
    

# TODO: need to create way to add recurring tasks
