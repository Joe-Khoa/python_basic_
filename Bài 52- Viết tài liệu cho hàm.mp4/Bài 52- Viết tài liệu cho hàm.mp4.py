
def UCLN(a,b):
    """ Function use for find the max ước of 2 number a and b
    e.g : 8 and 12 has the max ước is 4 """
    min = a if a > b else b
    i =0
    for i in range(min,0,-1):
        if a%i is 0 and b%i is 0:
            return i
a,b = eval(input('enter a,b : '))
uoc = UCLN(int(a),int(b))
print(uoc)
