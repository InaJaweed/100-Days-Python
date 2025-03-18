print("Welcome to the tip calculator!")

# Ask the user for the total bill amount and convert it to a float for calculations
totalBill = float(input("What was the total bill? $"))

# Ask the user for the desired tip percentage (e.g., 10%, 12%, or 15%) and convert it to a float
currentTip = float(input("How much tip would you like to give? 10, 12 or 15? "))

# Ask how many people will split the bill and convert it to an integer
splitBetween = int(input("How many people to split the bill? "))

# Calculate the total bill including the tip
# Formula: Total bill * (1 + tip percentage/100)
totalTipBill = totalBill * ((currentTip / 100) + 1)

# Calculate how much each person should pay and round to 2 decimal places
finalBill = round(totalTipBill / splitBetween, 2)

# Alternative option (uncomment for exact value without rounding):
# finalBill = totalTipBill / splitBetween

# Display how much each person should pay using an f-string
print(f"Each person should pay: ${finalBill}")

# Alternative print method using formatted string to ensure 2 decimal places:
# print(f"Each person should pay: ${finalBill:.2f}")