# Import the random module for generating random numbers
import random

# ASCII art representations for Rock, Paper, and Scissors
rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
PAPER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
SCISSOR
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Create a list to store the ASCII art choices
choices = [rock, paper, scissor]

# Prompt the user to make a choice by inputting 0, 1, or 2
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
print("Player Choice:")
print(choices[player])

# Generate a random choice for the computer using randint (0, 2)
computer = random.randint(0, 2)
print("Computer Choice:")
print(choices[computer])

# Determine the result of the game using conditional statements
if player == computer:
    # If both choices are the same, it's a tie
    print("This is a tie.")
elif player == 0 and computer == 2:
    # Rock (0) beats Scissors (2)
    print("You Win!")
elif player == 1 and computer == 0:
    # Paper (1) beats Rock (0)
    print("You Win!")
elif player == 2 and computer == 1:
    # Scissors (2) beats Paper (1)
    print("You Win!")
else:
    # Any other case means the computer wins
    print("You Lose!!")
