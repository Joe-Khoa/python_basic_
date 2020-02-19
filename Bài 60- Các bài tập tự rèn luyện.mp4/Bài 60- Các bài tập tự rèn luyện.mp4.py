# def sum1(n):
#     s = 0
#     while n > 0:
#         s += 1
#         n -= 1
#     return s
#
# def sum2():
#     global val
#     s = 0
#     while val > 0:
#         s += 1
#         val -= 1
#     return s
#
# def sum3():
#     s = 0
#     for i in range(val,0,-1):
#         s += 1
#         val -= 1
#     return s
#
# def main():
#     global val
#     val = 5
#     print(sum1(5))
#     print(sum2())
#     print(sum3())
#
# main()
#


# *******************************************END_TASK_2*******************************************

# def listing(a,b):
#     list = []
#
#     for i in range (a,b+1,1):
#         list.append(i)
#         list.append(-i)
#
#     for x in range(len(list)):
#         print(list[x],end=' ')
#         if x%2 ==1:
#             print('\t',end='')
# listing(-6,5)

# *******************************************END_TASK_3*******************************************

def caregorizeNo(n):

    i = 0
    count = 0
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            count +=1
            sum +=i

    print('count = {0}, sum = {1}'.format(count,sum))
    if sum == n:
        print(n,'is the perfect no!')
    elif sum > n:
        print('Abundant no!')
    else:
        print('nothing!')

n = int(input('enter a no > 0: '))
caregorizeNo(n)


