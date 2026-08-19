# Descriptive Statistics
# Real-world example: Employee Salaries

import pandas as pd
from scipy import stats

# Employee salary data (in thousands)
salary = [25, 28, 30, 32, 35, 35, 38, 40, 42, 45, 50, 80]

data = pd.Series(salary)

print("Employee Salary Dataset:")
print(data.tolist())

# -----------------------------------------
# 1. MEASURES OF CENTRAL TENDENCY
# -----------------------------------------

print("\n--- Measures of Central Tendency ---")

print("Mean   :", data.mean())
print("Median :", data.median())
print("Mode   :", data.mode().tolist())


# -----------------------------------------
# 2. MEASURES OF DISPERSION / VARIATION
# -----------------------------------------

print("\n--- Measures of Dispersion ---")

print("Range              :", data.max() - data.min())
print("Variance           :", data.var())
print("Standard Deviation :", data.std())


# -----------------------------------------
# 3. MEASURES OF LOCATION
# -----------------------------------------

print("\n--- Measures of Location ---")

print("Minimum :", data.min())
print("Q1      :", data.quantile(0.25))
print("Q2      :", data.quantile(0.50))
print("Q3      :", data.quantile(0.75))
print("Maximum :", data.max())
print("IQR     :", data.quantile(0.75) - data.quantile(0.25))


# -----------------------------------------
# 4. SHAPE AND SYMMETRY
# -----------------------------------------

print("\n--- Shape and Symmetry ---")

skewness = stats.skew(data)
kurtosis = stats.kurtosis(data)

print("Skewness :", skewness)
print("Kurtosis :", kurtosis)

if skewness > 0:
    print("Shape: Positively Skewed (Right Skewed)")
elif skewness < 0:
    print("Shape: Negatively Skewed (Left Skewed)")
else:
    print("Shape: Approximately Symmetric")

if abs(skewness) < 0.5:
    print("Symmetry: Approximately Symmetric")
else:
    print("Symmetry: Not Symmetric")


# -----------------------------------------
# 5. COMPLETE SUMMARY
# -----------------------------------------

print("\n--- Complete Statistical Summary ---")
print(data.describe())


# What the program calculates

# Category	                        Measures
# ---------------------------------------------------------------------------
# Central Tendency	                Mean, Median, Mode
# Dispersion/Variation	            Range, Variance, Standard Deviation
# Location	                        Minimum, Q1, Median, Q3, Maximum, IQR
# Shape & Symmetry	                Skewness, Kurtosis

# Real-world application: This program can help a company analyze employee salaries to 
# understand the typical salary, salary variation, distribution, and whether a few 
# highly paid employees are affecting the overall distribution.