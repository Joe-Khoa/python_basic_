from math import sqrt
def SecondDEqual(a,b,c):

    if a == 0:
        if a == 0 and c == 0:
            return('vo so nghiem')
        elif b == 0 and c != 0:
            return('VÔ nghiệm')
        else:
            x = -c / b
            return('nghiem la : ', x)
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return('Vô nghiệm')
        elif delta == 0:
            x = -b / (2 * a)
            return("nghiệm kép x1= x2= ", x)
        else:
            x1 = (-b - sqrt(delta)) / (2 * a)
            x2 = (-b + sqrt(delta)) / (2 * a)
            return('co 2 nghiem x1=', x1, 'x2=', x2)


