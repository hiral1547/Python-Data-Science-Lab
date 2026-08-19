# Aim: To define, call, and use custom functions in Python with parameters and return values.

# ==========================================
# 1. BASIC CUSTOM FUNCTION
# ==========================================

def greet():
    print("Welcome to Python Programming!")


# Calling the function
greet()


# ==========================================
# 2. FUNCTION WITH PARAMETERS
# ==========================================

def greet_student(name):
    print("Hello", name)


greet_student("Rahul")
greet_student("Priya")


# ==========================================
# 3. FUNCTION WITH RETURN VALUE
# ==========================================

def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)

print("Sum:", result)


# ==========================================
# 4. FUNCTION FOR CALCULATING AVERAGE
# ==========================================

def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


marks = [80, 75, 90, 85, 70]

average = calculate_average(marks)

print("Marks:", marks)
print("Average:", average)