from matplotlib import pyplot as plt
import  random
import numpy as np
def study_matplotlib_1 ():
    '''
    figure：设置图片大小，指的是我们所画的图
            - figsize 图片大小
            - dpi 调节图片清晰度
    '''
    fig = plt.figure(figsize=(20,6),dpi=80)
    x = range(2, 26, 2)
    y = [15, 13, 12, 25, 26, 30, 78, 15, 1, 0, 5, 4]
    plt.plot(x,y)#绘制图像
    '''
        绘制x轴的刻度 xticks
        绘制y轴的刻度 yticks
    '''
    plt.xticks(x)
    plt.savefig("./matplotlib.png")
    plt.show()#显示图像
def study_matplotlib_2():
    from matplotlib import pyplot as plt
    from matplotlib.font_manager import FontProperties
    import random
    if __name__ == "__main__":
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        x = range(0, 120)
        y = [random.randint(20, 35) for i in range(120)]
        font = FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc', size=16)
        plt.figure(figsize=(20, 8), dpi=80)
        plt.plot(x, y)
        '''
        调整x轴的刻度
        '''
        _xtick_labels = ["10点{}分".format(i) for i in range(60)]
        _xtick_labels += ["11点{}分".format(i) for i in range(60)]
        # 取步长 数字和字符串一一对应，数据长度一样
        plt.xticks(list(x)[::2], _xtick_labels[::2], rotation=45)  # rotaion 旋转度数
        '''
        添加描述信息
        '''
        plt.xlabel("时间")
        plt.ylabel("温度")
        plt.title("10点到12点的每分钟的气温变化情况")
        plt.show()
def study_matplotlib_3():
    '''显示中文'''
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    #fig = plt.figure(figsize=(20, 6), dpi=80)
    x = range(18, 31)
    y_1 = [2, 2, 2, 3, 5, 6, 8, 10, 1, 0, 5, 4, 6]
    y_2 = [6.,8,9,7,3,2,2,2,1,1,1,1,1]
    plt.plot(x, y_1,label ='自己')
    plt.plot(x,y_2,label ='别人',color = 'r',linestyle='--')
    _xticks_labels = ["{}岁".format(i) for i in x]
    plt.xticks(x, _xticks_labels)
    plt.yticks(range(0, 11))
    '''
    # 设置网格
    #grid(b, which, axis, color, linestyle, linewidth， **kwargs)
    b : 布尔值。就是是否显示网格线的意思
    which : 取值为'major', 'minor'， 'both'。
    axis : 取值为‘both’， ‘x’，‘y’。就是以什么轴为刻度生成网格。
    linestyle :也可以用ls来代替linestyle， 设置网格线的风格，
    linewidth : 设置网格线的宽度
    '''
    plt.grid(alpha = 0.1)
    #添加图例
    plt.legend(loc = 'upper left')
    plt.show()
def study_maplot_4():
    '''显示中文'''
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    a = ["张三","李四","王二","小明","小红","赵四","韩梅梅"]
    b_1 = [23,34,45,67,89,99,78]
    b_2 = [33,44,55,66,22,33,88]
    b_3 = [67,56,43,31,34,87,99]
    bar_width = 0.3
    y_1 = list(range(len(a)))
    y_2 = [i+bar_width for i in y_1]
    y_3 = [i+bar_width*2 for i in y_1]
    plt.barh(range(len(a)),b_1,height=bar_width,label = "一")
    plt.barh(y_2, b_2, height=bar_width,label="二")
    plt.barh(y_3, b_2, height=bar_width,label="三")
    plt.yticks(y_2, a)
    plt.show()
def study_maplot_5():
    a = [123,124,124,156,121,120,121,345,567,156,180,191,243,345,121,123,124,110,120,121,123,124,156]
    a_1 = max(a) - min(a)
    for i in range(2, a_1):
        if a_1 % i == 0:
            print(i, end=" ")
            b = int(input())
        else:
            i = 5;
            b = i
    num_bins = a_1 // b
    plt.figure(figsize=(50,9),dpi= 80)
    plt.hist(a,num_bins)
    plt.xticks(range(min(a),max(a)+b,b))
    plt.grid()
    plt.show()
def study_matplot_6():
    '''显示中文'''
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    y_3 = [11,23,14.17,21,3,5,3,7,23,24,12,13,15,15,10,11,12,14,15,18,19,10,2,3,6,8,6,7,2,13,7]
    y_10 = [12,15,16,14,12,15,14,16,11,13,14,16,15,12,14,13,10,11,14,11,15,16,14,16,15,14,12,10,11,12]
    print(len(y_10),len(y_3))
    x_3 = range(1,32)
    x_10 = range(51,81)
    print(len(x_3),len(x_10))
    plt.scatter(x_3,y_3)
    plt.scatter(x_10,y_10)
    _x = list(x_3)+list(x_10)
    _xticks_label = ["3月{}日".format(i) for i in x_3]
    _xticks_label += ["10月{}日".format(i-50) for i in x_10]
    plt.xticks(_x[::3],_xticks_label[::3],rotation = 125)
    plt.show()
if __name__ == "__main__":
    while True:
        num = input("nume:")
        if num == '1':
            study_matplotlib_1()
        elif num =='2':
            study_matplotlib_2()
        elif num == '3':
            study_matplotlib_3()
        elif num =="4":
            study_maplot_4()
        elif num == '5':
            study_maplot_5()
        elif num == "6":
            study_matplot_6()
''''

                 
                 data = {'state': ['ww', 'ee', 'rr', 'tt', 'yy', 'uu'],
                        'year': [2000, 2001, 2002, 2003, 2004, 2005],
                        'pop': [1.5, 1.6, 1.7, 1.8, 1.9, 2.1]}
                 fram = pd.DataFrame(data)
                 print(fram)
             
                 print(fram.head())
                 fram = pd.DataFrame(data, columns=['year', 'state', 'pop'])
                 print(fram)
                 print()
'''