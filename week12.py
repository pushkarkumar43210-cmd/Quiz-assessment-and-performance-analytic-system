# =========================================
# WEEK 12: NumPy + Pandas + Matplotlib
# =========================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------- Sample Data --------
data = {
    "Student": ["Pushkar", "Aman", "Riya", "Neha", "Rahul"],
    "Marks": [85, 40, 72, 30, 90],
    "Previous_Marks": [70, 35, 65, 25, 80]
}

# -------- Pandas DataFrame --------
df = pd.DataFrame(data)

print("\n--- Student Data ---")
print(df)


# =========================================
# 🔥 NumPy Analytics
# =========================================

marks_array = np.array(df["Marks"])

avg_marks = np.mean(marks_array)
max_marks = np.max(marks_array)
min_marks = np.min(marks_array)

print("\n--- NumPy Analytics ---")
print("Average Marks:", avg_marks)
print("Highest Marks:", max_marks)
print("Lowest Marks:", min_marks)

# Improvement %
df["Improvement %"] = ((df["Marks"] - df["Previous_Marks"]) / df["Previous_Marks"]) * 100


# =========================================
# 🔥 Pandas Analysis
# =========================================

print("\n--- Student-wise Comparison ---")
print(df[["Student", "Marks", "Improvement %"]])

# Pass/Fail
df["Status"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

print("\n--- Status ---")
print(df[["Student", "Marks", "Status"]])

# Groupby example
status_count = df.groupby("Status").size()
print("\nPass/Fail Count:\n", status_count)


# =========================================
# 🔥 Matplotlib Charts
# =========================================

# Line Graph (Trend)
plt.figure()
plt.plot(df["Student"], df["Marks"], marker='o')
plt.title("Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid()
plt.show()


# Pie Chart (Pass/Fail)
plt.figure()
plt.pie(status_count, labels=status_count.index, autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.show()
