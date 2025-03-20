# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.

def get_diagonal(tup):
    new_tup=()
    for i in range(len(tup)):
        for j in range(len(tup)):
            if i==j:
                new_tup += (tup[i][j],)
    return new_tup
    
input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)
                

def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))