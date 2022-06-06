import os #1、利用import语句进行导入模块，用逗号分隔可以导入多个包
import math,copy,random,time
from collections import Counter  #2、利用from...import ....进行导入
import numpy as np  #3、利用as关键字重命名包名，以后再使用就可以直接用np## 了
def study_numpy(length:int )->bool:#52、解释参数类型的函数创建，->为返回值类型
    tuple1 = (1,2,3,4,1,5,1)
    tuple2 = tuple(range(10,10+length))
    print("tuple1的形状为:",tuple1.reshape())

    print(tuple1.count(1))#输出该值出现了几次
    print(tuple1.index(1))#查找该值的索引值例如：1的索引在tuple1[0]的位置
    try:
        tuple1[0] = 9
    except TypeError:
        print("插入失败")
    finally:
        print("你管对错爷就这态度")
    try:

        print("id_tuple1 =  ",id(tuple1),"id_tuple2 = ",id(tuple2))

    except:

        return False

    else:
        tuple3 = tuple2 +tuple1
        print("id_tuple3=",id(tuple3))
        return True
def study_fuction():
    tuple1 = (5,6,4,8,9,7,2,3)
    list1 = [1,2,3,4,5,6,7,8,9]
    print(max(tuple1),min(tuple1),sum(tuple1),len(tuple1))#sum()函数，得到序列和 len()函数，得到序列长度
    print(divmod(tuple1[0],tuple1[5]))#divmod()函数，计算两个数的商和余数，结果两个格式为(商，余数)
    print(list(enumerate(tuple1)))#87、enumerate()，给元组添加一个索引
    tuple2 = tuple(list1)#将列表转换为元组
    print("tuple2 = ",tuple2)
    list2 =  list(reversed(list1))
    print("list2=", list2)
    Textstring = "The mountains and rivers are different, the wind and the moon are the same"
    words = Textstring.split(" ")#split()函数以里面的参数分割字符，返回一个列表，记得是列表列表！！！
    print("words = ",words)
    words.sort(key=len)#sort()函数进行排序，以key=len 意思是以字符串长度排序
    print("以长度排序:", words)
    words.sort(key=len, reverse=(True))#reverse = reversed（）用法一样
    print("以长度排序且反转:", words)
    words.sort(key= str)#以字典排序?????
    print("以字典排序:", words)
    ct = Counter(Textstring)#Counter（）能得到字符串中每个数字的出现次数
    print("ct =",ct)
    ct.update("eeeeexxxxxlllllllllllllxxx")#将里面内容更新
    print("ct =",ct)
    print("字符最多的前五位是:",ct.most_common(5))
def study_Slice():  #python的切片操作，得到序列的部分内容
	str1 = 'I hope one day, I can find you, my sweet dream'
	list1 = list(range(10))
	tuple1 = tuple(list1)

	print(str1[:])  #102、切片格式为str[start:end:step]，前闭后开,step可为正负，默认步长为1
	print(str1[::-1])  #103、当步长为负数的时候，反转
	print(str1[:15])  #104、只有end时，截取最开始到end
	print(str1[15:])  #105、只有start时，截取从start到末尾的所有字符
	print(str1[::2])  #106、步长为2
	print(str1[1::2])

	print(list1[:])  #107、和str一样
	print(list1[2:])
	print(list1[:2])
	print(list1[::-1])

	list1[1:5] = [10] #切片赋值，右边必须为一个可以遍历的序列
	#list1[1:5] = 10   这样就会报错
	print(list1)
def study_Slice():  #python的切片操作，得到序列的部分内容
	str1 = 'I hope one day, I can find you, my love'
	list1 = list(range(10))
	tuple1 = tuple(list1)

	print(str1[:])  #102、切片格式为str[start:end:step]，前闭后开,step可为正负，默认步长为1
	print(str1[::-1])  #103、当步长为负数的时候，反转
	print(str1[:15])  #104、只有end时，截取最开始到end Ps:" "空格也算
	print(str1[15:])  #105、只有start时，截取从start到末尾的所有字符
	print(str1[::2])  #106、步长为2
	print(str1[1::2])

	print(list1[:])  #107、和str一样
	print(list1[2:])
	print(list1[:2])
	print(list1[::-1])

	list1[1:5] = [10] #切片赋值，右边必须为一个可以遍历的序列
	#list1[1:5] = 10   这样就会报错
	print(list1)
def study_files():
    panth = input("panth:")
    print(panth)
    foldaer = os.path.exists(panth)
    if not foldaer:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(panth)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print
        "---  new folder...  ---"
        print
        "---  OK  ---"

    else:
        print
        "---  There is this folder! ---"
    filepath = input('请输入你的文件路径（输入quit退出）:')
    if filepath == 'quit':
        return True
    try:
        file = open(filepath, 'w')  # 121、打开文件，'w'为写格式打开 没有就创建一个
        file.write('哈哈，现在开始写文件')  # 122、向文件写入字符串
        file.close()  # 123、关闭文件
        file = open(filepath, 'r')  # 122、以'r'读格式打开
        print('从文件中读出的内容：\n', file.read())  # 123、read()函数可以得到文件内容


    except FileNotFoundError:
        print('文件未找见请重新输入')
        study_files()  # 124、这就是上面所说的递归调用
    except:
        print('出现错误,请重新输入路径')
        study_files()
    #os.remove(filepath)  # 删除文件
    #os.rmdir(panth)  # 删除文件夹
    #shutil.rmtree()删除目录及其所有内容。
class User():
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.yanzhi = 100000000000000000000000000000000000000000000000000000
    def dispaly(self):
        print("大家好，我是{},身高{}，体重{}，颜值超高{}".format(self.name,self.height,self.weight,self.yanzhi))

if __name__ =="__main__":
    choosefuction = '''
    0:退出 1：study_numpy(10)
    2:study_fuction() 3:study_Slice()
    4:study_files() 5: User'''
    while True:
        input("按键继续")
        print(choosefuction)
        num = input("num=")
        if num == "0":
            break
        elif num == "1":
            study_numpy(10)
        elif num == "2":
            study_fuction()
        elif num == "3":
            study_Slice()
        elif num == "4":
            study_files()
        elif num == "5":
            name = input("name:")
            height = input("height:")
            weight = input("weight:")
            user = User(name,height,weight)
            user.dispaly()