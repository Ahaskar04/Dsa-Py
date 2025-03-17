def filter_dict(d, condition):
    new_dict = {}
    for k, v in d.items():
        if condition(k, v):
            new_dict[k] = v
    return new_dict

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
print(filtered_dict)  # Output: {'b': 2, 'd': 4}