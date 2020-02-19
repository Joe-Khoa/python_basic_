while True:
    n = int(input('enter prime number: '))
    count = 0
    i = 0
    for i in range(1, n+1):
        if n % i is 0:
            count += 1
    if count == 2:
        print('\t->',n,' is prime number! ')
    else:
        print('\t->',n,' NOT the prime number! ')
    # select = input('continue or not, y or n: ')
    print('continue?, y-n: ')
    if input() == 'y':
        exit()
print("it's over")
