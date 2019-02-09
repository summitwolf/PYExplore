"""
Exercise 5: Write a program to read through the mail box data
and when you ﬁnd line that starts with “From”, you will split
the line into words using the split function. We are interested
in who sent the message, which is the second word on the From line.

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

You will parse the From line and print out the second word for each From
line, then you will also count the number of From (not From:) lines and print
out a count at the end. 
"""

fhand = open("mbox-short.txt")
fromCount = 0
for line in fhand:
    words = line.split()
    # only parse lines that start with 'from' and have at least 2 words
    if (not line.startswith('From')) or (len(words) < 2): continue;
    fromCount += 1
    print(words[1])

print('There were ' + str(fromCount) + ' lines in the file with From as the first word.')
