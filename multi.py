import random
import time
import numpy as np


# A = [[0, 0, 5, 2], [4, 2, 1, 0], [0, -1, 2, 1], [7, 2, 0, 5]]
# B = [[1, 2, 4, -1], [5, 3, 1, 0], [0, 0, 2, 0], [1, 7, 6, 3]]
# size = 10

# C = [[], [], [], []]

def generate_random_matrix(size):  # 矩阵生成器
    matrix = []
    for _ in range(size):
        row = [random.randint(0, 9) for _ in range(size)]
        matrix.append(row)
    return matrix


def matrix_multiply(a, b):
    """
    计算两个二维数组（矩阵）的乘积
    """
    m = len(a)  # 减少重复计算：将 len(a), len(a[0]), 和 len(b[0]) 的值提前存储在变量中，避免在循环中重复调用 len 函数。
    n = len(a[0])
    p = len(b[0])

    if n != len(b):
        raise ValueError("Number of columns in A must be equal to number of rows in B")

    # 初始化结果矩阵为零矩阵
    c = [[0] * p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            sum = 0  # 优化
            for k in range(n):
                sum += a[i][k] * b[k][j]
            c[i][j] = sum

    return c


def matrix_addition(matrix1, matrix2):
    # 确保两个矩阵的尺寸相同
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")

    # 获取矩阵的行数和列数
    rows = len(matrix1)
    cols = len(matrix1[0])

    # 预分配结果矩阵的空间
    result = [[0] * cols for _ in range(rows)]

    # 使用列表推导式进行矩阵加法
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

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
    start_time = time.time()  # 获取开始时间

    size = 1000
    A = generate_random_matrix(size)
    B = generate_random_matrix(size)
    # print(A, B)
    top_left_A, top_right_A, bottom_left_A, bottom_right_A = split_matrix(A)
    top_left_B, top_right_B, bottom_left_B, bottom_right_B = split_matrix(B)

    # matrix_multiply(top_left_A, top_left_B)
    # C_tl = matrix_addition(matrix_multiply(top_left_A, top_left_B), matrix_multiply(top_right_A, bottom_left_B))
    # C_tr = matrix_addition(matrix_multiply(top_left_A, top_right_B), matrix_multiply(top_right_A, bottom_right_B))
    # C_bl = matrix_addition(matrix_multiply(bottom_left_A, top_left_B), matrix_multiply(bottom_right_A, bottom_left_B))
    # C_br = matrix_addition(matrix_multiply(bottom_left_A, top_right_B), matrix_multiply(bottom_right_A, bottom_right_B))

    # print(np.dot(A, B))
    # print(C_tl, C_tr, C_bl, C_br)
    # matrix_multiply(A, B)
    # print(C_tl)
    end_time = time.time()  # 获取结束时间
    elapsed_time = end_time - start_time  # 计算经过的时间
    print(f"Elapsed time: {elapsed_time} seconds")