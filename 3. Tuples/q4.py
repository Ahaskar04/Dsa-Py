# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.

def concatenate_strings(input_tuple):
    string = ""
    for i in input_tuple:
        string +=i
        string +=" "
    return string.strip()
    
input_tuple = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple)
print(output_string)


def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)