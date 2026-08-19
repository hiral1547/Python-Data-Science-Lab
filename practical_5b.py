# Aim: To organize Python programs into reusable and 
# modular functions for better code structure and readability.

# Here, the program is organized into separate functions:

# calculate_total() → calculates total marks.
# calculate_average() → calculates average marks.
# calculate_grade() → determines the grade.
# display_result() → displays the final result.

# ==========================================
# STUDENT RESULT PROGRAM
# ==========================================

def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"


def display_result(name, marks):
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    print("\n----- STUDENT RESULT -----")
    print("Name:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)


# Main program
student_name = "Rahul"
student_marks = [85, 78, 92, 88, 76]

display_result(student_name, student_marks)





