# Aim: To create and reference variables using appropriate scope and 
# demonstrate the use of local and global variables in Python.

# ==========================================
# Local Variable
# ==========================================

def student_details():
    name = "Rahul"       # Local variable
    age = 20             # Local variable

    print("Name:", name)
    print("Age:", age)


student_details()

# ==========================================
# Global Variable
# ==========================================

college = "ABC College"     # Global variable

def display_college():
    print("College:", college)


display_college()

print("Outside function:", college)

# ==========================================
# Using the global Keyword
# ==========================================

counter = 0

def increase_counter():
    global counter
    counter += 1

increase_counter()
increase_counter()
increase_counter()

print("Counter:", counter)

# ============================================================
# Creating and Referencing Variables Using Appropriate Scope
# ============================================================

college = "ABC College"       # Global variable
course = "Python"             # Global variable


def student_info():
    name = "Rahul"            # Local variable
    marks = 85                 # Local variable

    print("Name:", name)
    print("Marks:", marks)
    print("College:", college)
    print("Course:", course)


student_info()