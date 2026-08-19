# Part E: Creating Your Own Module

## Aim

To create a user-defined Python module and import and use its functions in another Python program.

---

## Theory

A **module** in Python is a file containing Python code such as functions, variables, and classes. Modules help us organize programs into smaller, reusable components.

A user-defined module can be created by saving Python code in a file with the `.py` extension. The module can then be imported into another Python program using the `import` statement.

---

## Step 1: Create a User-Defined Module

Create a file named **`my_module.py`**.

### `my_module.py`

```python
# User-defined module

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def square(n):
    return n * n

```

## Step 2: Import and Use the Module

Create another file named **`main.py`** in the same folder.

### `my_module.py`

```python
# main.py

import my_module

print("Addition:", my_module.add(10, 5))

print("Subtraction:", my_module.subtract(10, 5))

print("Multiplication:", my_module.multiply(10, 5))

print("Square:", my_module.square(5))

```
```
Part E: Creating Your Own Module
Aim

To create a user-defined Python module and import and use its functions in another Python program.

Theory

A module in Python is a file containing Python code such as functions, variables, and classes. Modules help us organize programs into smaller, reusable components.

A user-defined module can be created by saving Python code in a file with the .py extension. The module can then be imported into another Python program using the import statement.

Step 1: Create a User-Defined Module

Create a file named my_module.py.

# my_module.py


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def square(n):
    return n * n
Step 2: Import and Use the Module

Create another file named main.py in the same folder.

# main.py


import my_module

print("Addition:", my_module.add(10, 5))
print("Subtraction:", my_module.subtract(10, 5))
print("Multiplication:", my_module.multiply(10, 5))
print("Square:", my_module.square(5))


Output
Addition: 15
Subtraction: 5
Multiplication: 50
Square: 25
Step 3: Import Specific Functions

Instead of importing the complete module, specific functions can be imported.

from my_module import add, square


print("Addition:", add(20, 10))
print("Square:", square(6))
Output
Addition: 30
Square: 36
Explanation
my_module.py is the user-defined module.
The def keyword is used to create functions inside the module.
import my_module imports the complete module.
my_module.add() accesses the add() function from the module.
from my_module import add, square imports only the required functions.
Modules make Python programs organized, reusable, and easier to maintain.
Folder Structure
Python_Practical/
│
├── my_module.py
└── main.py
Conclusion

Thus, a user-defined Python module was successfully created and imported into another Python program. The functions defined in the module were successfully accessed and executed.

```