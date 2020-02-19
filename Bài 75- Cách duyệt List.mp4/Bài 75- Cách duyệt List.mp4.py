from random import randrange

n = int(input('enter n: '))
lst = [0]*n
print(lst)
for i in range(n):
    lst[i] = randrange(-100,100)
print(lst)
print('*'*50)

for i in lst:
    print(i,end='\t')
print('\n')
print('*'*50)
for i in range(len(lst)):
    print('value of item no {0} is : {1}'.format(i,lst[i]))

print('\n')
print('*'*50)
# revert traversal
for i in range(len(lst)-1,-1,-1):
    print(lst[i])
