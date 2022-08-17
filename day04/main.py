import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Human Choice
choice = (input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n0/1/2:"))

# Computer Choice
computers_choice = random.randint(0, 2)

# If the user doesn't type a digit, display the error!
if not choice.isdigit():
    print("You've entered an invalid value, try again and choose a number between 0-2.")

# If the user types a digit, continue the game
else:
    choice = int(choice)

    # If the user enter more than 2, display the error
    if choice > 2:
        print("You've entered an invalid number, try again and choose a number between 0-2.")

    # If the user enter properly, print their choice
    elif choice == 0 or choice == 1 or choice == 2:
        if choice == 0:
            print(f"You chose: Rock {rock}")
        elif choice == 1:
            print(f"You chose: Paper {paper}")
        elif choice == 2:
            print(f"You chose: Scissors {scissors}")

        # If the computer chooses Rock
        if computers_choice == 0:
            print(f"The computer chose: Rock {rock}")
            if choice == 2:
                print("You lose, Rock wins against scissors.")  # Rock vs Scissors
            elif choice == 0:
                print("It's a draw!")  # Rock vs Rock
            else:
                print("You win!")  # Rock vs Paper

        # If the computer chooses Paper
        elif computers_choice == 1:
            print(f"The computer chose: Paper {paper}")
            if choice == 0:
                print("You lose, Paper wins against rock.")  # Paper vs Rock
            elif choice == 0:
                print("It's a draw!")   # Paper vs Paper
            else:
                print("You win!")   # Paper vs Scissors

        # If the computer chooses Scissors
        elif computers_choice == 2:
            print(f"The computer chose: Scissors {scissors}")
            if choice == 1:
                print("You lose, Scissors win against paper.")   # Scissors vs Paper
            elif choice == 2:
                print("It's a draw!")   # Scissors vs Scissors
            else:
                print("You win!")   # Scissors vs Rock
