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

def help_message():
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

def process_search_query(scrambled_word: str):
    word_len = str(len(scrambled_word.rstrip()))
    reordered_word = sorted(scrambled_word)
    sorted_word = ""
    for char in reordered_word:
        sorted_word = sorted_word + char
    return [sorted_word, word_len]

def main():
    test = process_search_query("lleho")
    print(test)

def print_hr(name="", length=32, return_permission=False):
    current_length = length
    final_print = ""
    if name:
        current_length = (current_length - len(name)) - 2
        if not current_length % 2 == 0:
            current_length = current_length - 1
        hr = "=" * (current_length // 2)
        final_print = (f"{hr} {name} {hr}")
    else:
        final_print = ("=" * current_length)

    return final_print if return_permission else print(final_print)

def color_print(color, text):
    color_code = getattr(Color, str(color).upper(), None)
    if color_code and color_code != Color.RESET:
        print(f"{color_code}{text}{Color.RESET}")
    else:
        print(text)


def find_best_match(wordList):
    max = { "word": "", "score": 0 }
    isAllEqual = True

    if not wordList:
        raise ValueError("Input cannot be empty.")
        
    for word in wordList:

        if word["score"] > max["score"]:
            max = word

        if word["score"] != max["score"]:
            isAllEqual = False

    if isAllEqual:
        return wordList
    else:
        return max

if __name__ == "__main__":
    main()