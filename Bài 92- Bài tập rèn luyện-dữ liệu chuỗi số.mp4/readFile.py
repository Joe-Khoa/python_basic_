
def readFile(path):
    f = open(path,'r',encoding='utf-8')
    lst = []
    for i in f:
        a = i.split(',')
        lst.append(a)
    f.close()
    return lst
