# lst = [-1,5,10,120,90,-123]
#
# print(lst[0])
# print(lst[-2])
# print(lst[lst[2]])

##################### TASK 2 #####################

# lst = [-1,5,10,120,90,-123]
#
# print(lst[0:3])
# print(lst[4:8])
# print(lst[:])
# print(lst[:4])
# print( -1 in lst)

##################### TASK 3 #####################
from random import randrange

# n = int(input('enter n : '))
# lst = []
# for i in range(n):
#     while True:
#         r = randrange(0,n*100)
#         if r not in lst:
#             lst.append(r)
#             break
# print(lst)

##################### TASK 4 #####################

# n = int(input('enter n number: '))
# lst = []
# i = int(input('enter number: '))
# lst.append(i)
# count=0
# while  count < n-1 :
#     print(n-1-count,'number is needed to add: ')
#     i = int(input('enter number: '))
#
#     if lst[count] < i:
#         lst.append(i)
#         count+=1
#
# print('\n',lst)

##################### TASK 5 #####################

# n = int(input('enter size of list : '))
# lst = []
# count=0
# while  count < n :
#     print(n-count,'number is needed to add: ')
#     i = int(input('enter number: '))
#     lst.append(i)
#     count+=1
# print(lst)
# lst.sort(reverse = True)
# print(lst)

##################### TASK 5 #####################

from pprint import pprint
#
# lst = {11,3,5,144.,12,89,331,41,53,35, 46,90,92}
#
# def evenOdd(lst):
#     odd = []
#     even = []
#     for i in lst:
#         if i%2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     print(even,'qty : ',len(even))
#     print('\n',odd,'qty : ',len(odd) )
# evenOdd(lst)
#
# def primeNo(lst):
#     prime = []
#     notPrime = []
#     for i in lst :
#         count = 0
#         i = int(i)
#         for j in range(1,i):
#             if i % j == 0 :
#                 count +=1
#         if count ==1:
#             prime.append(i)
#         else:
#             notPrime.append(i)
#     print(prime,'qty : ',len(prime))
#     print('\n',notPrime,'qty : ',len(notPrime) )
#
# primeNo(lst)


##################### TASK 6 #####################


# lst = {11,3,5,144.,12,89,331,41,53,35, 46,90,92}
#
# def enterNumber():
#     while True:
#         c = input('enter a num :')
#         if c.isnumeric() == True:
#             c = int(c)
#             return c
def printMax(matrix):
    for row in matrix:
        for col in row:
            print(col, end='\t')
        print('')
#
# # ##### 7.1
# def setUp():
#     row, col = eval(input('enter row,col: '))
#     matrix = [[0]*col]*row
#     # printMax(matrix)
#     goalMaxtrix = []
#     temp = 0
#     for y in matrix:
#         alias = []
#         for x in y:
#             temp += 1
#             print((temp), end='\t')
#             print('enter Element[{0}][{1}]'.format(y,x))
#             alias.append(enterNumber())
#         goalMaxtrix.append(alias)
#     return goalMaxtrix
# print(setUp())

# A  = [[3, 3, 3, 3], [4, 3, 42, 4], [2, 4, 4, 3]]
# B  = [[2, 4, 1, 5], [2, 5, 7, 6], [19, 2, 2, 4]]
# print(A)
# print(B)
# def maxtrixAdd(a,b):
#     C = []
#     for row in range(len(a)):
#         alias = []
#         for col in range(len(a[row])):
#             x = a[row][col]  + b[row][col]
#             # print(a[row][col])
#             alias.append(x)
#         C.append(alias)
#     return C
# print(maxtrixAdd(A,B))

# def permutationMatrix(matrix):
#     # goalMatrix = [[0]*len(matrix[0])]*len(matrix)
#     goalMatrix = []
#     print(matrix[1][2])
#     for row in range(len(matrix)):
#         temp = []
#         for col in range(len(matrix[row])):
#             x = matrix[col][row]
#             temp.append(x)
#         goalMatrix.append(temp)
#     return goalMatrix
#
# MxM =[[1, 2, 3],[4, 5, 6], [7, 8, 9]]
# M = permutationMatrix(MxM)
# printMax(MxM)
# print('*'*30,end='')
# print('\n')
# printMax(M)
    ################# SOLUTTION-2 #################
mm =[[1, 2, 3],[4, 5, 6], [7, 8, 9]]
def permutationMatrixSecond(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if row < col:
                temp = matrix[col][row]
                matrix[col][row] = matrix[row][col]
                matrix[row][col] = temp
    return matrix

printMax(mm)
print('*'*30,end='')
print('\n')
printMax(permutationMatrixSecond(mm))

