import statistics

# Enter dataset
data = list(map(float, input("Enter the data values separated by spaces: ").split()))

# ---------- Central Tendency ----------
mean = statistics.mean(data)
median = statistics.median(data)

try:
    mode = statistics.mode(data)
except statistics.StatisticsError:
    mode = "No unique mode"

# ---------- Dispersion ----------
data_range = max(data) - min(data)
variance = statistics.variance(data)
standard_deviation = statistics.stdev(data)

# ---------- Location ----------
minimum = min(data)
maximum = max(data)
q1 = statistics.quantiles(data, n=4)[0]
q2 = statistics.median(data)
q3 = statistics.quantiles(data, n=4)[2]
iqr = q3 - q1

# ---------- Display Results ----------
print("\n--- Measures of Central Tendency ---")
print("Mean   :", mean)
print("Median :", median)
print("Mode   :", mode)

print("\n--- Measures of Dispersion ---")
print("Range              :", data_range)
print("Variance           :", variance)
print("Standard Deviation :", standard_deviation)

print("\n--- Measures of Location ---")
print("Minimum :", minimum)
print("Q1      :", q1)
print("Q2      :", q2)
print("Q3      :", q3)
print("Maximum :", maximum)
print("IQR     :", iqr)