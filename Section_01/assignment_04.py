# Assignment 4:
"""
    Given 2 variables word1 and word2, write code to
    print the concatenation of the 2 words omitting the
    first_folder letter of the string saved in word1 and the second_folder
    letter of the string saved in word2.

    Example:
    ---------------
    word1 = "Vehicle"
    word2 = "Robot"
    result - ehicleRbot

"""

word1 = "Computer"
word2 = "Truck"

# Expected Result Printed: omputerTuck

# Your code below:
lst =(word1,word2)
c=0
result = ''
for x in lst:
    w=x[:c]+x[c+1:]+' '
    result += w
    c += 1
print(result)





























# Solution Below:
# result = word1[1:] + word2[0:1] + word2[2:]
# print(result)


