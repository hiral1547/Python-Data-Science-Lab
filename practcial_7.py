# Aim : To write a Python program to store and retrieve student records using 
# CSV and binary files.

#==========================Theory=============================================
# A CSV (Comma-Separated Values) file stores tabular data in plain-text form. 
# Each row represents a record, and individual values are separated by commas.

# Python provides the csv module for working with CSV files.

# A binary file stores data in binary format rather than readable text. 
# Python's pickle module can be used to serialize Python objects and store them 
# in binary files.

# Serialization means converting a Python object into a byte stream so that 
# it can be stored in a file.
#=============================================================================

import csv
import pickle

students = [
    [101, "Rahul", 85],
    [102, "Priya", 90],
    [103, "Amit", 78]
]

# Writing data to CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll No", "Name", "Marks"])
    writer.writerows(students)

# Reading data from CSV file
print("Data from CSV file:")
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# Writing data to binary file
with open("students.dat", "wb") as file:
    pickle.dump(students, file)

# Reading data from binary file
print("\nData from Binary file:")
with open("students.dat", "rb") as file:
    data = pickle.load(file)

    for student in data:
        print(student)