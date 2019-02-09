"""
Exercise 2: Figure out which line of the above program is still
not properly guarded. See if you can construct a text ﬁle which
causes the program to fail and then modify the program so that
the line is properly guarded and test it to make sure it handles
your new text ﬁle.
"""

# Was not properly guarded for lines where 'from' is followed by less than 2 words.
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 2: continue
    if words[0] != 'From' : continue
    print(words[2])

