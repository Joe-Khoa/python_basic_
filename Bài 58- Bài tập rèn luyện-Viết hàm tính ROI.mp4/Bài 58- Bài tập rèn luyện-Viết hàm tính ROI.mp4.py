
def invest():
    rev = float(input('enter the revenue: '))
    cost = float(input('enter the cost : '))

    ROI = (rev - cost) / cost
    print('ROI = ', round(ROI, 2))
    if ROI >= 0.75:
        print('should be invested! ')
    else:
        print('should NOT be invested!')
    # return True;
_continue = True
while _continue:
    invest()
    print('continue y/n ?')
    if input() is 'n':
        _continue = False
print('completed, thanks!')