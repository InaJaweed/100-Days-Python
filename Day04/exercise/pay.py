import random

friends = ["Bob", "Alice", "James", "Sam"]

pay = random.randint(0, len(friends) - 1)

print(f"Your turn to pay: {friends[pay]}")