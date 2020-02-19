def saveFile(path):
    file = open(path,'w',encoding='utf-8')
    file.writelines("SV001; Nguyễn Văn Chúc; 1/1/1990\n")
    file.writelines("SV001; Võ Văn Mừng; 1/1/1990\n")
    file.writelines("SV001; Phạm Văn Năm; 1/1/1990\n")
    file.writelines("SV001; Trần Văn Mới; 1/1/1990\n")
    file.close()

saveFile('studentDataBase.txt')