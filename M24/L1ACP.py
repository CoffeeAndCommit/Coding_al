import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50])

print("Original Array:", arr)

# Sum
print("Sum:", np.sum(arr))

# Mean
print("Mean:", np.mean(arr))

# Maximum
print("Maximum:", np.max(arr))

# Minimum
print("Minimum:", np.min(arr))

# Multiply by 2
print("Multiply by 2:", arr * 2)

# Add 5
print("Add 5:", arr + 5)

# Square each element
print("Squared Array:", arr ** 2)

# Index of maximum value
print("Index of Maximum:", np.argmax(arr))

# Sorted array
print("Sorted Array:", np.sort(arr))

# Reverse array
print("Reversed Array:", arr[::-1])