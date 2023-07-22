import random
from words import GAME_WORDS  # list of words that can be given
from words import OTHER_WORDS  # all the other valid words in english(excludes GameWords)


VALID_WORDS = GAME_WORDS + OTHER_WORDS  # check capitalisation rules
MAX_TRIES = 6


def wordle():
    word = GAME_WORDS[random.randint(0, len(GAME_WORDS))]  # sets the word to guess
    for tries in range(MAX_TRIES):  # limits to 6 guesses
        guess = user_guess()
        while guess not in VALID_WORDS:  # prevents user from typing in crap
            print("Word is invalid. Guess must have 5 letters and be an English word. Guess another 5 letter word: \n")
            guess = user_guess()
        output = evaluate(guess, word)
        print(f"Guess result: \n {guess} \n {output}")
        print(f"{MAX_TRIES-tries} tries left")
        if guess == word:
            print(f"Congratulations, you guessed the word in {tries} tries")
            break
        if tries == MAX_TRIES:
            print(f"Maximum tries reached, better luck next time. \n The word was {word}.")


def user_guess():
    guess = input("Guess a 5 letter word: \n").lower()  # gets user's guess
    return guess


def evaluate(guess, word):  # handles one guess
    output = ""
    word_letters = word  # subtract letters from word_letters as they are guessed to avoid double yellows for duplicate letters in guess when actual word only has one
    for char in range(5):  # evaluates the guess letter by letter
        if guess[char] == word[char]:
            output += "G"
            word_letters = word_letters.replace(guess[char], '', 1)
        elif guess[char] in word_letters:
            output += "Y"
            word_letters = word_letters.replace(guess[char], '', 1)
        else:
            output += "X"
    return output


if __name__ == "__main__":
    wordle()
