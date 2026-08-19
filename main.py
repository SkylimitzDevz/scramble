import json
from utils import help_message, process_search_query
from train import append_to_db, process_word
from utils import Color
import time

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
        start_time = ""
        end_time = ""

        print(f"{Color.GRAY}==============================={Color.RESET}")
        scrambled_input = input(f"{Color.MAGENTA}Scramble a word!: {Color.RESET}").lower()

        if scrambled_input == "/help":
            help_message()
            continue

        with open("database.json") as f:
            db = json.load(f)
        if not db:
            print(f"{Color.RED}Database is empty{Color.RESET}\nPlease use 'python train.py'")
            break

        if scrambled_input == "/exit":
            break
        
        [sorted_word, word_len] = process_search_query(scrambled_input)

        start_time = time.time()
        matches = get_matches(word_len, sorted_word)
        end_time = time.time()


        if matches == "404":
            print(f"{Color.RED}Computer don't know word :({Color.RESET}")
            teach = input("Do you want to teach computer a new word? (y/n): ")

            if teach.lower() == "y":
                word = input("Yay tell me the new word!: ")
                train_computer(word)
                continue
            else:
                print("Okay... :(")
                continue

        print(f"{Color.GRAY}Took {end_time - start_time:.2f} seconds{Color.RESET}")

        if len(matches) > 1:
            print(f"{Color.YELLOW}Computer found many, Computer confused, Computer don't know correct :({Color.RESET}")
            print(f"{len(matches)} found")
            for word in matches:
                print(f"{Color.CYAN}{word}{Color.RESET}")
            continue

        for word in matches:
            print(f"{Color.GREEN}YAY COMPUTER KNOW WORDDD :){Color.RESET}")
            print(f"{Color.CYAN}MATCH:{Color.RESET} {word}")

def lookup_matches(db, word_len, sorted_word):
    return db.get(word_len, {}).get(sorted_word, []) 

def get_matches(word_len, sorted_word):
    with open("database.json") as database:
        db = json.load(database)

        try:
            matches = lookup_matches(db, word_len, sorted_word)
            if not matches:
                return "404"
            return matches 
            
        except Exception as e:
            print(e)

main()
