# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.


def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))

tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)   
print(tuple_elementwise_sum(tuple1, tuple2)) # (6, 8, 10, 12)