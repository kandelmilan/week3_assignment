"""
Given a tuple with repeated elements,
 write a program to count the occurrences of a specific element within the tuple.
"""
tuple_element = (1, 2, 3, 2, 4, 2, 5, 6, 2, 2, 2, 2, 8)

element_to_count = 2

count = tuple_element.count(element_to_count)
print(f"the occurrences of a {element_to_count} within the tuple is {count}")
