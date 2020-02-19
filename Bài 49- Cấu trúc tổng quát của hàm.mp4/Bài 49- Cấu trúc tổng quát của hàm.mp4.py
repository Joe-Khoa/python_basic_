def ptb1(a,b):
    if a is 0 and b is 0:
        print('pt has multiple root')
    elif a is 0 and b is not 0:
        print('pt has NO root')
    elif a is not 0:
        print('pt has ONLY root: ', -b/a)
ptb1(3,4)

def printNo():
    print('print_function!')

printNo()