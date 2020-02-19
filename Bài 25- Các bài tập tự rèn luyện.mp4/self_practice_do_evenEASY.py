
# enter a number with 2 digit return 'reading letter' eg. 35 three-five
#
# manyStar = '*'*70
tail = '*'*10
# print(tail,'program read the number',tail)
#
# no = int(input('enter a number: '))
# a = no//10
# b = no%10
# noArr = ['zero','one','two', 'three','four', 'five',
#              'six','seven','eight','nine']
# if a == 0:
#     print('the reading of number ', no, 'is :', noArr[b])
# else:
#     print('the reading of number ',no,'is :',noArr[a],'-',noArr[b])
# print(manyStar)

# **********************************************************************
#   enter a day ( d-m-y) return the "next day"

#
# day  = int(input('enter a day: '))
# month  = int(input('enter a month: '))
# year  = int(input('enter a year: '))
# check_month = 1
# check_day = 1
# day_new = day
# month_new = month
# year_new = year
# happy_new_year = ''
# if day == 31 and month == 12:
#     day_new  = 1
#     month_new = 1
#     year_new +=1
#     happy_new_year = 'happy_new_year'
# elif month in (1,3,5,7, 8,10,12):
#     if day > 31:
#         check_day = 0
#     elif day != 31:
#         day_new +=1
#     else:
#         day_new= 1
#         month_new +=1
# elif month in (4,6,9,11):
#     if day > 30:
#         check_day = 0
#     elif day != 30:
#         day_new +=1
#     else:
#         day_new = 1
#         month_new +=1
# elif month == 2:
#     if(year%4 == 0 and year%100 != 0) or year%400 == 0:
#         print('nam nhuan')
#         if day > 29:
#             check_day = 0
#         elif day != 29:
#             day_new +=1
#         else:
#             day_new = 1
#             month_new += 1
#     else:
#         print('khong phai nam nhuan')
#         if day > 28:
#             check_day = 0
#         elif day != 28:
#             day_new +=1
#         else:
#             day_new = 1
#             month_new += 1
# else:
#     check_month = 0
# if check_month == 0 or check_day == 0:
#     print(' NOT a month or a day in a year, invalid day!')
# else:
#     print('the next day of' ,day,'-',month,'-',year, 'is',day_new,'-',month_new,'-',year_new,happy_new_year)

    # **********************************************************************

# enter no a,b and operator

# print(tail,'Program to calculte 2 no',tail)
#
# a = float(input('enter a: '))
# b = float(input('enter b: '))
# op = input('enter operator: ')
# reslt = 0;
# error = 0;
#
# if op == '+':
#     reslt = a+b
# elif op == '-':
#     reslt = a-b
# elif op == '*':
#     reslt = a*b
# elif op == "/":
#     if  b==0:
#         error = 'devide 0'
#     else:
#         reslt = a/b
# else:
#     error = 'not the operator'
# if error != 0:
#     print('error: ',error)
# else:
#     print('the result: a',op,'b = ',reslt)

    # **********************************************************************

# QUIZ:: enter a month return a name of Quarter (season)

print(tail,'which quarter od this month',tail)

month = int(input('Enter this month: '))
error = 0
quater = ''
if month > 12:
    error = ' is not a month'
elif month < 1:
    error = ' is not a month'
elif month > 9:
    quater = 'quater 4_winter'
elif month > 6:
    quater = 'quater 3_autumn'
elif month > 3:
    quater = 'quater 2_summer'
else:
    quater = 'quater 1_spring'
if error != 0:
    print(month,error)
else:
    print(month,' is ',quater)



