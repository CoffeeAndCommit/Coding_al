# Restaurant Customer Insights Explorer
# Using Python, Seaborn, and Matplotlib

import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------------
# Load the Built-in Tips Dataset
# -------------------------------------
tips = sns.load_dataset("tips")

# Display first five rows
print("First 5 Rows:")
print(tips.head())

# Dataset information
print("\nDataset Information:")
print(tips.info())

# Statistical summary
print("\nStatistical Summary:")
print(tips.describe())

# -------------------------------------
# 1. Scatter Plot
# Total Bill vs Tip
# -------------------------------------
plt.figure(figsize=(8,6))
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex",
    style="smoker",
    s=80
)

plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.grid(True)
plt.show()

# -------------------------------------
# 2. Line Plot
# Average Total Bill by Day
# -------------------------------------
plt.figure(figsize=(8,6))
sns.lineplot(
    data=tips,
    x="day",
    y="total_bill",
    estimator="mean",
    marker="o"
)

plt.title("Average Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Total Bill ($)")
plt.grid(True)
plt.show()

# -------------------------------------
# 3. Bar Plot
# Average Tip by Day
# -------------------------------------
plt.figure(figsize=(8,6))
sns.barplot(
    data=tips,
    x="day",
    y="tip"
)

plt.title("Average Tip by Day")
plt.xlabel("Day")
plt.ylabel("Average Tip ($)")
plt.show()

# -------------------------------------
# 4. Histogram
# Distribution of Total Bills
# -------------------------------------
plt.figure(figsize=(8,6))
sns.histplot(
    data=tips,
    x="total_bill",
    bins=20,
    kde=True
)

plt.title("Distribution of Total Bills")
plt.xlabel("Total Bill ($)")
plt.ylabel("Count")
plt.show()

# -------------------------------------
# 5. Box Plot
# Total Bill by Day
# -------------------------------------
plt.figure(figsize=(8,6))
sns.boxplot(
    data=tips,
    x="day",
    y="total_bill"
)

plt.title("Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.show()

# -------------------------------------
# 6. Violin Plot
# Tips by Gender
# -------------------------------------
plt.figure(figsize=(8,6))
sns.violinplot(
    data=tips,
    x="sex",
    y="tip"
)

plt.title("Tip Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Tip ($)")
plt.show()

# -------------------------------------
# 7. Count Plot
# Customers by Day
# -------------------------------------
plt.figure(figsize=(8,6))
sns.countplot(
    data=tips,
    x="day"
)

plt.title("Number of Customers by Day")
plt.xlabel("Day")
plt.ylabel("Count")
plt.show()

# -------------------------------------
# 8. Pair Plot
# Relationships Between Numerical Columns
# -------------------------------------
sns.pairplot(
    tips,
    hue="sex"
)

plt.show()

# -------------------------------------
# 9. Heatmap
# Correlation Matrix
# -------------------------------------
plt.figure(figsize=(8,6))

numeric_data = tips.select_dtypes(include=["number"])

sns.heatmap(
    numeric_data.corr(),
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Correlation Heatmap")
plt.show()

# -------------------------------------
# 10. Strip Plot
# Tips by Day
# -------------------------------------
plt.figure(figsize=(8,6))
sns.stripplot(
    data=tips,
    x="day",
    y="tip",
    jitter=True
)

plt.title("Tips by Day")
plt.xlabel("Day")
plt.ylabel("Tip ($)")
plt.show()

# -------------------------------------
# 11. Swarm Plot
# Total Bill by Party Size
# -------------------------------------
plt.figure(figsize=(8,6))
sns.swarmplot(
    data=tips,
    x="size",
    y="total_bill"
)

plt.title("Total Bill by Party Size")
plt.xlabel("Party Size")
plt.ylabel("Total Bill ($)")
plt.show()

# -------------------------------------
# 12. Summary Statistics
# -------------------------------------
print("\nAverage Tip by Gender:")
print(tips.groupby("sex")["tip"].mean())

print("\nAverage Total Bill by Day:")
print(tips.groupby("day")["total_bill"].mean())

print("\nAverage Tip by Party Size:")
print(tips.groupby("size")["tip"].mean())

print("\nRestaurant Customer Insights Explorer Completed Successfully!")