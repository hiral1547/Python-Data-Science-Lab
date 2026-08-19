# Student Performance Analysis

import pandas as pd
import matplotlib.pyplot as plt

# Create a dataset
data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Study_Hours": [2, 4, 5, 7, 8],
    "Marks": [45, 55, 65, 80, 90]
}

df = pd.DataFrame(data)

# 1. Display the data
print("Student Data:")
print(df)

# 2. Data analysis
print("\n--- Data Analysis ---")
print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

# 3. Find student with highest marks
top_student = df.loc[df["Marks"].idxmax(), "Student"]
print("Top Student:", top_student)

# 4. Visualization
plt.scatter(df["Study_Hours"], df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()