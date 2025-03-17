def reverse_dict(my_dict):
    reverse_dictionary = {}
    for key in my_dict:
        reverse_dictionary[my_dict[key]] = key
    return reverse_dictionary
    
        
my_dict = {'name': 'Jack', 'age': 26, 'address': 'Downtown', 'education': 'Engineering'}
print(reverse_dict(my_dict)) # Output