# Assignment 9

"""
We have 2 variables. fr and d. fr is a list of strings and d is a dictionary with email
addresses as keys and numbers as values (numbers in string format).
Write code to replace the email address in each of the strings in the fr list with
the associated value of that email looked up from the dictionary d.
If the dictionary does not contain the email found in the list, add a new entry
in the dictionary for the email found in the fr list. The value for this new email key
will be the next highest value number in the dictionary in string format.

Once the dictionary is populated with this new email key and a new number value,
replace that email's occurrence in the fr list with the number value.

The output of running your completed code should be the following:

Value of fr:
['199|4|11|GDSPV', '199|16|82|GDSPV', '205|12|82|GDSPV', '206|19|82|GDSPV']
Value of d:
{'7@comp1.COM': '199', '8@comp4.COM': '200', '13@comp1.COM': '205', '26@comp1.COM': '206'}

"""

# Don't manually change fr and d.
fr = [
'7@comp1.COM|4|11|GDSPV',
'7@comp1.COM|16|82|GDSPV',
'13@comp1.COM|12|82|GDSPV',
'26@comp1.COM|19|82|GDSPV'
]

d= {
'7@comp1.COM': '199',
'8@comp4.COM': '200',
'13@comp1.COM': '205'
}


# Your Code Below:
# --------------------------------------






# don't change the lines below:
# --------------------------------------
print("Value of fr: ")
print(fr)
print("Value of d:")
print(d)








































# Solution:
#
# line_list = []
# # this won't work for missing keys
# for line in fr:
#     columns = line.split("|")
#     lookup_val = columns[0]
#
#     # if lookup_val not in d.keys():
#     if(d.get(lookup_val) is None): # Can't find in dict
#
#         # get the next number + 1 from dict
#         next_number = int(max(d.values())) + 1
#         d[lookup_val] = str(next_number)
#         columns[0] = str(next_number)
#         line_list.append("|".join(columns))
#     else:
#         columns[0] = d.get(columns[0])
#         line_list.append("|".join(columns))
#
# fr = line_list
#
