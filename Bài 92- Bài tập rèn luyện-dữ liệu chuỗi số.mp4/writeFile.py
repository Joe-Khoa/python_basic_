def writeFile(string):
    f = open('test.txt','w')
    f.writelines(string)
    f.writelines('\n')
    f.close()
