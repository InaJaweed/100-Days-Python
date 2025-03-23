print("Welcome to the rollercoaster")

height = int(input("What is your height? "))

cost = 0

if height < 120:
    print("Cant Ride")
else:
    age = int(input("What is your age? "))
    if age >= 45 and age <= 55: # 45 or greater and 55 or less
        cost = 0 
    elif age < 12: # less than 12
        cost = 5
    elif age >= 12 and age < 18: # 12 or greater and less than 18
        cost = 7
    elif age >= 18: # 18 or over
        cost = 12
    photo = input("Want photos? Y or N: ").lower()
    if photo == 'y':
        cost += 3

print(f"Total Cost ${cost}")