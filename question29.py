"""
Given three sets, set1, set2, and set3,
write a program to find and print the intersection of all three sets.
"""

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {4, 5, 8, 9, 10, 11}
intersection_set = set1.intersection(set2, set3)
print(f"the intersection of the three set is {intersection_set}")
