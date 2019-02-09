fhand = open('mbox.txt')
print(fhand) #returns a file handle. A handle can be used to read the file's data

#When iterating a file handle, python will treat each line like an element.
count = 0
for line in fhand:
    count += 1
print("Lines in mbox.txt: " + str(count))

#Fhand.read returns the file as a single string of characters.
#This is will treat every char as an element.
count = 0
for char in fhand.read():
    count+= 1
print("Chars in mbox.txt: " + str(count))

#simple format for processing only 'interesting' lines
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    # Skip 'uninteresting lines'
    if not line.startswith('From: a'):
        continue
    # Process our 'interesting' line print(line)
    print(line)

#get file name from user
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)

#Making a file requires 'w' as second parameter
fout = open('output.txt', 'w')
line1 = 'I WAS UP LATE NIGHT BALLING. \n'
fout.write(line1)
line2 = 'COUNTING UP HUNDREDS BY THE THOUSANDS. \n'
fout.write(line2)
fout.close()

#detecting newlines and tabs
s = '1 2\t 3\n 4' # \t represents a tab, \n represents a new line
print(repr(s)) # repr(s) will return the string with whitespace characters as backslash sequences




