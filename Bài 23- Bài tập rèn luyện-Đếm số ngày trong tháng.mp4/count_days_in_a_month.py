
month = int(input('enter a month: '))

if month in (1,3,5,7,8,12):
    print("tháng ", month, 'có 31 ngày')
elif month in (4,6,9,11):
    print('tháng ', month,'có 30 ngày')
elif month == 2:
    year = int(input('check the year, enter year: '))
    if(year%4 ==0 and year%100 != 0) or year%400:
        print('month ',month, 'has 29 days')
    else:
        print('month ',month,'has 28 days')
else:
    print('not a month, invalid!')