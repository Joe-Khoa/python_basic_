a = [1,2,3,4]
b = [2,3,4,5]

# print('a[1] =',a[1])

b = a # b use memory_block_of_"a"
# print('b[1] =',b[1])
b[3] = 100
print('b[3] =',b[3])
print('a[3] =',a[3])
# ***
c = b # c use memory_block_of_"b"
b[3] = 500
print('*'*10)
print('c[3] =',c[3])
print('b[3] =',b[3])
print('a[3] =',a[3])

