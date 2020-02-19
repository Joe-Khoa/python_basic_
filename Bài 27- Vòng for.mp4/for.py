
n = int(input('enter a number'))
s = 0
if n%2 == 0:
    for i in range(0,n+1,2):
        s+=i
else:
    for i in range (1,n+1,2):
        s+=i
print('the sum is: ',s)