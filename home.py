import tasks
import sections
import categories
import cmdLists
import functions


def main():
    functions.clear_screen()
    print("Type \"help\" at any time to get a list of commands")
    while True:
        print("---HOME---")
        user_input = input("Enter a command: ").lower()

        match user_input:
            case "exit":
                break
            case "tasks":
                functions.clear_screen()
                tasks.run()
            case "categories":
                functions.clear_screen()
                categories.run()
            case "sections":
                functions.clear_screen()
                sections.run()
            case "help":
                cmdLists.generate_cmd_list("home")
            case "schedule":
                print("view schedule")
            case _:
                print("Invalid command")


if __name__ == "__main__":
    main()
