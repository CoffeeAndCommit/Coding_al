# Assignment: Set Symmetric Difference
# Write a Python program to find the symmetric difference between two sets.

# Define two sample sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# Finding symmetric difference using the symmetric_difference() method
sym_diff_method = set1.symmetric_difference(set2)
print("\nSymmetric difference using symmetric_difference() method:")
print(sym_diff_method)

# Finding symmetric difference using the ^ operator
sym_diff_operator = set1 ^ set2
print("\nSymmetric difference using ^ operator:")
print(sym_diff_operator)
