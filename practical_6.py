# Aim : To write a Python program to create, write, read, and append data 
# to a text file using exception handling.

#====================== Theory =========================================
# File handling in Python is used to store and retrieve data from files. 
# Python provides the built-in open() function for working with files.

# Common file modes are:

# r — Read an existing file.
# w — Write to a file. Creates a new file or overwrites an existing file.
# a — Append data to an existing file.
# r+ — Read and write.

# The with open() statement automatically closes the file after the operation is 
# completed.

# Exception handling is used to handle runtime errors without terminating 
# the program unexpectedly. Python uses try, except, else, and finally blocks 
# for exception handling.

#====================================================================

try:
    # Writing data to the file
    with open("student.txt", "w") as file:
        file.write("101, Rahul, 85\n")
        file.write("102, Priya, 90\n")
        file.write("103, Amit, 78\n")

    # Appending data to the file
    with open("student.txt", "a") as file:
        file.write("104, Neha, 88\n")

    # Reading data from the file
    with open("student.txt", "r") as file:
        data = file.read()

    print("Contents of student.txt:")
    print(data)

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("An error occurred:", e)