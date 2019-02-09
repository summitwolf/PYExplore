"""
Exercise 3: Encapsulate this code in a function named count,
and generalize it so that it accepts the string and the letter as arguments.
"""

def count (_string, _char):
    count = 0
    for char in _string:
        if (char == _char):
            count += 1
    return count

print(count("banana", 'a'))
print(count("baseball", 'q'))
print(count("autopsy", 't'))
