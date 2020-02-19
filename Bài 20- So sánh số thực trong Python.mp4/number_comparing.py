# ***********EP_SI_LON**************

d1 = 1.11-1.10
d2 = 2.11-2.10
print(d1)
print(d2)

# if(d1 == d2):
#     print('d1 = d2')
# else:
#     print('d1 != d2')
tolerent = 0.000001
threshold = d1-d2

if(threshold <0):
    threshold  = -threshold
if(threshold < tolerent):   # the difference is small AS POSSIBLE
    print('d1 = d2')
else:
    print('d1 != d2')
