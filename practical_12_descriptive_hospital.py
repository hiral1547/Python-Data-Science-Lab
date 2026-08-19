# Descriptive Statistics - Hospital Patient Waiting Time

# Example: Hospital Patient Data

# Descriptive statistics can be used to analyze patient waiting times in a hospital.

# Suppose the waiting times are:

# 10, 15, 20, 20, 25, 30, 35, 60 minutes

# Central Tendency: Find the average or typical waiting time.
# Dispersion: Find how much waiting times vary.
# Measure of Location: Find whether a patient's waiting time is in the lower or 
# higher part of the dataset.
# Shape and Symmetry: Check whether most patients have similar waiting 
# times or whether a few patients have unusually long waits.

# Real-world use: The hospital can use this information to identify delays, 
# improve staff scheduling, and reduce patient waiting time.

import pandas as pd
from scipy import stats

# Patient waiting times in minutes
waiting_time = [10, 15, 20, 20, 25, 30, 35, 60]

data = pd.Series(waiting_time)

print("Patient Waiting Time Data:")
print(data.tolist())

# -----------------------------------------
# 1. Measures of Central Tendency
# -----------------------------------------

print("\n--- Central Tendency ---")

print("Mean   :", data.mean())
print("Median :", data.median())
print("Mode   :", data.mode().tolist())


# -----------------------------------------
# 2. Measures of Dispersion / Variation
# -----------------------------------------

print("\n--- Dispersion / Variation ---")

print("Range              :", data.max() - data.min())
print("Variance           :", data.var())
print("Standard Deviation :", data.std())


# -----------------------------------------
# 3. Measures of Location
# -----------------------------------------

print("\n--- Measures of Location ---")

print("Minimum :", data.min())
print("Q1      :", data.quantile(0.25))
print("Q2      :", data.quantile(0.50))
print("Q3      :", data.quantile(0.75))
print("Maximum :", data.max())
print("IQR     :", data.quantile(0.75) - data.quantile(0.25))


# -----------------------------------------
# 4. Shape and Symmetry
# -----------------------------------------

print("\n--- Shape and Symmetry ---")

skewness = stats.skew(data)
kurtosis = stats.kurtosis(data)

print("Skewness :", skewness)
print("Kurtosis :", kurtosis)

if skewness > 0:
    print("Shape: Right Skewed")
elif skewness < 0:
    print("Shape: Left Skewed")
else:
    print("Shape: Symmetric")

if abs(skewness) < 0.5:
    print("Symmetry: Approximately Symmetric")
else:
    print("Symmetry: Not Symmetric")