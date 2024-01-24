"""
Create two sets, set_a and set_b, each with some common and some unique elements. 
Write a program to find and print the symmetric difference of the two sets.
"""

set_a = {1, 2, 3, 4}
set_b = {4, 5, 6, 7}

difference_set = set_a.symmetric_difference(set_b)
print(f"the difference set {difference_set}\n")
