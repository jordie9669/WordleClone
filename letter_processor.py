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
    # with open(FIVE_LETTER_WORDS) as five:
    #     word = random.choice(five.readlines())
    # return word
    word = 'train'
    return word


def allCharactersSame(source):
    n = len(source)
    print(n)
    input_word = input('Enter a word: ')
    print(input_word)
    for i in range(0, n):
        print(input_word[i])
        if input_word[i] == source[i]:
            return True
    return False


# Driver code
if __name__ == "__main__":

    s = get_source_word()
    if allCharactersSame(s):
        print("Yes")
    else:
        print("No")
