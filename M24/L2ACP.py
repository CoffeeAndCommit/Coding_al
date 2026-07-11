# Student Marks Analyser Using Pandas

import pandas as pd
import numpy as np

# -----------------------------
# Step 1: Create a Labelled Series
# -----------------------------
students = pd.Series(
    ["Aman", "Riya", "Rahul", "Sneha", "Karan"],
    index=[101, 102, 103, 104, 105]
)

print("===== Student Series =====")
print(students)

# -----------------------------
# Step 2: Create a DataFrame
# -----------------------------
data = {
    "Roll No": [101, 102, 103, 104, 105],
    "Name": ["Aman", "Riya", "Rahul", "Sneha", "Karan"],
    "Math": [85, 92, 78, 89, 95],
    "Science": [90, 95, 80, np.nan, 94],
    "English": [88, 91, 76, 90, np.nan]
}

df = pd.DataFrame(data)

print("\n===== Original DataFrame =====")
print(df)

# -----------------------------
# Step 3: Save DataFrame as CSV
# -----------------------------
df.to_csv("student_marks.csv", index=False)
print("\nCSV file 'student_marks.csv' saved successfully!")

# -----------------------------
# Step 4: Read CSV File
# -----------------------------
df = pd.read_csv("student_marks.csv")

print("\n===== Data Read from CSV =====")
print(df)

# -----------------------------
# Step 5: View Data
# -----------------------------
print("\n===== First 3 Rows =====")
print(df.head(3))

print("\n===== Last 2 Rows =====")
print(df.tail(2))

print("\n===== Data Types =====")
print(df.dtypes)

print("\n===== Data Information =====")
df.info()

print("\n===== Statistical Summary =====")
print(df.describe())

# -----------------------------
# Step 6: Check Missing Values
# -----------------------------
print("\n===== Missing Values =====")
print(df.isnull().sum())

# -----------------------------
# Step 7: Fill Missing Values
# -----------------------------
df["Science"].fillna(df["Science"].mean(), inplace=True)
df["English"].fillna(df["English"].mean(), inplace=True)

print("\n===== Data After Filling Missing Values =====")
print(df)

# -----------------------------
# Step 8: Calculate Total and Average
# -----------------------------
df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

print("\n===== Data with Total and Average =====")
print(df)

# -----------------------------
# Step 9: Student with Highest Average
# -----------------------------
top_student = df.loc[df["Average"].idxmax()]

print("\n===== Top Student =====")
print(top_student)

# -----------------------------
# Step 10: Students Scoring More Than 90 in Math
# -----------------------------
print("\n===== Students Scoring More Than 90 in Math =====")
print(df[df["Math"] > 90])

# -----------------------------
# Step 11: Highest and Lowest Marks in Each Subject
# -----------------------------
print("\n===== Highest Marks =====")
print("Math:", df["Math"].max())
print("Science:", df["Science"].max())
print("English:", df["English"].max())

print("\n===== Lowest Marks =====")
print("Math:", df["Math"].min())
print("Science:", df["Science"].min())
print("English:", df["English"].min())

# -----------------------------
# Step 12: Sort by Average
# -----------------------------
sorted_df = df.sort_values(by="Average", ascending=False)

print("\n===== Students Sorted by Average =====")
print(sorted_df)

# -----------------------------
# Step 13: Assign Grades
# -----------------------------
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(grade)

print("\n===== Data with Grades =====")
print(df)

# -----------------------------
# Step 14: Save Updated Data
# -----------------------------
df.to_csv("student_marks_updated.csv", index=False)

print("\nUpdated CSV file 'student_marks_updated.csv' saved successfully!")

# -----------------------------
# Final DataFrame
# -----------------------------
print("\n===== Final Student Marks Report =====")
print(df)