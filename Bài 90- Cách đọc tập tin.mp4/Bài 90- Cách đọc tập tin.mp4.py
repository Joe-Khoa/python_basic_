def writeFile(path):
    f = open(path,'w',encoding='utf-8')
    f.writelines("SV001; Nguyễn Văn Chúc; 1/1/1990\n")
    f.writelines("SV001; Võ Văn Mừng; 1/1/1990\n")
    f.writelines("SV001; Phạm Văn Năm; 1/1/1990\n")
    f.writelines("SV001; Trần Văn Mới; 1/1/1990\n")
    f.close()

writeFile('StuDatabase.txt')

def readFile(path):
    f = open(path,'r',encoding='utf-8')
    for line in f:
        print(line.strip())
    f.close()

readFile('StuDatabase.txt')
