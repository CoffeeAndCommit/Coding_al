# ============================================================
# Seaborn Library in Python
# Activity: Space Mission Data Explorer
# ============================================================

import seaborn as sns
import matplotlib.pyplot as plt

# ---- PART 1: What is Seaborn — Import and Load Data ----

# Load Seaborn's built-in planets dataset.
df = sns.load_dataset('planets')
df = df.dropna()

print("First 5 rows:")
print(df.head())
print()

print(df.info())
print()

print(df.describe())
print()

print("Discovery Methods:", df['method'].unique())

# ---- PART 2: Histogram ----

sns.histplot(data=df, x='orbital_period', bins=20, color='steelblue')
plt.title('Distribution of Planet Orbital Periods')
plt.xlabel('Orbital Period (Days)')
plt.ylabel('Count')
plt.show()

# ---- PART 3: KDE Plot and Fitting Distribution ----

sns.kdeplot(data=df, x='distance', fill=True)
plt.title('Distance Pattern of Planet Discoveries (KDE)')
plt.xlabel('Distance (Parsecs)')
plt.show()

sns.histplot(data=df, x='distance', kde=True, color='coral')
plt.title('Planet Distance — Histogram with KDE Curve')
plt.xlabel('Distance (Parsecs)')
plt.ylabel('Count')
plt.show()

# ---- PART 4: Scatter Plot ----

sns.scatterplot(
    data=df,
    x='distance',
    y='orbital_period',
    hue='method'
)

plt.title('Distance vs Orbital Period by Discovery Method')
plt.xlabel('Distance (Parsecs)')
plt.ylabel('Orbital Period (Days)')
plt.show()

# ---- PART 5: Heatmap ----

corr = df.corr(numeric_only=True)

print("Correlation table:")
print(corr)
print()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap — Planet Discovery Data')
plt.show()
