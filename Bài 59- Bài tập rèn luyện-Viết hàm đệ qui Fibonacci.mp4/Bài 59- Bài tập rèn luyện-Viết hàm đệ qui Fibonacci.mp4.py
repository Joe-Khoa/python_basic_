

def fibonaci(n):
    if n is 2  or n is 1:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)
def listFibo(n):
    for i in range(1,n+1):
        print(fibonaci(i),end = '\t')

n = int(input('enter n: '))
# fibo = fibonaci(n)
# print('fibonaci no of {0} is {1}'.format(n,fibo))
listFibo(n)



