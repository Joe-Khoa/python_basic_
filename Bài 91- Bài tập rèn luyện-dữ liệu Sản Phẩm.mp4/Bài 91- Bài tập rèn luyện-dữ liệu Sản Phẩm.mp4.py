def enterString():
    while True:
        string = input()
        delSpaceString = string.replace(' ','')
        if delSpaceString.isalnum() == True:
            string.strip()
            return string
            break
def enterNumber():
    while True:
        string = input()
        if string.isnumeric() == True:
            x = string.strip()
            return str(x)
            break
def enterSVdata():
    dataList = []
    while True:
        print('enter the code: ')
        code = enterString()
        print('enter name : ')
        name = enterString()
        print('enter product price: ')
        price = enterNumber()
        svlst = []
        svlst.append(code)
        svlst.append(name)
        svlst.append(price)
        svData = ';'.join(svlst)+'\n'
        dataList.append(svData)
        print('continue? ')
        if input() != 'y':
            break
    return dataList

def writeFile(path):

    lst = enterSVdata()
    f = open(path,'w',encoding='utf-8')
    for i in lst:
        f.writelines(i)
    f.close()
writeFile('SVdatabase.txt')

def readFile(path):
    f = open(path,'r',encoding='utf-8')
    list = []
    for i in f:
        x = i.split(';')
        list.append(x)
    print(list)
    sortList = []
    for i in range(len(list)):
        a = list[i][2].split()
        sortList.append(a)
    print(sortList)
    f.close()
readFile('SVdatabase.txt')




# def selectSort(array):
#     position = 0
#     for i in range(0, len(array),1):
#         j = i + 1
#         position = i
#         temp = array [i]
#         for j in range(0, len(array),1):
#             if array[j] < temp:
#                 temp = array[j]
#                 position = j
#         array[position] = array[i]
#         array[i] = temp
#     print( array)
#
# array = [42,5,90,4,7,14]
# ar = selectSort(array)
# print(array)
# print(ar)