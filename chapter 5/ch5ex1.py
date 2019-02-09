"""
Chapter 5, Excercise 2
    Write another program that prompts for a list of numbers as above
    and at the end prints out both the maximum and minimum of the numbers
"""

#get list of values from user
enteredValues = []
userEnteredDone = False
while not userEnteredDone:
    userInput = input("Please enter an integer, float, or type 'done' to finish: ")
    if (userInput == "done"):
        userEnteredDone = True
        print(enteredValues)
    else:
        try:
            enteredValues.append(float(userInput))
        except:
            print("The value you entered was invalid. Please try again.")

minimum = min(enteredValues)
maximum = max(enteredValues)
print("Min: " + str(minimum))
print("Max: " + str(maximum))
