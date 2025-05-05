import cmdLists
import sys


def run():
    while True:
        print("---SECTIONS---")
        user_input = input("Please enter a command: ").lower()
    
        match user_input:
            case "exit":
                sys.exit()
            case "home" | "back":
                break
            case "help":
                cmdLists.generate_cmd_list("sections")
            case _:
                print("Invalid command")
