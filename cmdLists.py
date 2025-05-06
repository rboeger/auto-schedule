import os
import functions


home = {
    "exit": "exits the program", 
    "help": "show this list",
    "tasks": "go to the task menu to edit or add tasks", 
    "categories": "go to the category menu to edit or add categories", 
    "sections": "go to the sections menu to edit or add sections"
}

tasks = {
    "exit": "exit the task menu",
    "help": "show this list"
}

sections = {
    "exit": "exit the section menu",
    "help": "show this list"
}

categories = {
    "exit": "exit the category menu",
    "help": "show this list"
}


def get_task_list():
    loaded_task_list = functions.load_json_file("./database.json")
    filtered_task_list = {}
    for task in loaded_task_list['tasks']:
        filtered_task_list[task['name']] = task['description']
    return filtered_task_list


def get_section_list():
    loaded_section_list = functions.load_json_file("./database.json")
    filtered_section_list = {}
    for section in loaded_section_list['sections']:
        filtered_section_list[section['name']] = section['start time']
    return filtered_section_list


error = {
        "an edge case has occurred": "Please look into the error"
}


def get_list(list_name):
    match list_name.lower():
        case "home":
            return home
        case "tasks":
            return tasks
        case "sections":
            return sections
        case "categories":
            return categories
        case "task list":
            return get_task_list()
        case "section list":
            return get_section_list()
        case _:  # edge case, will probably never be used
            return error


def generate_cmd_list(list_name):
    list_data = get_list(list_name)
    visual_list = "\n"
    
    for item in list_data:
        visual_list += f"\t{item} - {list_data[item]}\n"
    os.system('cls' if os.name == 'nt' else 'clear')
    print(visual_list)


