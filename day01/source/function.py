#原始成绩信息
Scores = {'张小敬':[85,86],'姚汝能':[90,85],'檀棋':[95,88],'李必':[100,99],'徐宾':[95,80]}

#定义函数add_scores()，实现计算总成绩的功能
def add_scores(name):
    sum = Scores[name][0] + Scores[name][1]
    return sum

#将输入的名字赋值给变量name
name = input('请输入5位同学中任意一位同学的名字：')
#调用函数add_scores()，将函数返回的值保存在变量sum中
sum = add_scores(name)
#输出结果
print('这位同学的总分是：'+str(sum))