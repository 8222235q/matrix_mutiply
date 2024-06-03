import numpy as np

# A = [[0, 0, 5, 2], [4, 2, 1, 0], [0, -1, 2, 1], [7, 2, 0, 5]]
# B = [[1, 2, 4, -1], [5, 3, 1, 0], [0, 0, 2, 0], [1, 7, 6, 3]]
A = np.random.randint(0, 10, size=(5, 4))
B = np.random.randint(0, 10, size=(4, 4))

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


if __name__ == '__main__':
    # C = matrix_multiply(A, B)
    # for row in C:
    #     print(row)


    # 拆分矩阵

    top_left, top_right, bottom_left, bottom_right = split_matrix(A)

    # 打印结果
    print(A)
    print("Top Left:\n", top_left)
    print("Top Right:\n", top_right)
    print("Bottom Left:\n", bottom_left)
    print("Bottom Right:\n", bottom_right)
    # print(matrix_multiply(A, B))