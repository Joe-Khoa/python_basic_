def  ptb1(a,b):
    if a is 0 and b is 0:
        return 'MULTIPLE roots'
    elif a is 0 and b is not 0:
        return 'ha NO root'
    elif a is not 0:
        return 'Pt {0}x+{1} = 0 has root: x = {2} '.format(a,b,-b/a)
def print_data(data):
    print(data)

exit_flag = True
while exit_flag:
    a,b = eval(input('enter a,b: ' ))
    x= ptb1(int(a),int(b))
    print_data(x)


    print('continue... y/n ?')
    if input() is 'n':
        exit_flag = False
print('completed, thank you! ')

print(p)