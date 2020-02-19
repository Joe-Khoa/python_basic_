i=j=0
for i in range (1,10):
    for j in range(1,10):
        tuple = "{0:>2} x {1:>1} = {2:>2}".format(i,j,i*j)
        print(tuple,end = '\t\t')
    print(' ')
