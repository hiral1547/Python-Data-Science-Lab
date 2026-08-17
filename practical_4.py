# To implement looping and control statements in Python using while loop, 
# for loop, nested loop, break, continue, and pass.


# ==========================================
# 1. WHILE LOOP
# ==========================================

print("----- WHILE LOOP -----")

i = 1

while i <= 5:
    print("Number:", i)
    i += 1


# ==========================================
# 2. FOR LOOP
# ==========================================

print("\n----- FOR LOOP -----")

for i in range(1, 6):
    print("Number:", i)


# ==========================================
# 3. NESTED LOOP
# ==========================================

print("\n----- NESTED LOOP -----")

for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)


# ==========================================
# 4. BREAK STATEMENT
# ==========================================

print("\n----- BREAK STATEMENT -----")

for i in range(1, 10):
    if i == 5:
        break

    print("Number:", i)


# ==========================================
# 5. CONTINUE STATEMENT
# ==========================================

print("\n----- CONTINUE STATEMENT -----")

for i in range(1, 6):
    if i == 3:
        continue

    print("Number:", i)


# ==========================================
# 6. PASS STATEMENT
# ==========================================

print("\n----- PASS STATEMENT -----")

for i in range(1, 6):
    if i == 3:
        pass
    else:
        print("Number:", i)


# ==========================================
# 7. PRACTICAL EXAMPLE
# ==========================================

print("\n----- STUDENT MARKS -----")

marks = [85, 42, 78, 35, 91]

for mark in marks:

    # Skip marks below 40
    if mark < 40:
        continue

    # Stop if marks are greater than 90
    if mark > 90:
        print("Excellent:", mark)
        break

    print("Pass:", mark)


# ==========================================
# 8. PASS WITH CONDITIONAL STATEMENT
# ==========================================

print("\n----- PASS WITH IF -----")

age = 18

if age < 18:
    pass
else:
    print("Person is eligible to vote.")



# | Statement   | Purpose                                           |
# | ----------- | ------------------------------------------------- |
# | `while`     | Repeats a block while a condition is `True`       |
# | `for`       | Iterates through a sequence or range              |
# | Nested loop | A loop inside another loop                        |
# | `break`     | Immediately terminates the loop                   |
# | `continue`  | Skips the current iteration and moves to the next |
# | `pass`      | Does nothing; used as a placeholder               |
