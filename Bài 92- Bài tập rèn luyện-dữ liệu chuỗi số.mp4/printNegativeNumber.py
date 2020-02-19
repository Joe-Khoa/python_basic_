
from readFile import *

lst = readFile('test.txt')
print(lst)
print('*'*120)
print('\n')

for y in lst:
    for x in y:
        a = int(x)
        if (int(x) < 0) is True:
            print(x,end='\t\t')
    print('')



