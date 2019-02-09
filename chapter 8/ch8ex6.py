"""
Chapter 8, Excercise 6
     Write a program which repeatedly reads numbers until the user enters “done”.
     Once “done” is entered, print out the total, count, and average of the
     numbers. If the user enters anything other than a number, detect their
     mistakeusing try and except and print an error message and skip to the next
     number.
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
print("Minimum: " + str(minimum))
print("Maximum: " + str(maximum))
