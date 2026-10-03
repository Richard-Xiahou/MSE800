# Reading Traceback – Activity
# You are given a Python program that contains several errors. Your task is to run the program, 
# read the traceback, identify the type and location of each error, and correct the program.
#  Start by copying the following code into Python Tutor or your Python environment and run it:

def calculate_average(marks):
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)

students = {
    "Ali": [70, 80, 65],
    "Sara": [85, 90, 88],
    "John": [60, 55, 70]
}
for name, marks in students.items():
    average = calculate_average(marks)
    print(name, "average:", average)

highest = max(students)
print("Student with highest marks:", highest)

print("Result:", results)

# we can also test the program online: https://pythontutor.com/visualize.html#mode=display