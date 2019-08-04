from common.FileUtils import *
import csv
import numpy as np
import matplotlib.pyplot as plt

Semester1 = []
Semester2 = []
Semester3 = []
plt.rcParams['font.sans-serif'] = ['SimHei']
fig,ax = plt.subplots()
ax.set_title('10位同学三个学期排名的对比')
'''
with 关键字只是 
参考资料：https://blog.csdn.net/azhao_dn/article/details/7659276 https://blog.csdn.net/u012609509/article/details/72911564
1. 用于资源访问；
2. 无需异常处理，简化try finally代码；
3. 自动释放资源。
'''
'''
open() 函数
参考资料：https://www.runoob.com/python3/python3-func-open.html
1. 用于打开一个文件，并返回文件对象
'''
with open(findPath("data1403.csv")) as csvfile:
    ##读取文件
    f_csv = csv.reader(csvfile)

    for row in f_csv:
        Semester1.append(int(row[0]))
        Semester2.append(int(row[1]))
        Semester3.append(int(row[2]))
#生成x轴坐标 1-11
x = np.arange(1,11)
#y轴
plt.ylabel("排名")
plt.xlabel("学生序号")
l1 = plt.bar(x -0.3,Semester1,0.3,alpha = 0.8,color='b', label="一学期")
l2 = plt.bar(x,Semester2,0.3,alpha = 0.8,color = 'r', label="二学期")
l3 = plt.bar(x+0.3,Semester3,0.3,alpha = 0.8,color = 'y', label="三学期")

#设置题注
plt.legend()

plt.grid(True,linestyle = '--',alpha = 0.8)

for a,b in zip(x,Semester1):
    plt.text(a-0.3,b+0.2,'%d'%b,ha = 'center',va = 'bottom',fontsize = 10)

for a,b in zip(x,Semester2):
    plt.text(a+0.3,b+0.2,'%d'%b,ha = 'center',va = 'bottom',fontsize = 10)

for a,b in zip(x,Semester3):
    plt.text(a+0.3,b+0.2,'%d'%b,ha = 'center',va = 'bottom',fontsize = 10)

plt.show()

