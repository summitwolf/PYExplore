"""
Exercise 4: Download a copy of the ﬁle www.py4e.com/code3/romeo.txt.
Write a program to open the ﬁle romeo.txt and read it line by line.
For each line, split the line into a list of words using the split
function. For each word, check to see if the word is already in a
list. If the word is not in the list, add it to the list. When the
program completes, sort and print the resulting words in
alphabeticalorder.
"""
uniqueWords = []
fhand = open("romeo.txt")
for line in fhand:
    words = line.split(' ')
    # chop off '\n'
    for i, word in enumerate(words):
        if '\n' in word:
            print("Caught: " + word)
            words[i] = word[:-1]
            
    # add words to list if not yet included
    for word in words:
        if word not in uniqueWords:
            uniqueWords.append(word)
uniqueWords.sort()
print(uniqueWords)
