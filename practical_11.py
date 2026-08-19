# Program: Data Analytics and Data Measurement Scales
# Real-world example: Hospital Patient Data

import pandas as pd

# Create patient dataset
data = {
    "Patient_ID": [101, 102, 103, 104, 105, 106],
    "Department": ["Cardiology", "Neurology", "Cardiology",
                   "Orthopedics", "Neurology", "Cardiology"],
    "Age": [45, 60, 35, 50, 40, 70],
    "Pain_Level": [2, 4, 1, 3, 5, 2],
    "Treatment_Cost": [50000, 75000, 30000, 45000, 60000, 80000]
}

df = pd.DataFrame(data)

# Display dataset
print("Hospital Patient Dataset:")
print(df)

# -----------------------------------
# DATA ANALYTICS
# -----------------------------------

print("\n--- Data Analytics ---")

# Basic statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Average patient age
print("\nAverage Patient Age:",
      df["Age"].mean())

# Average treatment cost
print("Average Treatment Cost:",
      df["Treatment_Cost"].mean())

# Highest treatment cost
print("Highest Treatment Cost:",
      df["Treatment_Cost"].max())

# Number of patients in each department
print("\nPatients by Department:")
print(df["Department"].value_counts())


# -----------------------------------
# DATA MEASUREMENT SCALES
# -----------------------------------

print("\n--- Data Measurement Scales ---")

print("Nominal  : Department")
print("Ordinal  : Pain Level")
print("Interval : Temperature (°C)")
print("Ratio    : Age and Treatment Cost")

# Display examples
print("\nExamples:")
print("1. Nominal  -> Department: Cardiology, Neurology")
print("2. Ordinal  -> Pain Level: Low, Medium, High")
print("3. Interval -> Temperature: 36°C, 37°C, 38°C")
print("4. Ratio    -> Age: 25, 40, 60")