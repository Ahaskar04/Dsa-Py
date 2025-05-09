# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

def common_elements(tuple1, tuple2):
    new_tuple = ()
    for i in tuple1:
        for j in tuple2:
            if i == j:
                new_tuple += (i,)
                
    return new_tuple

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)


def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))