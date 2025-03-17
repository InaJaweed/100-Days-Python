print("Welcome to the Band Name Generator")
# getting the user input and using upper method to capitalise all characters
city = input("What's the name of the city you grew up in?\n").upper()
animeChar = input("What's your favourite anime character?\n").upper()
# printing the generated band name by concatenating the city and animeChar character with a space
print("Your band name could be " + city + ' ' + animeChar)