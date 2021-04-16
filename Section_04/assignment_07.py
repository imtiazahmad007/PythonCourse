# Assignment 7
"""
Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the same
place in both strings.

EXAMPLE:
    string_match('xxcaazz', 'xxbaaz') → 3
    string_match('abc', 'abc') → 2
    string_match('abc', 'axc') → 0

"""

#Your Code Below:

def string_match(str1, str2):
    set1 = set()
    for ii in range(len(str1)-1):
        my_str = str1[ii]+str1[ii+1]
        set1.add(my_str)

    set2 = set()
    for ii in range(len(str2)-1):
        my_str = str2[ii]+str2[ii+1]
        set2.add(my_str)

    return len(set1.intersection(set2))


print(string_match("xxcaazz", "xxbaaz") == 3)
print(string_match("abc", "abc") == 2)
print(string_match("abc", "axc") == 0)




























# Solution
# def string_match(a, b):
#     # Figure which string is shorter.
#     shorter = min(len(a), len(b))
#     count = 0
#
#     # Loop i over every substring starting spot.
#     # Use length-1 here, so can use char str[i+1] in the loop
#     for i in range(shorter - 1):
#         a_sub = a[i:i + 2]
#         b_sub = b[i:i + 2]
#         if a_sub == b_sub:
#             count = count + 1
#
#     return count
