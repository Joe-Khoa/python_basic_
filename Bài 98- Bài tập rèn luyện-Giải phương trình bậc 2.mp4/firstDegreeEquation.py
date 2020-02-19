def firstDEqual(a,b):
    if a == 0 and b == 0:
        return 'imnumerable roots'
    elif a == 0 and b != 0:
        return 'not exist root'
    else:
        return str(-b/a)