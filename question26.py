"""
Create a tuple with elements 'apple', 'banana', and 'cherry'.
Unpack the tuple into three variables and print them.
"""

tuple1 = ('apple', 'banana',  'cherry')
for i in tuple1:
    print(f"the variable in tuple1 is {i}\n")


# another method

first_tuple, second_tuple, third_tuple = tuple1
print(f"the first variable in tuple is {first_tuple}")
print(f"the second variable in tuple is {second_tuple}")
print(f"the third variable in tuple is {third_tuple}")
