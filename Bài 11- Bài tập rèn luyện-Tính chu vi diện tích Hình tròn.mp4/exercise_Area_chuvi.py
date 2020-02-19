import math
# PI = 3.14
try:
    r = float(input("enter the circle radius: "))
    CV = 2*math.pi*r
    AR =math.pi*r**2

    print("chu_vi: ", CV)
    print("area: ",AR)
except:
    print('error found')