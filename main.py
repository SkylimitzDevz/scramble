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

    print(f"{Color.GREEN}Hello! Welcome to Scramble \nYou Scramble, I guess!{Color.RESET}")
    print(f"Use '/help' for more info")

    while True:
        print(f"{Color.GRAY}==============================={Color.RESET}")
        user_input = input(f"{Color.MAGENTA}Scramble a word! :{Color.RESET}").lower()

        if user_input == "/help":
            print(f"\n\n{Color.GREEN}================ HELP ================{Color.RESET}")
            print("Here's how to play:")
            print(f"- You can scramble a word and send it\n- The program will try to guess the word\n- You can also teach a word to the computer by sending in the new word\n{Color.CYAN}- You can also do a mini benchmark by training your computer on more words so it can be smarter!{Color.RESET}")

            print(f"\n{Color.GREEN}How to Train!{Color.RESET}")
            print("To train, exit this program first and use 'python train.py'\nAfter, choose 'file' by saying 'f'\nThen type in your preferred file.")
            print("Available file:\n- 1K\n- 50K\n- 100K\n- 500K")
            print("Run one as '1k_words.txt' and see how long it takes, and share the time!")
            print("This is a CPU test")

            print(f"{Color.GREEN}\nCOMMANDS{Color.RESET}\n- /exit - exit the program\n- /help - to get help")
            print(f"{Color.GREEN}======================================{Color.RESET}")
            continue

        with open("database.json") as f:
            db = json.load(f)
        if not db:
            print(f"{Color.RED}Database is empty{Color.RESET}\nPlease use 'python train.py'")
            break
        
        word_len = str(len(user_input))
        reorder = sorted(user_input)
        sorted_word = ""
        for char in reorder:
            sorted_word = sorted_word + char

        matches = get_matches(word_len, sorted_word)

        if user_input == "/exit":
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
