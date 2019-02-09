"""
Exercise 2: Write a program to prompt for a ﬁle name,
and then read through the ﬁle and look for lines of the form:

X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with “X-DSPAM-Conﬁdence:”
pull apart the line to extract the ﬂoating-point number on the line.
Count these lines and then compute the total of the spam conﬁdence
values from these lines. When you reach the end of the ﬁle,
print out the average spam conﬁdence.

-------------------------------------------------------------------------

Exercise 3: Sometimes when programmers get bored or want to have a bit of
fun, they add a harmless Easter Egg to their program. Modify the program
that prompts the user for the ﬁle name so that it prints a funny message
when the user types in the exact ﬁle name “na na boo boo”. The program
should behave normally for all other ﬁles which exist and don’t exist.
"""

#get file from user
try:
    fInput = input('Enter a file name: ')
    fhand = open(fInput)
except:
    if (fInput == 'na na boo boo'):
        print("NA NA BOO BOO TO YOU - You have been punk'd")
    print('no file named', fInput)
    quit()

#put all confidence values into a list
count = 0
confidences = []
for line in fhand:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence: '):
        continue
    #process lines that fit criteria
    confidenceIndex = line.find(' ')
    confidence = line[confidenceIndex + 1:]
    confidences.append(float(confidence))
    count+= 1
print('Confidence count: ', count)
average = (sum(confidences)/count)
print('Average confidence:', average)
