#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise). 
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

def rotate(matrix):
    n = len(matrix)
 
    # Transpose the matrix
    for i in range(n):  # Iterate over the rows
        for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
            # Swap the elements at positions (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print(matrix)
 
    # Reverse each row
    for row in matrix:  # Iterate over each row in the matrix
        row.reverse()  # Reverse the elements in the current row
    print(matrix)

rotate([[1,2,3],[4,5,6],[7,8,9]]) 