"""
Create a nested dictionary called students with keys as student names and values
as dictionaries containing 'age' and 'grade' for each student. Add information for at least three students. 
Write a function update_grade(student_dict, student_name, new_grade) that takes a dictionary of students,
the name of a student,and a new grade. Update the grade of the specified student and return the modified dictionary.
 
Given a list of names, create a dictionary where the keys are names and the values are the 
lengths of the corresponding names.
"""
student = {
    "ram": {"age": 20, "grade": 12},
    "sita": {"age": 19, "grade": 12},
    "shyam": {"age": 19, "grade": 12},
}


def update_grade(student_dict, student_name, new_grade):
    if student_name in student_dict:
        student_dict[student_name]['grade'] = new_grade
        print(f"Grade for {student_name} updated to {new_grade}")
    else:
        print(f"Student {student_name} not found in the dictionary.")

    return student_dict


students = update_grade(student, 'hari', 18)
names_list = ['ram', 'sita', 'shyam']
names_lengths = {name: len(name) for name in names_list}

# Print the results
print("Nested Dictionary (students):", students)
print("Dictionary with Name Lengths:", names_lengths)



