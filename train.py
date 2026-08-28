import json
import time
from utils import Color
import traceback

def loading_gui(total, completed):
    percentage = (completed / total) * 100
    filled = int(40 * percentage / 100)
    bar = "█" * filled + "-" * (40 - filled)
    print(f"\r{completed}/{total}{Color.GREEN} |{bar}| {Color.RESET}{percentage:5.1f}%\033[K", end="", flush=True)


def append_to_db(word_temp):
    total_temp_len = len(word_temp)
    completed_temp = 0
    skipped = 0

    with open("database.json") as database:
        database_snapshot = json.load(database)

        for word_obj in word_temp:
            current_char_length = str(word_obj["char_length"])
            existing_words = database_snapshot.get(current_char_length, {}).get(word_obj["sorted_word"], [])

            if word_obj["word"] in existing_words:
                skipped += 1
                completed_temp += 1
                loading_gui(total_temp_len, completed_temp)
                continue
            new_word = {"word":word_obj["word"], "score":0}
            database_snapshot.setdefault(current_char_length, {}).setdefault(word_obj["sorted_word"], []).append(new_word)

            completed_temp += 1
            loading_gui(total_temp_len, completed_temp)

        with open("database.json", "w") as database:
            json.dump(database_snapshot, database, indent=4)

        return {"skipped_words":skipped}


def process_word(word):
    sorted_word_char_array = sorted(word.rstrip().lower())
    sorted_word = ""
    for char in sorted_word_char_array:
        sorted_word = sorted_word + char
    return {"sorted_word":sorted_word, "char_length":len(word.rstrip()), "word": word.rstrip().lower()}


def train_dataset(dataset):
    start_time = ""
    end_time = ""
    word_temp = []
    start_time = time.time()
    for word in dataset:
        word_temp.append(process_word(word))
    output = append_to_db(word_temp)
    end_time = time.time()
    print()
    if output["skipped_words"]:
        print(f"Computer already knew {output["skipped_words"]} word(s), skipped them.")
    print(f"{Color.GREEN}Took {end_time - start_time:.2f} seconds{Color.RESET}")


def main():
    source_type = input("Is training source a file or manual input? (f/m) : ")
    # if source is a traning file
    if source_type.lower() == "f":
        while True:
            try:
                source_name = input("Enter source name (Include extension) : ")
                with open(source_name, "r", encoding="utf-8", errors="replace") as file:
                    train_dataset(file)
                    break

            except FileNotFoundError:
                print("Sorry Computer couldn't find this file :(")
                print("Try again")

            except Exception as e:
                print(e)
                print("Try again")


    # if source is a manual word input
    elif source_type.lower() == "m":
        word = input("Enter one word you want to teach computer: ")
        train_dataset([word])

    else:
        print("Hmm I didn't quite get that...")


if __name__ == "__main__":
    main()