"""
Write a function list_to_set(input_list) that takes a list as input and returns
a set containing unique elements from the list.
"""


def list_to_set(input_list):
    unq_set = set(input_list)
    return unq_set


input_list = [1, 2, 2, 3, 3, 3, 4, 4, 4]
result = list_to_set(input_list)
print(f"set containing unique elements from the list is {result}.")
