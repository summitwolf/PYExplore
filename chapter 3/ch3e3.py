#Excercise 3 - Score to Grade

#retrieve score from user
while True:
    try:
        print('')
        score = float(input('Please enter a score between 0.0 and 1.0: '))
        if (0.0 <= score and score <= 1.0 ):
            break
        else:
            print('That number is not between 0.0 and 1.0')
    except:
        print('The value you entered was not a number.')

#convert score to grade
grade = ''
if score >= 0.9:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
else:
    grade = 'F'
print('Your grade is: ' + grade)
    




