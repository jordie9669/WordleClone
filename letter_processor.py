from collections import Counter
import random

WORDS_FILE = 'C:/Users/New User/PycharmProjects/wordleclone/words.txt'
FIVE_LETTER_WORDS = 'C:/Users/New User/PycharmProjects/wordleclone/five_letter_words.txt'


def pre_process_words() -> None:
    """Take the big list of words and pick out all 5 letter words and add them to a new text file."""
    with open(WORDS_FILE) as rawdata:
            with open(FIVE_LETTER_WORDS, 'w') as five_letter_words:
                for word in rawdata:
                    word = word.lower().strip()
                    if len(word) == 5:
                        print(word, file=five_letter_words)


def get_source_word():
    """Randomly grab a source word from the five letter words file."""
    with open(FIVE_LETTER_WORDS) as five:
        word = random.choice(five.readlines())

    return word


def all_chars_same(source):
    n = 0
    if n <= len(source):
        n = n + 1
        if input_word[n] == source[n]:
            print(input_word[n])
            return True

    return False


# Driver code
if __name__ == "__main__":

    input_word = input("Enter a 5 letter word: ")

    s = get_source_word()
    num_tries = 0

    if all_chars_same(s):
        print("Yes")
    else:
        while num_tries <= 5:
            if len(input_word) == 5:
                pass
            else:
                while len(input_word) != 5:
                    print("Your word must be 5 letters long")
                    input_word = input("Enter a 5 letter word: ")

            num_tries = num_tries + 1
            if num_tries == 5:
                print("Sorry you lose, the correct word was " + s)

            print("Your word is incorrect, try again")
            input_word = input("Enter a 5 letter word: ")





# def letters_in_correct_position(source):
#     for i in range(0, len(source)):
#         if input_word[i] == source[i]:
#             print(input_word[i].strip())
#             # these letter would change to green as they are in the correct position
#
# def letters_present_but_wrong_position(source):
#     pass
