# Aim: To implement data manipulation using Pandas for Website Traffic Analysis

import pandas as pd

# Website traffic data
data = {
    "Date": [
        "2026-08-01", "2026-08-02", "2026-08-03",
        "2026-08-04", "2026-08-05", "2026-08-06",
        "2026-08-07"
    ],
    "Visitors": [1200, 1500, 1100, 1800, 2000, 1700, 2200],
    "Page_Views": [3500, 4200, 3100, 5200, 6000, 4800, 6500],
    "Bounce_Rate": [45, 42, 50, 38, 35, 40, 32],
    "Conversions": [60, 75, 50, 90, 110, 85, 125]
}

df = pd.DataFrame(data)

print("Original Website Traffic Data:")
print(df)


# 1. Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# 2. Filter days with more than 1500 visitors
print("\n--- Days with More Than 1500 Visitors ---")
print(df[df["Visitors"] > 1500])


# 3. Sort by number of visitors
print("\n--- Sorted by Visitors ---")
print(df.sort_values("Visitors", ascending=False))


# 4. Add Conversion Rate
df["Conversion_Rate"] = (
    df["Conversions"] / df["Visitors"]
) * 100

print("\n--- Data with Conversion Rate ---")
print(df)


# 5. Calculate average values
print("\n--- Average Values ---")
print("Average Visitors:",
      df["Visitors"].mean())

print("Average Page Views:",
      df["Page_Views"].mean())

print("Average Bounce Rate:",
      df["Bounce_Rate"].mean())


# 6. Find the day with highest visitors
highest = df.loc[df["Visitors"].idxmax()]

print("\n--- Highest Traffic Day ---")
print(highest)


# 7. Statistical summary
print("\n--- Statistical Summary ---")
print(df.describe())


# | Operation          | Purpose                   |
# | ------------------ | ------------------------- |
# | `pd.DataFrame()`   | Create dataset            |
# | `pd.to_datetime()` | Convert dates             |
# | Filtering          | Find specific records     |
# | `sort_values()`    | Sort data                 |
# | Creating columns   | Calculate conversion rate |
# | `mean()`           | Calculate averages        |
# | `idxmax()`         | Find highest value        |
# | `describe()`       | Generate statistics       |

# IT companies use website traffic analysis to understand user behavior, monitor website performance, measure conversions, and 
# improve digital marketing strategies.