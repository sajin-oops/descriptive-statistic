import statistics

# Example list of numbers
data = [10, 15, 20, 25, 30, 30]

# Calculate various statistical measures using built-in functions
mean = statistics.mean(data)               # Mean
median = statistics.median(data)           # Median
mode = statistics.mode(data)               # Mode
variance = statistics.variance(data)       # Variance (for a sample)
std_dev = statistics.stdev(data)           # Standard Deviation (for a sample)

# Output the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")

#O/P 
Mean: 21.666666666666668
Median: 22.5
Mode: 30
Variance: 66.66666666666667
Standard Deviation: 8.16496580927726