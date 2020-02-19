# task-1
# # upper
# word = ' string '
# num = word.isalnum()         #check if all char are alphanumeric
# alpha = word.isalpha()         #check if all char in the string are alphabetic
# digit = word.isdigit()         #test if string contains digits
# title = word.istitle()         #test if string contains title words
# upper = word.isupper()         #test if string contains upper case
# lower = word.islower()         #test if string contains lower case
# space = word.isspace()         #test if string contains spaces
# end = word.endswith('d')     #test if string endswith a d
# start = word.startswith('H')   #test if string startswith H
#
# str = ' stringgg '
# j = ['join','']
# format = str.format()
# count = str.count('g')
# find = str.find('i')
# join = ','.join(j)
# # print(join)
# rfind = str.rfind('g')
# # print(rfind)
# # str.center(10)
# # print(str)
# # print(count)
# # print(num)

# *********************** 1 ***********************
s = input('enter string: ')

# 2.1
# no_upper_letter = sum(1 for c in s if c.isupper())
# print('n0 of upper letter is:',no_upper_letter)
# 2.2
# n0_lower_letter = sum( 1 for c in s if c.islower())
# print(n0_lower_letter)
# 2.3
# no_special_letter = 0
# for c in s:
#     if not(c.isalnum()):
#         no_special_letter +=1
# print(no_special_letter)
# 2.4
# no_space = s.count(' ',5)
# print(no_space)
# 2.5
# no_nguyen_am = sum(1 for c in s if c in ['u','e','o','a','i'])
# print(no_nguyen_am)
# 2.6
# no_phu_am = sum( 1 for c in s if c not in ['u','e','o','a','i'] and c.isalpha())
# print(no_phu_am)
# *********************** 2 ***********************

def NegaNoStr(s):
    list = []
    for i in range(len(s)):
        if s[i] == '-':
            if s[i+1].isnumeric() is False:
                continue
            else:
                list.append('-')
                for j in range(i+1,len(s)):
                    if s[j].isnumeric() == True:
                        list.append(s[j])
                    else:
                        break
    return list

def printArr(s):
    arr = NegaNoStr(s)
    string = ''.join(arr)
    arr2 = string.split('-')
    for i in arr2:
        if len(i) != 0:
            print('-'+i)

printArr(s)


# *********************** 3 ***********************
