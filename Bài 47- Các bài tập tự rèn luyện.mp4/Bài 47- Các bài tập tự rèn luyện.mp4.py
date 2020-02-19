# task 1

# from random import *
#
# a = 4.5
# a = 100
# note: range(0,100) exclude(<0 and >99)
# while True:
#     n = randrange(0, 100)
#     print(n,end=',')
#     if n == a:
#         print('can generate : ',a)
#         break

# *****************************************************END TASK-1*************************************************

# task_2
# from math import sqrt
#
# print('count the distance of 2 point: ')
# Xa,Ya  = eval(input('Xa,Ya :'))
# Xb,Yb  = eval(input('Xb,Yb :'))
# distance = sqrt( (Xa - Xb)**2 + (Ya - Yb)**2)
# print('distance AB is :',distance)

# *****************************************************END TASK-2*************************************************

# from math import*
#
# a,X = eval(input('enter: a>0 && #1,X>0 '))
#
# if a > 0 and a != 1 and X > 0:
#     lg = log(a,X)
#     print('logaX = ',lg)

# *****************************************************END TASK-3*************************************************

# task-4

# from math import *
# n = int(input('enter n : '))
# sqrt = sqrt(2)
# i=0
# for i in range(0 , n-1):
#     sqrt = sqrt(sqrt)

# *****************************************************END TASK-4*************************************************

# task-5

import time

for i in range(1,8):
    for j in range(1,8):
        if i < 4 and  j < 4:
            print('  ',end='')
        if i < 4 and j > 3:
            if (i == j-3) or (i == j-2) or (i == j-1):
                print(' *',end='')
            else:
                print('  ',end='')
        if i is 4:
            print(' *',end='')
        if i > 4 and j < 4:
            if (i + j) == 8 or (i + j) == 7  or (i + j) == 6:
                print(' *',end='')
            else:
                print('  ',end='')
        if i > 4 and  j > 4:
            print('  ',end='')
    print('')
time.sleep(5)
# part-2
for i in range(1,8):
    for j in range(1,8):
        if i < 4 and  j < 4:
            print('  ',end='')
        if i < 4 and j > 3:
            if (i == j-3) or (i == j-2) or (i == j-1):
                if i is 3 and j is 5:
                    print('  ', end='')
                else:
                    print(' *',end='')
            else:
                print('  ',end='')
        if i is 4:
            print(' *',end='')
        if i > 4 and j < 4:
            if ((i + j) == 8 or (i + j) == 7  or (i + j) == 6):
                if i is 5 and j is 2:
                    print('  ', end='')
                else:
                    print(' *',end='')
            else:
                print('  ',end='')
        if i > 4 and  j > 4:
            print('  ',end='')
    print('')
time.sleep(5)
#part-3
# print('#'*50)
for i in range(1,8):
    for j in range(1,8):
        # FIELD I<4
        if i < 4 and  j < 4:
            print('  ',end='')
        if i < 4 and j > 4:
            if (i + j == 6) or (i + j == 7) or (i + j == 8):
                if i is 3 and j is 5:
                    print('  ', end='')
                else:
                    print(' *',end='')
            else:
                print('  ',end='')
        if j is 4:
            print(' *',end='')
        if i is 4 and j is not 4:
            print('  ',end='')
            # FIELD I>4
        if i > 4 and j < 4:
            if ((i + j) == 8 or (i + j) == 9  or (i + j) == 10):
                    print(' *',end='')
            else:
                print('  ',end='')
        if i > 4 and  j > 4:
            print('  ',end='')
    print('')
time.sleep(5)
# part-4
# print('#' * 50)
for i in range(1, 8):
    for j in range(1, 8):
        # FIELD I<4
        if i < 4 and j < 4:
            print('  ', end='')
        if i < 4 and j > 4:
            if (i + j == 6) or (i + j == 7) or (i + j == 8):
                if i is 2 and j is 5:
                    print('  ', end='')
                else:
                    print(' *', end='')
            else:
                print('  ', end='')
        if j is 4:
            print(' *', end='')
        if i is 4 and j is not 4:
            print('  ', end='')
            # FIELD I>4
        if i > 4 and j < 4:
            if ((i + j) == 8 or (i + j) == 9 or (i + j) == 10):
                if i is 6 and j is 3:
                    print('  ', end='')
                else:
                    print(' *', end='')
            else:
                print('  ', end='')
        if i > 4 and j > 4:
            print('  ', end='')
    print('')
