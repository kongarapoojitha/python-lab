
# MINI PROJECT: JSON-Based Log File Analyzer

import json
import os

log_file = "application.log"
json_file = "log_analysis.json"

# Create sample log file if it does not exist
if not os.path.exists(log_file):
    sample_logs = [
        "10:00 INFO Application started",
        "10:05 WARNING Low memory",
        "10:10 ERROR Database connection failed",
        "10:15 INFO User logged in",
        "10:20 ERROR File not found",
        "10:25 WARNING Disk space low",
        "10:30 INFO Application running"
    ]

    with open(log_file, "w") as file:
        for log in sample_logs:
            file.write(log + "\n")

# Initialize counters
info_count = 0
warning_count = 0
error_count = 0
total_logs = 0

# Read and analyze log file
with open(log_file, "r") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        total_logs += 1

        if "INFO" in line.upper():
            info_count += 1

        elif "WARNING" in line.upper():
            warning_count += 1

        elif "ERROR" in line.upper():
            error_count += 1

# Store results in dictionary
analysis = {
    "Total Logs": total_logs,
    "INFO Messages": info_count,
    "WARNING Messages": warning_count,
    "ERROR Messages": error_count
}

# Save results into JSON file
with open(json_file, "w") as file:
    json.dump(analysis, file, indent=4)

# Display results
print("\n===================================")
print("       LOG FILE ANALYZER")
print("===================================")

print("Total Log Messages:", total_logs)
print("INFO Messages:", info_count)
print("WARNING Messages:", warning_count)
print("ERROR Messages:", error_count)

print("===================================")
print("Analysis saved successfully!")
print("JSON File:", json_file)
print("===================================")

# Read and display JSON report
with open(json_file, "r") as file:
    result = json.load(file)

print("\n===== JSON ANALYSIS REPORT =====")

for key, value in result.items():
    print(key, ":", value)

