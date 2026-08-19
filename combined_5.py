import random
import statistics
import math


# Global variable
college_name = "ABC College"


# ==========================================
# CUSTOM FUNCTIONS
# ==========================================

def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return statistics.mean(marks)


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


def display_student(name, marks):
    # Local variables
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    print("\n----- STUDENT DETAILS -----")
    print("College:", college_name)
    print("Name:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)


# ==========================================
# MAIN PROGRAM
# ==========================================

student_name = "Rahul"
student_marks = [85, 78, 92, 88, 76]

display_student(student_name, student_marks)


# ==========================================
# RANDOM MODULE
# ==========================================

random_number = random.randint(1, 100)

print("\nRandom number:", random_number)


# ==========================================
# STATISTICS MODULE
# ==========================================

print("Mean:", statistics.mean(student_marks))
print("Median:", statistics.median(student_marks))


# ==========================================
# MATH MODULE
# ==========================================

print("Square root of 100:", math.sqrt(100))
print("5 factorial:", math.factorial(5))
print("Value of PI:", math.pi)