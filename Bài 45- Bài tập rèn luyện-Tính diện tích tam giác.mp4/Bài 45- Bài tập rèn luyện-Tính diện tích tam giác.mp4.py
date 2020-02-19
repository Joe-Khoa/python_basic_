from math import sqrt

print('enter the line of triangle : ')
while True:
    a = float(input('enter a > 0: '))
    b = float(input('enter b > 0: '))
    c = float(input('enter c > 0: '))

    if a <= 0 or b <= 0 or c <= 0 or (a+b) < c or (a+c) < b or (c+b) < a :
        print(" stupid, don't see the alert? huh. enter AGAIN ")
        print('*'*30,'AGAIN','*'*30)
        continue
    else:
        p = a + b + c
        p_half = p/2
        s = sqrt(p_half*(p_half-a)*(p_half-b)*(p_half-c))
        print('the area of triangle is: ',s)
    break


