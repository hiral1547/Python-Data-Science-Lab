# ===========================================
# Aim: Demonstrate Python variables, built-in data types, and arithmetic, assignment, comparison, 
# logical, membership, identity, and bitwise operators.
# ===========================================


# ==========================================
# 1. VARIABLES AND BUILT-IN DATA TYPES
# ==========================================

# Integer
age = 20

# Float
attendance = 87.5

# String
student_name = "Rahul"

# Boolean
is_registered = True

# List
marks = [85, 78, 92, 88, 76]

# Tuple
subjects = ("Python", "Math", "Science", "English", "Computer")

# Set
skills = {"Python", "SQL", "Git"}

# Dictionary
student = {
    "name": student_name,
    "age": age,
    "attendance": attendance
}

# None
remarks = None

print("Student:", student_name)
print("Age:", age)
print("Attendance:", attendance)
print("Marks:", marks)
print("Subjects:", subjects)
print("Skills:", skills)
print("Student Details:", student)
print("Remarks:", remarks)


# ==========================================
# 2. ARITHMETIC OPERATORS
# ==========================================

total = sum(marks)
number_of_subjects = len(marks)

average = total / number_of_subjects
remainder = total % number_of_subjects
power = age ** 2
integer_division = total // number_of_subjects

print("\n--- Arithmetic Operators ---")
print("Addition:", 10 + 5)
print("Subtraction:", 10 - 5)
print("Multiplication:", 10 * 5)
print("Division:", 10 / 5)
print("Floor Division:", total, "//", number_of_subjects, "=", integer_division)
print("Modulus:", remainder)
print("Power:", power)

print("Total Marks:", total)
print("Average Marks:", average)


# ==========================================
# 3. ASSIGNMENT OPERATORS
# ==========================================

bonus = 5

bonus += 2       # bonus = bonus + 2
bonus -= 1       # bonus = bonus - 1
bonus *= 2       # bonus = bonus * 2
bonus /= 2       # bonus = bonus / 2
bonus //= 2      # bonus = bonus // 2
bonus %= 3       # bonus = bonus % 3

print("\n--- Assignment Operators ---")
print("Final bonus:", bonus)


# ==========================================
# 4. COMPARISON OPERATORS
# ==========================================

print("\n--- Comparison Operators ---")

print("Average == 80:", average == 80)
print("Average != 80:", average != 80)
print("Average > 80:", average > 80)
print("Average < 80:", average < 80)
print("Average >= 40:", average >= 40)
print("Average <= 100:", average <= 100)


# ==========================================
# 5. LOGICAL OPERATORS
# ==========================================

passed_exam = average >= 40
good_attendance = attendance >= 75

print("\n--- Logical Operators ---")

# AND
eligible = passed_exam and good_attendance

# OR
special_case = average >= 90 or attendance >= 90

# NOT
not_registered = not is_registered

print("Passed AND good attendance:", eligible)
print("Excellent marks OR attendance:", special_case)
print("NOT registered:", not_registered)


# ==========================================
# 6. MEMBERSHIP OPERATORS
# ==========================================

print("\n--- Membership Operators ---")

print("'Python' in subjects:", "Python" in subjects)
print("'Java' in subjects:", "Java" in subjects)

print("'Python' in skills:", "Python" in skills)
print("'Java' not in skills:", "Java" not in skills)


# ==========================================
# 7. IDENTITY OPERATORS
# ==========================================

print("\n--- Identity Operators ---")

student_1 = student
student_2 = student.copy()

print("student_1 is student:", student_1 is student)
print("student_1 is student_2:", student_1 is student_2)

print("student_1 == student_2:", student_1 == student_2)


# ==========================================
# 8. BITWISE OPERATORS
# ==========================================

a = 10        # Binary: 1010
b = 6         # Binary: 0110

print("\n--- Bitwise Operators ---")

print("a & b:", a & b)     # AND
print("a | b:", a | b)     # OR
print("a ^ b:", a ^ b)     # XOR
print("~a:", ~a)           # NOT
print("a << 1:", a << 1)   # Left shift
print("a >> 1:", a >> 1)   # Right shift


# ==========================================
# 9. PRACTICAL DECISION USING OPERATORS
# ==========================================

print("\n--- Final Student Evaluation ---")

if average >= 75 and attendance >= 75:
    result = "Distinction"
elif average >= 40 and attendance >= 75:
    result = "Pass"
else:
    result = "Fail"

print("Student:", student_name)
print("Total:", total)
print("Average:", average)
print("Attendance:", attendance)
print("Result:", result)