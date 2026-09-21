# Matrices with mutation

def zero(m,n):
    result = []
    for i in range(m):
        row = [0] * n
        result.append(row)
    return result

def identity(n):
    result = zero(n,n)
    for i in range(n):
        result[i][i] = 1
    return result

# update A and add B to it (A = A + B)
def add(A, B):
    assert len(A) == len(A) # the number of rows must be the same
    for rowA,rowB in zip(A,B):
        assert len(rowA) == len(rowB)
        # the number of columns must be the same
        for i in range(len(rowA)):
            rowA[i] = rowA[i] + rowB[i]

A = [[2,3],
     [3,5],
     [4,2]]
add(A,[[]])
print(A)
