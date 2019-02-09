"""
Exercise 1: Write a function called chop that takes a list and modiﬁes it
, removing the ﬁrst and last elements,
and returns None. Then write a function called middle
that takes a list and returns a new list that contains all
but the ﬁrst and last elements.
"""

def chop(t):
    del t[0]
    del t[-1]

myList = [1,2,3,4,5]
chop(myList)
print(myList)

def middle(t):
    pass
    
