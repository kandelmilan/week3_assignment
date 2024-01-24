"""
Write a function concat_tuples(tuple1, tuple2) that takes two tuples as arguments and 
returns a new tuple containing elements from both tuples.
"""


def concat_tuples(tuple1, tuple2):
    tuple3 = tuple1+tuple2
    return tuple3


tuple1 = [1, 2, 3]
tuple2 = [4, 5, 6]
tuple3 = concat_tuples(tuple1, tuple2)
print(f"Concatenated Tuple:{tuple3}")


"""
to take a tuples as from a terminal 
input_tuple1 = input("Enter elements separated by commas: ")
elements_list = input_tuple1.split(',')
input_tuple = tuple(elements_list)
print("Input Tuple:", input_tuple)
"""
