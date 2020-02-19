from random import*
while True:
    Machine_No = randrange(1,100)
    win = False
    count = 7
    while count > 0:
        Your_No = int(input(' plz enter a number for lottery : '))
        count-=1
        print('it remains {0} times. '.format(count))
        if Machine_No == Your_No:
            win = True
            print('\n')
            print('####### BOOM - BOOM - BOOM #######')
            print('bingo, you rocked!***ugly_no*** {0} *** '.format(Your_No))
            print('\n')
            break
        if Your_No > Machine_No:
            print("hint: your is GREATER than! ")
        else:
            print('hint: your is LESS than! "')
        print('*'* 40)
    if win is not True:
        print('GaMe OvEr,the ugly number is **** {0} **** stupid!'.format(Machine_No))

    print('Đù you wanna continue ? Y..(*^*)..N')
    if input() is 'N':
        break
    else:
        print('*'*40,'RESTART','*'*40)
        win == False
print('thank for joined time ')

