def fn(n, m=0):
    s = 0
    for i in range(0,m+n,1):
        s+=i
    return s
print(fn(5,1))