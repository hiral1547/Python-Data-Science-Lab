# Aim: To implement conditional statements in Python using if, if...else, elif, and Boolean expressions.
# ==========================================
# 1. IF STATEMENT
# ==========================================

age = 20

print("----- IF STATEMENT -----")

if age >= 18:
    print("The person is eligible to vote.")


# ==========================================
# 2. IF...ELSE STATEMENT
# ==========================================

marks = 65

print("\n----- IF...ELSE STATEMENT -----")

if marks >= 40:
    print("Student has passed.")
else:
    print("Student has failed.")


# ==========================================
# 3. ELIF STATEMENT
# ==========================================

percentage = 82

print("\n----- ELIF STATEMENT -----")

if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

print("Percentage:", percentage)
print("Grade:", grade)


# ==========================================
# 4. BOOLEAN EXPRESSIONS
# ==========================================

age = 21
has_id = True

print("\n----- BOOLEAN EXPRESSIONS -----")

print("Age >= 18:", age >= 18)
print("Has ID:", has_id)

if age >= 18 and has_id:
    print("Entry is allowed.")
else:
    print("Entry is not allowed.")


# ==========================================
# 5. PRACTICAL EXAMPLE
# ==========================================

marks = 78
attendance = 85

print("\n----- STUDENT ELIGIBILITY -----")

if marks >= 75 and attendance >= 75:
    print("Student is eligible for distinction.")
elif marks >= 40 and attendance >= 75:
    print("Student has passed.")
elif marks >= 40 and attendance < 75:
    print("Student passed but attendance is insufficient.")
else:
    print("Student has failed.")


# | Statement          | Purpose                                | Example                            |
# | ------------------ | -------------------------------------- | ---------------------------------- |
# | `if`               | Executes code when a condition is true | `if age >= 18:`                    |
# | `if...else`        | Chooses between two conditions         | `if marks >= 40 ... else`          |
# | `elif`             | Checks multiple conditions             | `elif percentage >= 75:`           |
# | Boolean expression | Produces `True` or `False`             | `age >= 18`                        |
# | `and`              | Both conditions must be true           | `marks >= 40 and attendance >= 75` |
# | `or`               | At least one condition must be true    | `marks >= 90 or attendance >= 90`  |
# | `not`              | Reverses a Boolean value               | `not has_id`                       |
