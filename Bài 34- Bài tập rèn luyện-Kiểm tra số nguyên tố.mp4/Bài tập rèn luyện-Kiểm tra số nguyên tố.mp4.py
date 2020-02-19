n = int(input('enter a number: '))

count = 0
for i in range (1,n+1):
    if n%i is 0:
        count+=1
if count == 2:
    print("the number is 'So Nguyen To'")
else:
    print('NOT _so nguyen to')
