# My Savings Progress Chart Using Matplotlib

import matplotlib.pyplot as plt

# -----------------------------
# Weekly Savings Data
# -----------------------------
weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]
savings = [500, 800, 1200, 1500, 2000]

# -----------------------------
# Line Graph
# -----------------------------
plt.figure(figsize=(8, 5))

plt.plot(
    weeks,
    savings,
    marker='o',
    linestyle='-',
    linewidth=3,
    color='blue',
    markersize=8,
    label='Savings'
)

plt.title("My Weekly Savings Progress", fontsize=16)
plt.xlabel("Weeks", fontsize=12)
plt.ylabel("Savings (₹)", fontsize=12)
plt.grid(True)
plt.legend()

plt.show()

# -----------------------------
# Bar Chart
# -----------------------------
plt.figure(figsize=(8, 5))

plt.bar(
    weeks,
    savings,
    color='green',
    width=0.5
)

plt.title("My Weekly Savings (Bar Chart)", fontsize=16)
plt.xlabel("Weeks", fontsize=12)
plt.ylabel("Savings (₹)", fontsize=12)

plt.show()\