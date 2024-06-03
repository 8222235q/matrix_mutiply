import multiprocessing
# import time
from multi import *
import numpy as np


def compute_block(queue, A_block, B_block, operation, index):
    """计算矩阵块的乘法和加法"""
    if operation == 'multiply':
        result = matrix_multiply(A_block, B_block)
    elif operation == 'add':
        result = matrix_addition(A_block, B_block)
    queue.put((index, result))


if __name__ == '__main__':



    size = 10000
    A = generate_random_matrix(size)
    B = generate_random_matrix(size)

    # print(np.dot(A, B))

    # 分割矩阵
    top_left_A, top_right_A, bottom_left_A, bottom_right_A = split_matrix(A)
    top_left_B, top_right_B, bottom_left_B, bottom_right_B = split_matrix(B)

    start_time = time.time()  # 获取开始时间
    # 创建队列
    queue = multiprocessing.Queue()

    # 创建进程进行矩阵块的计算
    processes = []

    # 启动8个进程同时计算矩阵块的乘法
    tasks = [
        (top_left_A, top_left_B, 'multiply', 'C_tl_1'),
        (top_right_A, bottom_left_B, 'multiply', 'C_tl_2'),
        (top_left_A, top_right_B, 'multiply', 'C_tr_1'),
        (top_right_A, bottom_right_B, 'multiply', 'C_tr_2'),
        (bottom_left_A, top_left_B, 'multiply', 'C_bl_1'),
        (bottom_right_A, bottom_left_B, 'multiply', 'C_bl_2'),
        (bottom_left_A, top_right_B, 'multiply', 'C_br_1'),
        (bottom_right_A, bottom_right_B, 'multiply', 'C_br_2')
    ]

    for A_block, B_block, operation, index in tasks:
        p = multiprocessing.Process(target=compute_block, args=(queue, A_block, B_block, operation, index))
        processes.append(p)
        p.start()

    # 获取所有计算结果
    results = {}
    for _ in tasks:
        index, result = queue.get()
        results[index] = result

    # 等待所有进程完成
    for p in processes:
        p.join()

    # 计算最终结果矩阵块
    C_tl = matrix_addition(results['C_tl_1'], results['C_tl_2'])
    C_tr = matrix_addition(results['C_tr_1'], results['C_tr_2'])
    C_bl = matrix_addition(results['C_bl_1'], results['C_bl_2'])
    C_br = matrix_addition(results['C_br_1'], results['C_br_2'])

    # 打印结果
    # print("C_tl:", C_tl)
    # print("C_tr:", C_tr)
    # print("C_bl:", C_bl)
    # print("C_br:", C_br)

    end_time = time.time()  # 获取结束时间
    elapsed_time = end_time - start_time  # 计算经过的时间
    print(f"Elapsed time: {elapsed_time} seconds")
