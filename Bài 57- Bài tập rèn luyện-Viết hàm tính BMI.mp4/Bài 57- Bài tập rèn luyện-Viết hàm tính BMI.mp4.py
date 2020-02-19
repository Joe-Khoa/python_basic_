print('program to calculate weight and the height')

def BMI(BMI):
    if BMI < 18.5:
        print('so SLIM ', 'LOW disease expectant ')
    elif 18.5 <= BMI < 24.9:
        print('normal', 'AVERAGE disease expectant ')
    elif 25 <= BMI < 29.9:
        print('pretty obesity', 'HIGH disease expectant ')
    elif 30 <= BMI < 34.9:
        print('obesity level 1', 'HIGH disease expectant ')
    elif 34 <= BMI < 39.9:
        print('obesity level 2', 'VERY HIGH disease expectant ')
    else:
        print('obesity level 3', 'DANGEROUS disease expectant ')
    print('try again? y/n')
    if input() is 'n':
        print('take care your health')
        _continue = False
    return False
_continue = True
while _continue:
    w = float(input('enter weight (kg): '))
    h = float(input('enter height (m): '))
    bmi = round(w/h**2,2)
    print(bmi)
    _continue = BMI(bmi)


