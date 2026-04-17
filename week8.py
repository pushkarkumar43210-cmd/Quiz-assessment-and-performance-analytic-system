# WEEK 8: CSV + Pandas
import csv
import os
import pandas as pd

os.makedirs("data", exist_ok=True)

# Write CSV
students = [
    {"sid": "S001", "name": "John", "dept": "CSE"},
    {"sid": "S002", "name": "Jane", "dept": "ECE"}
]
df = pd.DataFrame(students)
df.to_csv("data/students.csv", index=False)

# Read CSV
loaded = pd.read_csv("data/students.csv")
print("Loaded students:")
print(loaded)

# Error handling
try:
    pd.read_csv("data/missing.csv")
except FileNotFoundError:
    print("✅ File error handled!")
