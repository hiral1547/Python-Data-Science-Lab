# Aim: Perform basic operations on Python arrays, lists, tuples, sets, dictionaries, and strings.

# ==========================================
# 1. ARRAY OPERATIONS
# ==========================================

from array import array

arr = array('i', [10, 20, 30, 40, 50])

print("----- ARRAY OPERATIONS -----")
print("Original Array:", arr)

# Accessing an element
print("First element:", arr[0])

# Adding an element
arr.append(60)
print("After append:", arr)

# Inserting an element
arr.insert(2, 25)
print("After insert:", arr)

# Removing an element
arr.remove(40)
print("After remove:", arr)

# Updating an element
arr[0] = 5
print("After update:", arr)


# ==========================================
# 2. LIST OPERATIONS
# ==========================================

numbers = [10, 20, 30, 40, 50]

print("\n----- LIST OPERATIONS -----")
print("Original List:", numbers)

# Accessing
print("First element:", numbers[0])

# Adding
numbers.append(60)
print("After append:", numbers)

# Inserting
numbers.insert(1, 15)
print("After insert:", numbers)

# Removing
numbers.remove(30)
print("After remove:", numbers)

# Sorting
numbers.sort()
print("Sorted List:", numbers)

# Reversing
numbers.reverse()
print("Reversed List:", numbers)


# ==========================================
# 3. TUPLE OPERATIONS
# ==========================================

subjects = ("Python", "Java", "C++", "SQL")

print("\n----- TUPLE OPERATIONS -----")
print("Original Tuple:", subjects)

# Accessing
print("First subject:", subjects[0])

# Slicing
print("First two subjects:", subjects[0:2])

# Count
print("Number of times Python occurs:", subjects.count("Python"))

# Finding index
print("Index of SQL:", subjects.index("SQL"))

# Length
print("Number of subjects:", len(subjects))


# ==========================================
# 4. SET OPERATIONS
# ==========================================

set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

print("\n----- SET OPERATIONS -----")
print("Set A:", set_a)
print("Set B:", set_b)

# Union
print("Union:", set_a | set_b)

# Intersection
print("Intersection:", set_a & set_b)

# Difference
print("Difference:", set_a - set_b)

# Adding an element
set_a.add(70)
print("After adding 70:", set_a)

# Removing an element
set_a.remove(20)
print("After removing 20:", set_a)


# ==========================================
# 5. DICTIONARY OPERATIONS
# ==========================================

student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python",
    "marks": 85
}

print("\n----- DICTIONARY OPERATIONS -----")
print("Original Dictionary:", student)

# Accessing a value
print("Student Name:", student["name"])

# Adding a key-value pair
student["city"] = "Mumbai"
print("After adding city:", student)

# Updating a value
student["marks"] = 90
print("After updating marks:", student)

# Removing a key-value pair
student.pop("age")
print("After removing age:", student)

# Displaying keys
print("Keys:", student.keys())

# Displaying values
print("Values:", student.values())

# Displaying key-value pairs
print("Items:", student.items())


# ==========================================
# 6. STRING OPERATIONS
# ==========================================

text = "Python Programming"

print("\n----- STRING OPERATIONS -----")
print("Original String:", text)

# Accessing characters
print("First character:", text[0])

# Slicing
print("First six characters:", text[:6])

# Length
print("Length:", len(text))

# Uppercase
print("Uppercase:", text.upper())

# Lowercase
print("Lowercase:", text.lower())

# Replace
print("After replacing Python:", text.replace("Python", "Java"))

# Find
print("Position of Programming:", text.find("Programming"))

# Check membership
print("'Python' in text:", "Python" in text)

# Split
print("Split String:", text.split())