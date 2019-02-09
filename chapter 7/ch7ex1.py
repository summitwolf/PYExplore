"""
Exercise 1: Write a program to read through a ﬁle and
print the contents of the ﬁle (line by line) all in upper case.
"""
try:
    fhand = open('mbox-short.txt')
except:
    print('no file named mbox-short.txt')
    quit()
for line in fhand:
    line = line.upper()
    print(line)
