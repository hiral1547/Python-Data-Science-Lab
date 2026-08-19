import random

# Total number of monitoring checks
total_checks = 100

# Counters
healthy_count = 0
issue_count = 0

# --------------------------------
# Server Monitoring
# --------------------------------

for i in range(total_checks):

    # Random variable
    # 0 = Healthy
    # 1 = Issue
    X = random.choice([0, 1])

    if X == 0:
        healthy_count += 1
    else:
        issue_count += 1


# --------------------------------
# Calculate Probability
# --------------------------------

probability_issue = issue_count / total_checks

probability_healthy = healthy_count / total_checks


# --------------------------------
# Display Results
# --------------------------------

print("Cloud Server Monitoring")
print("-----------------------")

print("Total Checks:", total_checks)

print("Healthy Checks:", healthy_count)

print("Issue Checks:", issue_count)

print("\nProbability of Issue:",
      probability_issue)

print("Probability of Healthy:",
      probability_healthy)

print("\nIssue Probability:",
      probability_issue * 100, "%")

print("Healthy Probability:",
      probability_healthy * 100, "%")