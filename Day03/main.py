# ASCII
ascii = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''

# Display the ASCII art
print(ascii)

# Welcome message for the game
print("Welcome to Treasure Island")

# Prompt the user for their name
user = input("What is your name? ")

# Introduce the game mission to the user
print(f"Hello {user}, your mission is to find treasure.\n")

# First decision point: opening the chest
print(f"{user} comes across a chest. Do you want to open it? Yes or No?")
choice = input("choice: ").lower()  # Convert input to lowercase for easier comparison

if choice == "yes":
    # If the user chooses to open the chest
    print("You found a weapon! And then you find yourself in a maze.\n")
    print("As you walk closer to the center, you see a glimpse of light\nand then BOOM!!! Undead creatures start surrounding you!!")
    
    # Second decision point: fight or run
    print("Make a choice: do you want to fight or run?")
    choice = input("choice: ").lower()

    if choice == "fight":
        # If the user chooses to fight
        print(f"Unlucky {user}, you have died!!")
    else:
        # If the user chooses to run
        print("\nAs you run away, you step on a trip wire and open up a secret pathway that leads to a gold fountain!!")
        print(f"Congrats!! {user}, you have found the treasure!!")

else:
    # If the user chooses not to open the chest
    print("You make progress towards an old tree.")
    print("As you walk, you see a small well with a beam of light.\nYou take a closer look and see something gold!")
    
    # Second decision point: jump in or ignore
    print("Make a choice: jump in or ignore?")
    choice = input("choice: ").lower()

    if choice == "jump":
        # If the user jumps in
        print(f"{user} found the golden fountain! Congrats!!")
    else:
        # If the user ignores the well
        print(f"{user} died! A sudden monster flew and attacked you!")
