A = [[0, 0, 5, 2], [4, 2, 1, 0], [0, -1, 2, 1], [7, 2, 0, 5]]
B = [[1, 2, 4, -1], [5, 3, 1, 0], [0, 0, 2, 0], [1, 7, 6, 3]]


# C = [[], [], [], []]


def matrix_multiply(a, b):
    # m = len(A)
    # n = len(A[0])
    # p = len(B[0])

    c = [[0] * len(a) for i in range(len(b))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]

    return c

def split_matrix(A):

    assert len(A) == 4 and all(len(row) == 4 for row in A)

    # 创建子矩阵
    A1 = [row[:2] for row in A[:2]]
    A2 = [row[2:] for row in A[:2]]
    A3 = [row[:2] for row in A[2:]]
    A4 = [row[2:] for row in A[2:]]

    return A1, A2, A3, A4


# 分割矩阵
sub_matrices = split_matrix(A)

# 打印子矩阵
for i, sub_matrix in enumerate(sub_matrices, 1):
    print(f"子矩阵 A{i}:")
    for row in submatrix:
        print(row)
    print()  # 为了更好的可视分隔


C = matrix_multiply(a, B)
for row in C:
    print(row)
