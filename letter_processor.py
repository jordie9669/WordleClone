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


def get_source_word() -> str:
    """Randomly grab a source word from the five letter words file."""
    with open(FIVE_LETTER_WORDS) as five:
        word = random.choice(five.readlines())
    print(word.strip())
    return word.strip()


get_source_word()