# Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.
def reverse_dict(my_dict):
    reverse_dictionary = {}
    for key in my_dict:
        reverse_dictionary[my_dict[key]] = key
    return reverse_dictionary
    
        
my_dict = {'name': 'Jack', 'age': 26, 'address': 'Downtown', 'education': 'Engineering'}
print(reverse_dict(my_dict)) # Output