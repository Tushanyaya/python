import numpy as np
import matplotlib.pyplot as plt
import math
import random


# Rastrigr 函数
def object_function(x):
    f = 0
    for i in range(0, len(x)):
        f = f + (x[i] ** 2 - (10 * math.cos(2 * np.pi * x[i])) + 10)
    return f


# 参数
def initpara():
    NP = 100  # 种群数量
    F = 0.6  # 缩放因子
    CR = 0.7  # 交叉概率
    generation = 2000  # 遗传代数
    len_x = 10
    value_up_range = 5.12
    value_down_range = -5.12
    return NP, F, CR, generation, len_x, value_up_range, value_down_range


# 种群初始化
def initialtion(NP):
    np_list = []  # 种群，染色体
    for i in range(0, NP):
        x_list = []  # 个体，基因
        for j in range(0, len_x):
            x_list.append(value_down_range + random.random() * (value_up_range - value_down_range))
        np_list.append(x_list)
    return np_list


# 列表相减
def substract(a_list, b_list):
    a = len(a_list)
    new_list = []
    for i in range(0, a):
        new_list.append(a_list[i] - b_list[i])
    return new_list


# 列表相加
def add(a_list, b_list):
    a = len(a_list)
    new_list = []
    for i in range(0, a):
        new_list.append(a_list[i] + b_list[i])
    return new_list


# 列表的数乘
def multiply(a, b_list):
    b = len(b_list)
    new_list = []
    for i in range(0, b):
        new_list.append(a * b_list[i])
    return new_list


# 变异
def mutation(np_list):
    v_list = []
    for i in range(0, NP):
        r1 = random.randint(0, NP - 1)
        while r1 == i:
            r1 = random.randint(0, NP - 1)
        r2 = random.randint(0, NP - 1)
        while r2 == r1 | r2 == i:
            r2 = random.randint(0, NP - 1)
        r3 = random.randint(0, NP - 1)
        while r3 == r2 | r3 == r1 | r3 == i:
            r3 = random.randint(0, NP - 1)

        v_list.append(add(np_list[r1], multiply(F, substract(np_list[r2], np_list[r3]))))
    return v_list


# 交叉
def crossover(np_list, v_list):
    u_list = []
    for i in range(0, NP):
        vv_list = []
        for j in range(0, len_x):
            if (random.random() <= CR) | (j == random.randint(0, len_x - 1)):
                vv_list.append(v_list[i][j])
            else:
                vv_list.append(np_list[i][j])
        u_list.append(vv_list)
    return u_list


# 选择
def selection(u_list, np_list):
    for i in range(0, NP):
        if object_function(u_list[i]) <= object_function(np_list[i]):
            np_list[i] = u_list[i]
        else:
            np_list[i] = np_list[i]
    return np_list

if __name__=="__main__":
    # 主函数
    NP, F, CR, generation, len_x, value_up_range, value_down_range = initpara()
    np_list = initialtion(NP)
    min_x = []
    min_f = []
    for i in range(0, NP):
        xx = []
        xx.append(object_function(np_list[i]))
    min_f.append(min(xx))
    min_x.append(np_list[xx.index(min(xx))])
    for i in range(0, generation):
        v_list = mutation(np_list)
        u_list = crossover(np_list, v_list)
        np_list = selection(u_list, np_list)
        for i in range(0, NP):
            xx = []
            xx.append(object_function(np_list[i]))
        min_f.append(min(xx))
        min_x.append(np_list[xx.index(min(xx))])
    # 输出
    min_ff = min(min_f)
    min_xx = min_x[min_f.index(min_ff)]
    print('the minimum point is x ')
    print(min_xx)
    print('the minimum value is y ')
    print(min_ff)
    # 画图
    x_label = np.arange(0, generation + 1, 1)
    plt.plot(x_label, min_f, color='blue')
    plt.xlabel('iteration')
    plt.ylabel('fx')
    plt.savefig('./iteration-f.png')
    plt.show()
