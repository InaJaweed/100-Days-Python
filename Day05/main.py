# Import the random module to generate random selections
import random

# List of all lowercase letters
lowLetters = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', "l", 'm', 'n','o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# List of all uppercase letters
uppLetters = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', "L", 'M', 'N','O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List of all digits from 0 to 9
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of common symbols used in passwords
symbols = ['!','#','$', '%', '&','(' ,')', '*', '_']


print("Welcome to the Password Generator!")

# User input to define the number of characters from each category
nrLowLetters = int(input("How many lower case letters would you like? "))
nrUppLetters = int(input("How many upper case letters would you like? "))
nrNumbers = int(input("How many numbers would you like? "))
nrSymbols = int(input("How many symbols would you like? "))

# Empty lists to store randomly chosen characters
finalLowLetters = []
finalUppLetters = []
finalNumber = []
finalSymbols = []

# Generate random lowercase letters using a for loop
for lowLet in range(1, nrLowLetters + 1):
    # Choose a random index within the length of the lowLetters list
    randomLowLetter = random.randint(0, len(lowLetters) - 1)
    # Append the randomly selected letter to the finalLowLetters list
    finalLowLetters += lowLetters[randomLowLetter]

# Generate random uppercase letters
for uppLet in range(1, nrUppLetters + 1):
    randomUppLetter = random.randint(0, len(uppLetters) - 1)
    finalUppLetters += uppLetters[randomUppLetter]

# Generate random numbers
for num in range(1, nrNumbers + 1):
    randomNumber = random.randint(0, len(number) - 1)
    finalNumber += number[randomNumber]

# Generate random symbols
for symb in range(1, nrSymbols + 1):
    randomSymbol = random.randint(0, len(symbols) - 1)
    finalSymbols += symbols[randomSymbol]

# Combine all the randomly chosen characters into one list
password = finalLowLetters + finalUppLetters + finalNumber + finalSymbols

# Shuffle the list to randomize the order of characters
random.shuffle(password)

# Convert the list into a string using join() to create the final password
finalPass = "".join(password)

# Display the generated password
print(f"Here is your password: {finalPass}")
