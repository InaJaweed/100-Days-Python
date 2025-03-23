print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni? Y or N: ").lower()
extraCheese = input("Do you want extra cheese? Y or N: ").lower()

cost = 0

if size == 's':
    cost = 15
elif size == 'm':
    cost = 20  
elif size == 'l':
    cost = 25


if pepperoni == 'y':
    if size == 's':
        cost += 2
    else:
        cost += 3

if extraCheese == 'y':
    cost += 1

print(f"Total Cost ${cost}")