#task_1
# print('\n')
# a=0
# while a<100:
#     if a and a%10 is 0:
#         print('')
#     line = "{0:>2}".format(a)
#     print(line,'*',end=' ', )
#     a+=1
#
# print('\n',"total items is : ",a)

# task-2
# count=1
# a=0
# while a<100:
#     b=0
#     while b<40:
#         if (a+b)%2 is 0:
#             print("{0:>4}".format(count),'*',end=' ')
#             count+=1
#         if count !=0 and count%11==0:
#             print(' ')
#         b += 1
#
#     a+=1

# task 3


# for i in range(5):
# for i in range(5,10):
# for i in range(5,20,3):
# for i in range(20,5,-1):
# for i in range(20, 5, -3):
# for i in range(20, 5, -3):
# for i in range(0):
# for i in range(10, 101, 10):
# for i in range(10, -1, -1):
# for i in range(-3,4):
# for i in range(0,10,1):
#     print(i, ' ',end='')

# task-4
# count =1
# for a in range(20,100,5):
#     print(count,'.*  ',end='')
#     count+=1
# print('')

# task-5

# done=False
# n,m = 0,100
#
# while not done and n!=m:
#     n = int(input('enter n: '))
#     if n < 0:
#         done = True
#     print('exit_loop_with: n = ',n)


# n,m = 0,100
# while n!=m:
#     n = int(input('enter n : '))
#     if n < 0:
#         break;
# print('exit_loop_with: n = ',n)


# n=int(input('enter the level of matrix: '))
# i=0
# for i in range (n):
#     j=0
#     for j in range (n):
#         if i is 0 or i is n-1 or j is 0 or j is n-1:
#             print('*',end=' ')
#         else:
#             print('x',end=' ')
#     print('')

# n = int(input('enter the n: '))
# i=0
# for i in range(n):
#     j = 0
#     for j in range(n):
#         if i+j<n-1:
#             print(' ',end='\t')
#         else:
#             print('*',end='\t')
#     print('')

import math

# n = int(input('enter the number n lẻ: '))
# if n%2 ==0:
#     int(input("plz enter odd number: "))
# else:
#     avg = n//2
#     i=0
#     print(avg)
#     for i in range (n):
#         j=0;
#         for j in range(n):
#             if (j is 0 and i < avg) or (j is (n-1) and i>avg ) or (i == avg) or (i == j):
#             # if i==j :
#                 print('*', end=' ')
#             else:
#                 print('_',end=' ')
#         print('')
#
