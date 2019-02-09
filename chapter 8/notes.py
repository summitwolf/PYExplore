
# lists can contain differing datatypes
myList = ['spam', 2.0, 5, [10, 20]]

#if you read/write to an nonexistant eliment, you get an index error

'spam' in myList # returns true

# negative indicies wrap backwards to end of list

# common way to traverse a list while getting the index
for i in range(len(myList)):
    print(myList[i])

# list operations
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c) # [1, 2, 3, 4, 5, 6]
print(a*3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# slice operator also works on lists
c[1:3] # [2, 3]
t = ['a', 'b', 'b', 'd', 'e', 'f']
t[1:3] = ['x']*2
print(t)

t.append('g')
t.extend(['j', 'i', 'h'])
print(t)
t.sort()
print(t)

#lists and strings

s = 'spam'
t = list(s)
print(t)

s = 'the quick brown fox'
t = s.split()
print(t)
#split can take an argument for a different dilimeter than ' '
#str.join(list of words) will make a string with tr inbetween elements
print(' '.join(t))

# pop removes the element and returns it
w = t.pop(1)
print(t)
print(w)

# del deletes element. Can be sliced.
del t[1]
