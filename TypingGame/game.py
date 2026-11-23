from pathlib import Path
import random


WORD_FILE = Path(__file__).parent / "test_words.txt"

def load_words():
    with open(WORD_FILE, "r") as file:
        words = file.read().splitlines()

    return words


def get_random_word(words):
    return random.choice(words)