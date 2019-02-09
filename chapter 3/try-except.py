prompt = "input a number.. "
try:
    number = int(input(prompt))
    print("Your number * 10: " + str(number*10))
except:
    print("you didn't enter a number")
