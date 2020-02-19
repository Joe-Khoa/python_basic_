from random import randrange

def creatListMxN():
    m,n = eval(input('enter row,col: '))
    matrix = [[1]*n]*m
    # print(matrix)
    newMax = []
    for row in range(m):
        row = []
        for col in range(n):
            row.append(randrange(-100,101))
        newMax.append(row)
    return newMax

def printList(list):
    for row in list:
        for col in row:
            print(col,end = '\t'*2)
        print('')
matrix = creatListMxN()

printList(matrix)

########################### TRACK 2 ###########################

def printDefLine(list,line):
    for col in list[line]:
        print(col,end = '\t'*2)

def printDefCol(list, col):
    for row in range(len(list)):
        print(list[row][col])

# printDefLine(matrix,1)
# printDefCol(matrix,1)

def MaxInList(list):
    Max = list[0][0]
    for row in list:
        for col in row:
            if col > Max:
                Max = col
    return Max
max = MaxInList(matrix)
print('\n','max = ',max)
