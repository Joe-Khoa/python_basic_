from random import randrange

while True:
    x = randrange(0,100)
    print(x,end=',')
    if x is 50:
        break
print('\n','random_over')