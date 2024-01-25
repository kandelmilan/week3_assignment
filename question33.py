"""
Write a function merge_dicts(dict1, dict2) that takes two dictionaries as 
arguments and returns a new dictionary containing the combined key-value pairs of both dictionaries. 
If there are common keys, the values from the second dictionary should overwrite the values from the 
first dictionary.
Given the dictionary grades = {'Alice': 90, 'Bob': 85, 'Charlie': 92},
 write a program that calculates and prints the average grade.
"""


def merge_dicts(dict1, dict2):
    dict3 = dict1.copy()
    dict3.update(dict2)
    return dict3


dict_grade = {'Alice': 90, 'Bob': 85, 'Charlie': 92}

avg_grade = sum(dict_grade.values())/len(dict_grade)
print(f"the average  dictionary garde is {avg_grade}.\n ")


dict1 = {"full_name": "rajan kandel", "college_name": "hcoe"}
dict2 = {"full_name": "milan kandel", "father_name": "abcd"}

result = merge_dicts(dict1, dict2)
print(f"after the operation dictionary is {result}\n")


# another method

dict1 = {"full_name": "rajan kandel", "college_name": "hcoe"}
dict2 = {"full_name": "milan kandel", "father_name": "abcd"}

dict_detail = {
    **dict1,
    **dict2,
    "height": "3.45ft"
}
print(dict_detail)
