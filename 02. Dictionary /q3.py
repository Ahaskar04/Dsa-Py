# Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition.
def merge_and_sum(dict1, dict2):
    # Start with a copy of the first dictionary
    merged = dict1.copy()
    
    # Loop through the second dictionary
    for key, value in dict2.items():
        if key in merged:
            # If the key exists in both, sum their values
            merged[key] += value
        else:
            # Otherwise, simply add the new key-value pair
            merged[key] = value
    return merged

# Example usage:
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 3, 'c': 4, 'd': 5}
result = merge_and_sum(d1, d2)
print(result)  # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}
