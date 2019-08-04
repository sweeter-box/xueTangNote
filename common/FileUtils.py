import os
import platform

## file 文件名
def findPath(file):
    ##获取项目文件当前路径
    o_path = os.getcwd()
   ## print("当前路径"+o_path)
    separator = getSeparator()
    str = o_path
    str = str.split(separator)
    while len(str) > 0:
        spath = separator.join(str)+separator+file
        leng = len(str)
        if os.path.exists(spath):
            return spath
        str.remove(str[leng-1])


def getSeparator():
    if 'Windows' in platform.system():
        separator = '\\'
    else:
        separator = '/'
    return separator

def getCurrentFilePath():
    return os.getcwd()