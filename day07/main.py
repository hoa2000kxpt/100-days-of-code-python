"""
Hints:
#Step 1: Picking a random words and checking answers
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word

#Step 2: Replacing Blanks with Guesses
#TODO-1 - Create an empty List called display. For each letter in the chosen_word, add "_" to 'display'.
So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_"
representing each letter to guess.
#TODO-2 - Loop through each position in the chosen_word; If the letter at that position matches 'guess the reveal
that letter in the display at that position. (e.g: If the user guessed "p" and the chosen word was "apple", then
display should be ["_", "p", "p", "_", "_"])
#TODO-3 - Print 'display' and you should see the guessed letter in the correct position and every other letter
replace with "_".

#Step 3: Checking if the Player has won
#TODO-1 - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
letters in the chosen_word and 'display' has more blanks ("_"). Then you can tell the user they've won.

#Step 4: Keeping Track of the Player's Lives
#TODO-1 - Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
#TODO-2 - If guess is not a letter in the chosen_word, then reduce 'lives' by 1. If the lives goes down to 0 then the
game should stop and it should print "You lose".
#TODO-3 - Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

#Step 5: Improve the User Experience
#TODO-1 - Update the word list to use the 'word_list' from hangman_words.py.
#TODO-2 - Import the stages from hangman_art.py and make this error go away.
#TODO-3 - Import the logo from hangman_art.py and print it at the start of the game
#TODO-4 - If the user has entered a letter they've already guessed, print the letter and let them know.
#TODO-5 - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
"""

from replit import clear
import random
from hangman_words import word_list
from hangman_art import stages, logo2, logo3

# Initialize chosen word and word length
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo3)
print("\nTo win, guess the word before the person is hung.\n")

display = []
wrong_guesses = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter:").lower()

    clear()

    # If the user guesses wrong, add it to list
    if guess in wrong_guesses:
        print(f"{' '.join(display)}")
        print(stages[lives])
        print(f"You've already guessed with the letter '{guess}', pick another letter.")
    else:
        wrong_guesses.append(guess)

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        print(f"{' '.join(display)}")

        # If there is no underscore symbol, the user wins!
        if "_" not in display:
            end_of_game = True
            print("\nGeninus, genius, genius! You won!")
            print(logo2)

        # # If the user guesses wrong, subtract 1 life
        if guess not in chosen_word:
            lives -= 1

        if not end_of_game:
            print(stages[lives])
            if guess not in chosen_word:
                print(f"'{guess}' is not in the word, you lost 1 life.")

        if lives == 0:
            end_of_game = True
            print("The man has been hung, you lose.")
            print(f"\nThe word was '{chosen_word}'")
