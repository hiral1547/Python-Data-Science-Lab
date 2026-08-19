# Aim: To explore and analyze the statistical properties of software 
# bug resolution time using the stats package from SciPy.

# Exploring Statistics using SciPy Stats
# IT Example: Software Bug Resolution Time

from scipy import stats

# Bug resolution time in hours
resolution_time = [
    2, 3, 4, 5, 3,
    6, 8, 4, 5, 10,
    7, 3, 12, 6, 5
]

print("Bug Resolution Time (hours):")
print(resolution_time)

# --------------------------------
# Central Tendency
# --------------------------------

print("\n--- Central Tendency ---")

print("Mean   :", stats.tmean(resolution_time))
print("Median :", stats.median(resolution_time))
print("Mode   :", stats.mode(resolution_time).mode)


# --------------------------------
# Dispersion
# --------------------------------

print("\n--- Dispersion ---")

print("Variance           :", stats.tvar(resolution_time))
print("Standard Deviation :", stats.tstd(resolution_time))


# --------------------------------
# Shape of Data
# --------------------------------

print("\n--- Shape of Data ---")

print("Skewness :", stats.skew(resolution_time))
print("Kurtosis :", stats.kurtosis(resolution_time))


# --------------------------------
# Minimum and Maximum
# --------------------------------

print("\n--- Minimum and Maximum ---")

print("Minimum Time :", min(resolution_time), "hours")
print("Maximum Time :", max(resolution_time), "hours")


# --------------------------------
# Percentiles
# --------------------------------

print("\n--- Percentiles ---")

print("25th Percentile :", stats.scoreatpercentile(resolution_time, 25))
print("50th Percentile :", stats.scoreatpercentile(resolution_time, 50))
print("75th Percentile :", stats.scoreatpercentile(resolution_time, 75))


# This helps an IT company understand:
    # Average time taken to fix a bug.
    # How much bug resolution time varies.
    # The typical resolution time using the median.
    # Whether a few bugs take unusually long to resolve.

# In a real IT company : 

    # These values would normally come from a bug-tracking system such as Jira, 
    # Azure DevOps, or a similar tool.

    # For example:
        # Bug #101 → Created: 9:00 AM → Fixed: 11:00 AM → 2 hours
        # Bug #102 → Created: 10:00 AM → Fixed: 1:00 PM  → 3 hours
        # Bug #103 → Created: 8:00 AM → Fixed: 12:00 PM → 4 hours

        # Then Python can read those real records and calculate the statistics.