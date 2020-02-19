# matrix = [
#             [1,2,3],
#             [4,5,6],
#             [7,8,9],
#         ]
# print(matrix)
# print('*'*35)
# for row in matrix:
#     for col in row:
#         print(col,end='\t')
#     print('')
# print('*'*35)
#
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         print(matrix[row][col],end='\t')
#     print('')
# print('#'*35)
from random import randrange

def maxtrixCreate(row,col):
    row = int(row)
    col = int(col)
    matrix = [[0]*col]*row
    mat =[]
    # print(matrix)
    for row in range(len(matrix)):
        rowApp = []
        for col in range(len(matrix[row])):
            rowApp.append(randrange(-100,101))
        mat.append(rowApp)
    return mat

def printMt1(matx):
    for row in matx:
        for col in row:
            print(col,end='\t'*2)
        print('')

def prinMt2(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end ='\t'*2 )
        print('')

row, col = eval(input('row x row: '))
prinMt2(maxtrixCreate(row,col))

