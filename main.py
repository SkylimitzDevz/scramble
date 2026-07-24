import json
from train import process_word
from train import append_to_db

def train_computer(word):
    try:
        cache = process_word(word)
        append_to_db([cache])
        print("Yay computer smart! :D ")
        return
    except:
        print("Something went wrong")
        return


def main():
    print("######################################")
    user_input = input("Scramble a word! :")

    word_len = str(len(user_input))
    reorder = sorted(user_input)
    sorted_word = ""
    for char in reorder:
        sorted_word = sorted_word + char

    matches = get_matches(word_len, sorted_word)

    if matches == "404":
        print("Computer don't know word :(")
        teach = input("Do you want to teach computer new word? (y/n) :")

        if teach.lower() == "y":
            word = input("Yay tell me the new word! :")
            train_computer(word)
            return
        else:
            print("Okay... :(")        
            return

    if len(matches) > 1:
        print("Computer found many, Computer confused, Computer don't know correct :(")
        for word in matches:
            print(word)
        return

    for word in matches:
        print("YAY COMPUTER KNOW WORDDD :)")
        print(word)


def get_matches(word_len, sorted_word):
    with open("database.json") as database:
        database_snapshot = json.load(database)
        try:
            matches = database_snapshot[word_len][sorted_word]
            return matches
            
        except:
            return "404"

main()
