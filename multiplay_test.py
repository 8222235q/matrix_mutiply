import numpy as np

from multi import *

def add_matrices(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def subtract_matrices(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def strassen_multiply(a, b):
    if len(a) == 1:
        return [[a[0][0] * b[0][0]]]

    a11, a12, a21, a22 = split_matrix(a)
    b11, b12, b21, b22 = split_matrix(b)

    m1 = strassen_multiply(add_matrices(a11, a22), add_matrices(b11, b22))
    m2 = strassen_multiply(add_matrices(a21, a22), b11)
    m3 = strassen_multiply(a11, subtract_matrices(b12, b22))
    m4 = strassen_multiply(a22, subtract_matrices(b21, b11))
    m5 = strassen_multiply(add_matrices(a11, a12), b22)
    m6 = strassen_multiply(subtract_matrices(a21, a11), add_matrices(b11, b12))
    m7 = strassen_multiply(subtract_matrices(a12, a22), add_matrices(b21, b22))

    c11 = add_matrices(subtract_matrices(add_matrices(m1, m4), m5), m7)
    c12 = add_matrices(m3, m5)
    c21 = add_matrices(m2, m4)
    c22 = add_matrices(subtract_matrices(add_matrices(m1, m3), m2), m6)

    new_matrix = []
    for i in range(len(c11)):
        new_matrix.append(c11[i] + c12[i])
    for i in range(len(c21)):
        new_matrix.append(c21[i] + c22[i])

    return new_matrix


# 示例
size = 100
a = generate_random_matrix(size)
b = generate_random_matrix(size)

# print(np.dot(a, b))

start_time = time.time()  # 获取开始时间
result = strassen_multiply(a, b)
end_time = time.time()  # 获取结束时间
elapsed_time = end_time - start_time  # 计算经过的时间
print(f"Elapsed time: {elapsed_time} seconds")
for row in result:
    print(row)
