多进程效率最优矩阵乘法算法（Python)
首先实现4x4:
每个函数需要给出具体函数的使用方法（即API部分）
1.def 两个4x4矩阵相乘 ( )
2.def分割4x4矩阵 ( )
3.测试两个函数协调是否运行正常

4.将两个4x4矩阵相乘的函数泛化到多个矩阵能正常相乘
5.测试能分割任意给定的矩阵
6.测试两个函数协调是否运行正常

1.编写多进程函数
2.测试





未来解决：对内存进行优化、算法优化、如果内置库的算法效率低则使用自己写的算法、减少临时变量：尽量减少临时变量的使用，以节省内存。



    # # 拆分矩阵
    #
    # top_left_A, top_right_A, bottom_left_A, bottom_right_A = split_matrix(A)
    # top_left_B, top_right_B, bottom_left_B, bottom_right_B = split_matrix(B)
    #
    # # 矩阵块相乘
    # # 计算各个部分的矩阵乘法结果并相加
    # C_tl = matrix_addition(matrix_multiply(top_left_A, top_left_B), matrix_multiply(top_right_A, bottom_left_B))
    # C_tr = matrix_addition(matrix_multiply(top_left_A, top_right_B), matrix_multiply(top_right_A, bottom_right_B))
    # C_bl = matrix_addition(matrix_multiply(bottom_left_A, top_left_B), matrix_multiply(bottom_right_A, bottom_left_B))
    # C_br = matrix_addition(matrix_multiply(bottom_left_A, top_right_B), matrix_multiply(bottom_right_A, bottom_right_B))
    # print(C_tl, C_tr, C_bl, C_br)
    # print(merge_matrices(C_tl, C_tr, C_bl, C_br))
    # 示例：生成一个3x3的随机整数矩阵
