import numpy as np

# A = [[0, 0, 5, 2], [4, 2, 1, 0], [0, -1, 2, 1], [7, 2, 0, 5]]
# B = [[1, 2, 4, -1], [5, 3, 1, 0], [0, 0, 2, 0], [1, 7, 6, 3]]
size = 1000
A = np.random.rand(size, size)
B = np.random.rand(size, size)

# C = [[], [], [], []]


def matrix_multiply(a, b):
    # m = len(A)
    # n = len(A[0])
    # p = len(B[0])
    """
        计算两个二维数组（矩阵）的乘积
        """
    if len(a[0]) != len(b):
        raise ValueError("Number of columns in A must be equal to number of rows in B")  # 增加了异常捕获

    c = [[0] * len(a) for _ in range(len(b))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):  # 可对len函数进行优化
                c[i][j] += a[i][k] * b[k][j]  # 此处可进行进一步优化

    return c


def matrix_addition(matrix1, matrix2):
    # 确保两个矩阵的尺寸相同
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result


def split_matrix(matrix):
    rows = len(matrix)  # 矩阵的行数x-axis
    cols = len(matrix[0])  # 矩阵的列数y-axis
    mid_row = rows // 2  # 取整除 - 往小的方向取整数(确定中间轴)
    mid_col = cols // 2

    # 初始化四个子矩阵
    top_left = []
    top_right = []
    bottom_left = []
    bottom_right = []

    for i in range(rows):
        if i < mid_row:
            top_left.append(matrix[i][:mid_col])
            top_right.append(matrix[i][mid_col:])
        else:
            bottom_left.append(matrix[i][:mid_col])
            bottom_right.append(matrix[i][mid_col:])

    return top_left, top_right, bottom_left, bottom_right


def merge_matrices(*matrices):  # 合并矩阵, 可传入任意个矩阵
    merged_matrix = []
    for matrix in matrices:
        for row in matrix:
            merged_matrix.append(row)
    return merged_matrix


if __name__ == '__main__':
    # C = matrix_multiply(A, B)
    # for row in C:
    #     print(row)

    # 打印结果
    # print(A)
    # print(split_matrix(A))
    # print(B)
    # print(split_matrix(B))
    # print(matrix_multiply(A, B))
    # print(np.dot(A, B))

    # 拆分矩阵

    top_left_A, top_right_A, bottom_left_A, bottom_right_A = split_matrix(A)
    top_left_B, top_right_B, bottom_left_B, bottom_right_B = split_matrix(B)

    # 矩阵块相乘
    # 计算各个部分的矩阵乘法结果并相加
    C_tl = matrix_addition(matrix_multiply(top_left_A, top_left_B), matrix_multiply(top_right_A, bottom_left_B))
    C_tr = matrix_addition(matrix_multiply(top_left_A, top_right_B), matrix_multiply(top_right_A, bottom_right_B))
    C_bl = matrix_addition(matrix_multiply(bottom_left_A, top_left_B), matrix_multiply(bottom_right_A, bottom_left_B))
    C_br = matrix_addition(matrix_multiply(bottom_left_A, top_right_B), matrix_multiply(bottom_right_A, bottom_right_B))
    print(C_tl, C_tr, C_bl, C_br)
    # print(merge_matrices(C_tl, C_tr, C_bl, C_br))
