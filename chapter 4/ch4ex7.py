"""
CH4 - Excercise 7
Computes grade with a function
"""

#converts score to letter grade
def computeGrade(score):
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
    return grade

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

grade = computeGrade(score)
print('Your grade is: ' + grade)
    


