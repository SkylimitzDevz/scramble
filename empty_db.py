import json


class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    GRAY = "\033[90m"


def main():
    try:
        while True:
            empty_state = {}
            should_clear = input(f"{Color.RED}Are you sure you want to empty the database?(y/n): {Color.RESET}").lower()
            if should_clear == "y":
                with open("database.json", "w") as f:
                    json.dump(empty_state, f, indent=4)
                print(f"{Color.GREEN}Database successfully cleared!{Color.RESET}")
                break
            elif should_clear == "n":
                print("OK")
                break
            else:
                print(f"{Color.YELLOW}Use 'y' for yes or 'n' for no{Color.RESET}")
                continue
    except Exception as e:
        print(e)

main()