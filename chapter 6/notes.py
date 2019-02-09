fruit = 'banana'
letter = fruit[1]
print(letter) #letter ia 'a'

lastLetter = fruit[len(fruit) - 1] #Without '-1', index is out of range.
lastLetter = fruit[-1] #this also works

#string segments are called slices.
s = 'Monty Python'
print(s[0:5])

#ommitting an index
print(fruit[:3])
print(fruit[3:])

#strings are immmutable. fruit[0] = 'k' would return an error.

#in operator
'a' in 'abc' # true
'box' in 'this box' #true
'hat' in 'the quick brown fox' # false

#comparing two strings with '>' or '<' can tell you which is first alphabetically

word = 'banana'
index = word.find('na')
#index is 2
index = word.find('na', 3) #starts looking at index 3, index is 4.

#strip() removess white spaced from beginning and end.

#startswith() returns true if string starts with argument

num = 23
thing = 'camels'
country = 'America'
print('There are %d %s in %s.' % (num, thing, country))
