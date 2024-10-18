# this is my own module to put the word list for to guess
from wordlist import words

# this is the Random module; it will automatically pick random word from the wordlist
import random

# this is the ASKII art for the Hangman
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

# this is a function to display the hangman
def display_man(wrong_guesses):
    print ("*************") # for border design
    for line in hangman_art [wrong_guesses]:
        print(line)
    print ("*************")

# this will display the hint or the underscores, depending to the word to guess
def display_hint(hint):
    print(" ".join(hint))

# this will display the correct answer
def display_answer(answer):
    print(" ".join(answer))

# this is the main function containing the main body of code
def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("///Invalid input///")
            continue

        if guess in guessed_letters:
            print(f"///{guess} is already guessed///")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint [i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("///YOU WIN!///")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("///YOU LOSE!///")
            is_running = False


if __name__ == "__main__":
    main()

