import json

def loading_gui(total, completed):
    print("\033[H\033[J", end="")
    percentage = (completed / total )* 100
    number = round(percentage/10)
    print(f"{completed} / {total} completed")


def append_to_db(word_temp):

    total_temp_len = len(word_temp)
    completed_temp = 0

    with open("database.json") as database:
        database_snapshot = json.load(database)

        for word_obj in word_temp:
            current_char_length = str(word_obj["char_length"])
            # Check if a word already exists in the DB.
            existing_words = database_snapshot.get(current_char_length, {}).get(word_obj["sorted_word"], [])

            if word_obj["word"] in existing_words:
                print("Computer already knows this word ;)")
                continue

            database_snapshot.setdefault(current_char_length, {}).setdefault(word_obj["sorted_word"], []).append(word_obj["word"])

            completed_temp = completed_temp + 1
            loading_gui(total_temp_len, completed_temp)
            

        with open("database.json", "w") as database:
            json.dump(database_snapshot, database, indent=4)


def process_word(word):
    sorted_word_char_array = sorted(word.rstrip().lower())
    sorted_word = ""
    for char in sorted_word_char_array:
        sorted_word = sorted_word + char

    return {"sorted_word":sorted_word, "char_length":len(word.rstrip()), "word": word.rstrip().lower()}
        

def main():
    source_type = input("Is traning source a file or manual input? (f/m) : ")

    # if source is a traning file
    if source_type.lower() == "f":
        while True:
            try:
                source_name = input("Enter source name (Include extention) : ")
                with open(source_name, "r", encoding="utf-8") as file:
                    word_temp = []
                    
                    for word in file:
                        # add new word to cache
                        word_temp.append(process_word(word))
                    append_to_db(word_temp)
                    continue

            except FileNotFoundError:
                print("Sorry Computer couldn't find this file :(")
                print("Try again")

            except Exception as e:
                print(e)
                print("Try again")


    # if source is a manual word input
    elif source_type.lower() == "m":
        word = input("Enter one word you want to teach computer: ")
        cache = process_word(word)
        print(cache)
        append_to_db([cache])

    else:
        print("Hmm I didn't quite get that...")


if __name__ == "__main__":
    main()

if __name__ == "__append_to_db__":
    append_to_db()

if __name__ == "__process_word__":
    process_word()