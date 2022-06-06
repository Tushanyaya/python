import numpy as np
import pandas as pd
if __name__ == "__main__":
    def PD():
        while True :
             n = input("输入数字：")
             if n == "1":
                '''
                Series 类似一维的数组对象，会产生相关的标签
                '''
                t = pd.Series([1,2,3,4,5,6],index= list("abcdef"))#创建一维数组 index 表示你需要的索引

                print(t[['a','b','c']])
                print(t[t>4])
                print(t*2)
             elif n =="2":

                data = {'state': ['ww', 'ee', 'rr', 'tt', 'yy', 'uu'],
                     'year': [2000, 2001, 2002, 2003, 2004, 2005],
                     'pop': [1.5, 1.6, 1.7, 1.8, 1.9, 2.1]}
                fram = pd.DataFrame(data)
                print(fram)
                print(fram.head())
                fram = pd.DataFrame(data, columns=['year', 'state', 'pop'])
                print(fram)
                fram2 = pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five','six'])
                #找不到该值，结果中会产生缺值
                print(fram2)
                print(fram2.columns)
                print(fram2['state'])#获取DataFrame中某列的数据获取为一个Series
                print(fram2.year)#获取DataFrame中某列的数据获取为一个Series
                #Ps: frame2[column]使用于任何列的名，fram2.column只适用符合python的变量名
                print(fram2.loc['three'])#loc[] 行通过位置名称方式寻找
                fram2['debt'] = 16.5#列通过修改方式来添加值
                print(fram2)
                fram2["debt"] = np.arange(6.)
                print(fram2)
                val = pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
                fram2['debt'] = val#用Series精确赋值
                print(fram2)
                fram2['eastern'] = fram2.state =='ee'
                print(fram2)
                del fram2['eastern']
                print(fram2)
             elif n =='3':
                obj = pd.Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])
                print(obj)
                obj2 = obj.reindex(['a','b','c','d','e'])#reindex():索引重新排序
                print(obj2)
                obj3 = pd.Series(['blue','purple','yellow',],index=[])
                print(obj3)
                obj3.reindex(range(6),method='ffill')
                print(obj3)









    PD()



