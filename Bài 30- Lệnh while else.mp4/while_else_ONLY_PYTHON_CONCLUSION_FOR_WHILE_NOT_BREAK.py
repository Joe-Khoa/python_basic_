#***********************if_else_*******************

count =sum = 0
print('enter the 5 number: ')

while count < 5:
    x = float(input('enter a number : '))
    if x < 0:
        print('number x < 0, stop canculating: ')
        break
    sum+=x
    count+=1
else:       # print the average
    print('the average number is : ', sum/count)
