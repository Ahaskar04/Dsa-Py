# Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.


def insert_value_front(input_tuple, value_to_insert):
    list_data = list(input_tuple)
    list_data.insert(0, value_to_insert)
    return tuple(list_data)
    
print(insert_value_front((1,2,3), 15))


def insert_value_at_beginning(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple