"""
Chapter 8, Excercise 7
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

total = sum(enteredValues)
count = len(enteredValues)
if (count > 0):
    average = total/count
else:
    average = "N/A"
print("Total: " + str(total))
print("Count: " + str(count))
print("Average: " + str(average))
