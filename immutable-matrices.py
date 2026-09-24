# immutable matrices
# a matrix is represented as a tuple of tuples.
# The length of the outer tuple is the number of rows.
# The length of each row is the number of columns
# Assertion: each row has the same length.

def number_of_rows(A):
    return len(A)

def number_of_columns(A):
    return len(A[0])

def zero(m,n):
    return ( (0,)*n ,) *m

def identity(n):
    result = []
    for i in range(n):
         row = (0,)*i + (1,) + (0,)*(n-i-1)
         result.append(row)
    return tuple(result)

# add two matrices A and B and return the result.

def addition(A,B):
    # note that the two matrices must have the same size to be able to compute their sum.
    assert number_of_columns(A) == number_of_columns(B)
    assert number_of_rows(A) == number_of_rows(B)
    result = []
    for i in range(number_of_rows(A)):
        row = []
        for j in range(number_of_columns(A)):
            x = A[i][j] + B[i][j]
            row.append(x)
        result.append(tuple(row))
    return tuple(result)

A = ((2,3),
     (3,5),
     (4,2))

B = ((1,1),
     (1,1),
     (1,1))

def transpose(A):
    return tuple(zip(*A))

print(transpose(A))





# multiplication
