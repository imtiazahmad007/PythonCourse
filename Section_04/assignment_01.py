# Assignment 1

"""

Create a method called twelver that accepts 2 integer arguments: a and b.
The method should return True if one of the arguments is 12
or if the sum of both arguments equals 12.

twelver(3, 12) → True
twelver(4, 9) → False
twelver(9, 3) → True

"""


# Your Code Below:
def twelver(one, two):
    if (type(one) == int or type(one) == float) and (type(two) == int or type(two) == float):
        pass
    else:
        return False

    if one == 12 or two == 12 or one+two == 12:
        return True
    return False


print(twelver(3, 12))
print(twelver(4, 9))
print(twelver(9, 3))
print(twelver(5.5, 6.5))
print(twelver("a", "1"))







































# Solution:
# def twelver(a, b):
#   return (a == 12 or b == 12 or a+b == 12)