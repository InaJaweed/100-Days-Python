for num in range(1, 101):
    output = ""
    if num % 3 == 0 :
        output += "Fizz"
    if num % 5 == 0:
        output += "Buzz"
    print(output or num)