n = int(input('enter the height : '))

# for i in range(n):
#     for j in range(n):
#         if  j==0 or i==j or j==n-1:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print('')   # new line

## use while
i=0
while i<n:
    j = 0
    while j<n:
        if j==0 or j==n-1 or i==j:
            print(i,end='')   # print continuous, not begin a new line
        else:
            print(' ',end='')
        j+=1
    i+=1
    print('')
