# Exercise 2 - Pay program which avoids errors.

while True:
    try:
        hours = float(input("enter hours: "))
        rate = float(input("enter rate: "))
        break
    except:
        print('please enter a number.')

pay = hours * rate
print('your pay is : ' + str(pay))
