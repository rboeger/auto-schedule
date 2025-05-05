import cmdLists
import sys


def run():
    while True:
        print("---CATEGORIES---")
        user_input = input("Enter a command: ").lower()
    
        match user_input:
            case "exit":
                sys.exit()
            case "back" | "home":
                break
            case "help":
                cmdLists.generate_cmd_list("categories")
            case "new":
                name = input("Category Name: ")
                color = input("Color: ")
            case "tasks":
                name = input("Category to list tasks: ")
                print("This will eventually list the tasks that are in the category ", name)
            case _:
                print("Invalid command")
            
