# Assignment 4

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

grow_string('Code') → 'CCoCodCode'
grow_string('abc') → 'aababc'
grow_string('ab') → 'aab'

"""

# Your Code Below:


def grow_string(string):
    if len(string) == 0:
        return False

    result = ""
    for i in range(len(string)):
        result += string[:i+1]
    return result


print(grow_string("Code") == "CCoCodCode")
print(grow_string("abc") == "aababc")
print(grow_string("ab") == "aab")



































# Solution:

# def grow_string(str):
#   result = ""
#   # On each iteration, add the substring of the chars 0..i
#   for i in range(len(str)):
#     result = result + str[:i+1]
#   return result

