"""Task 1: Text-based Hangman using random, while loop, if-else, strings, and lists."""

import random

WORDS = ["python", "hangman", "program", "keyboard", "computer","Rushabh"]
MAX_WRONG = 6


def display_word(word, guessed):
    """Show the word with unguessed letters as underscores."""
    shown = []
    for letter in word:
        if letter in guessed:
            shown.append(letter)
        else:
            shown.append("_")
    return " ".join(shown)


def play():
    word = random.choice(WORDS)
    guessed = []          # all letters guessed so far
    wrong = 0

    print("Welcome to Hangman!")
    print(f"You have {MAX_WRONG} incorrect guesses allowed.\n")

    while wrong < MAX_WRONG:
        print("Word:", display_word(word, guessed))
        print("Guessed:", " ".join(guessed) if guessed else "-")
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
        elif guess in guessed:
            print("You already guessed that letter.\n")
        else:
            guessed.append(guess)
            if guess in word:
                print("Good guess!\n")
            else:
                wrong += 1
                print("Wrong guess!\n")

        # Check for a win
        if all(letter in guessed for letter in word):
            print("Word:", display_word(word, guessed))
            print("Congratulations, you won!")
            return

    print(f"Game over! The word was '{word}'.")


if __name__ == "__main__":
    play()
