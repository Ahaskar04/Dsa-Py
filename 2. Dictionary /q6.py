# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

def check_same_frequency(list1, list2):
    """
    Returns True if both lists have the same frequency of elements, otherwise False.
    """
    # Get the set of all unique elements in both lists
    unique_elements = set(list1) | set(list2)
    
    # Compare counts for each element
    for element in unique_elements:
        if list1.count(element) != list2.count(element):
            return False
    return True

# Example usage:
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))  # Output: True
