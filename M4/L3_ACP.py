# Assignment: Check the frequency
# Check the frequency of a value in the given test dictionary.

def check_frequency(test_dict, value):
    # Count the frequency of the specified value among the dictionary's values
    count = 0
    for val in test_dict.values():
        if val == value:
            count += 1
    return count

# Given test dictionary
test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print("Original dictionary:", test_dict)

# Value to search for
K = 2
freq = check_frequency(test_dict, K)

print(f"Frequency of value {K} in the dictionary is: {freq}")
