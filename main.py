import json
from train import process_word
from train import append_to_db

class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    GRAY = "\033[90m"

def train_computer(word):
    try:
        cache = process_word(word)
        append_to_db([cache])
        print(f"{Color.BLUE}Yay computer smart! :D {Color.RESET}")
        return
    except Exception as e:
        print(f"Something went wrong: {e}")
        return


def main():
    while True:
        print(f"{Color.GRAY}==============================={Color.RESET}")
        user_input = input(f"{Color.MAGENTA}Scramble a word! :{Color.RESET}").lower()

        word_len = str(len(user_input))
        reorder = sorted(user_input)
        sorted_word = ""
        for char in reorder:
            sorted_word = sorted_word + char

        matches = get_matches(word_len, sorted_word)

        if user_input == "exit":
            break

        if matches == "404":
            print(f"{Color.RED}Computer don't know word :({Color.RESET}")
            teach = input("Do you want to teach computer new word? (y/n) :")

            if teach.lower() == "y":
                word = input("Yay tell me the new word! :")
                train_computer(word)
                continue
            else:
                print("Okay... :(")
                continue


        if len(matches) > 1:
            print(f"{Color.YELLOW}Computer found many, Computer confused, Computer don't know correct :({Color.RESET}")
            print(f"{len(matches)} found")
            for word in matches:
                print(f"{Color.CYAN}{word}{Color.RESET}")
            continue

        for word in matches:
            print(f"{Color.GREEN}YAY COMPUTER KNOW WORDDD :){Color.RESET}")
            print(f"{Color.CYAN}MATCH:{Color.RESET} {word}")


def get_matches(word_len, sorted_word):
    with open("database.json") as database:
        database_snapshot = json.load(database)
        try:
            matches = database_snapshot[word_len][sorted_word]
            return matches
            
        except:
            return "404"

main()
