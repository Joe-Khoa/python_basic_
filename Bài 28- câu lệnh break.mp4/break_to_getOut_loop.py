
#
# while True:
#     x = int(input('enter number'))
#     if x%2 == 0:
#         print('even no')
#     else:
#         print('odd no')
#     q = input('continue ? y/n')
#     if q == 'n':
#         break
# print('thank thím have used this sw!')

# ******************************


n = int(input('enter n'))
s = 0

for i in range(1,n+1):
    s+=i
    print('sum: ',s)
    if s >= 15:
        break
print('final sum is 10: ',s)
