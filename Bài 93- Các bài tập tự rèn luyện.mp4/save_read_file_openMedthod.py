import os
def saveFile(path,data = [],method ='a'):
    # if os.path.isfile(path) is True:
    #     file = open(path,'a',encoding='utf-8')
    # else:
    file = open(path, method, encoding='utf-8')

    for line in data:
        file.writelines((line+'\n'))
        # file.writelines((line))

    file.close()
    return True
def readFile(path):
    file = open(path,'r',encoding='utf-8')
    data = []
    for line in file:
        data.append(line)
    file.close()
    return data

