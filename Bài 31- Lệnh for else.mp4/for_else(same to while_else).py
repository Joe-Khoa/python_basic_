a  = int(input('enter a number : '))
sum = 0

for n in range(5,10):
    if 4%a == 1:
        print('Exit the for_loop')
        break
    sum +=n
else:
    print('the sum _ when a#3, a==2: ',sum)