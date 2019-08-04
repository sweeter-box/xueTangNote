import csv
#使用import语句调用Python内置csv模块
Scores = {'张小敬':[85,86],'姚汝能':[90,85],'檀棋':[95,88],'李必':[100,99],'徐宾':[95,80]}
#原始成绩
titles = ['姓名','语文成绩','数学成绩']
#csv文件的首行

with open('scores.csv','w',newline='') as myScores:
    #以w，即写入的方式打开scores01.csv文件，如果该文件不存在，则创建一个名为scores01的空csv文件；newline = ''是解决文件里有空行的问题
    myWriter = csv.writer(myScores)
    #生成一个名为myWriter的writer对象
    myWriter.writerow(titles)
    #调用myWriter对象的writerow()方法
    for key in Scores.items():
        #遍历Scores字典的元素，第0个key对应的值是{'李必':[85,86]}
        line = [key[0],Scores[key[0]][0],Scores[key[0]][1]]
        #因为writerow()方法是将列表一行一行写入到文件，需要我们将每一行的“姓名”“语文成绩”“数学成绩”放在一个列表里
        myWriter.writerow(line)
        #一行一行地写入数据
