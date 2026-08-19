# Data Analysis: Univariate, Bivariate and Multivariate
# Real-world example: Supermarket Sales

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create supermarket sales dataset
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone",
                "Tablet", "Laptop", "Phone", "Tablet", "Laptop"],
    "Sales": [80000, 50000, 30000, 75000, 55000,
              35000, 90000, 60000, 40000, 85000],
    "Quantity": [2, 5, 4, 2, 6, 5, 3, 7, 6, 2],
    "Profit": [12000, 8000, 5000, 11000, 9000,
               6000, 15000, 10000, 7000, 13000]
}

df = pd.DataFrame(data)

print("Supermarket Sales Dataset:")
print(df)


# --------------------------------
# 1. UNIVARIATE ANALYSIS
# --------------------------------

print("\n--- Univariate Analysis ---")

# Analyze Sales
print("\nSales Statistics:")
print(df["Sales"].describe())

# Histogram
plt.figure(figsize=(6, 4))
plt.hist(df["Sales"], bins=5)
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.title("Sales Distribution")
plt.show()


# --------------------------------
# 2. BIVARIATE ANALYSIS
# --------------------------------

print("\n--- Bivariate Analysis ---")

# Sales vs Profit
correlation = df["Sales"].corr(df["Profit"])

print("Correlation between Sales and Profit:", correlation)

# Scatter plot
plt.figure(figsize=(6, 4))
plt.scatter(df["Sales"], df["Profit"])
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.title("Sales vs Profit")
plt.show()


# --------------------------------
# 3. MULTIVARIATE ANALYSIS
# --------------------------------

print("\n--- Multivariate Analysis ---")

# Correlation between numerical variables
print("\nCorrelation Matrix:")
print(df[["Sales", "Quantity", "Profit"]].corr())

# Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(
    df[["Sales", "Quantity", "Profit"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Sales Data Correlation")
plt.show()

# Pair plot
sns.pairplot(df[["Sales", "Quantity", "Profit"]])
plt.show()