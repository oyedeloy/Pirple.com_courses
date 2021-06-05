"""
This function accepts 3 parameters and checks for equality between any two of them.

The function returns True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.

Strings can also be compared to integers if they are equivalent. For example, if the following values are passed to your function:

6,5,"5"
"""


def compare_num(x, y, z):
    if x == y or x == z or y == z:
        return True
    elif x == int(y) or x == int(z) or y == int(x) or y == int(z) or z == int(x) or z == int(y):
            return True     
    else:
        return False
    
print(compare_num("2", 6, 2))
