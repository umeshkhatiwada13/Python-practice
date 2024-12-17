def rotate_matrix(A):
    A = A[::-1]
    for i in range(len(A)):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    return A


print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
