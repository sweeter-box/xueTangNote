Name_list = ['张小敬','姚汝能','檀棋']
print(Name_list)
#输出列表

print(Name_list[0])
#输出列表第0个元素，列表的索引是从0开始的哦


name = input('请输入新来同学的名字：')
#获取新同学的名字，将名字放在变量name里
Name_list.append(name)
#将变量中的值加入到列表Name_list里
print(Name_list)