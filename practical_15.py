# Aim: To perform numerical computing and analyze multidimensional server monitoring data 
# stored in a CSV file using NumPy.

# Create server_data.csv

import numpy as np

# Read data from CSV file
data = np.genfromtxt(
    "server_data.csv",
    delimiter=",",
    skip_header=1,
    dtype=None,
    encoding="utf-8"
)

# Extract server names
servers = data["f0"]

# Extract numerical data
server_data = np.column_stack((
    data["f1"],
    data["f2"],
    data["f3"]
))

print("Server Monitoring Data:")
print(server_data)

# Shape of multidimensional array
print("\nArray Shape:", server_data.shape)

# Average usage
print("\nAverage CPU Usage:",
      np.mean(server_data[:, 0]), "%")

print("Average Memory Usage:",
      np.mean(server_data[:, 1]), "%")

print("Average Network Usage:",
      np.mean(server_data[:, 2]), "%")

# Maximum usage
print("\nMaximum CPU Usage:",
      np.max(server_data[:, 0]), "%")

print("Maximum Memory Usage:",
      np.max(server_data[:, 1]), "%")

print("Maximum Network Usage:",
      np.max(server_data[:, 2]), "%")

# Minimum usage
print("\nMinimum CPU Usage:",
      np.min(server_data[:, 0]), "%")

print("Minimum Memory Usage:",
      np.min(server_data[:, 1]), "%")

print("Minimum Network Usage:",
      np.min(server_data[:, 2]), "%")

# Find servers with CPU usage above 75%
high_cpu = server_data[:, 0] > 75

print("\nServers with CPU Usage Above 75%:")

for server in servers[high_cpu]:
    print(server)


# The program uses:

#     np.genfromtxt() → Reads the CSV file.
#     np.column_stack() → Creates a multidimensional NumPy array.
#     np.mean() → Calculates average resource usage.
#     np.max() / np.min() → Finds maximum and minimum usage.
#     Boolean indexing → Finds servers with CPU usage above 75%.

# Real IT use: This is similar to how an IT team can analyze monitoring data 
# to identify overloaded servers and optimize infrastructure resources.

# Server data would normally come from server monitoring tools such as:
#     AWS CloudWatch, Microsoft Azure Monitor, Google Cloud Monitoring, and 
#     Other server monitoring systems