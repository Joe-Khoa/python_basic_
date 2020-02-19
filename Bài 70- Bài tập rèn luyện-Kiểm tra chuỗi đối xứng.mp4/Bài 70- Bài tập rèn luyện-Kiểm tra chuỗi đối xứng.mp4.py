def symetric(s):
    flag = True
    for i in range(len(s)):
        if s[i] != s[len(s) - i -1]:
            flag = False
            break
    return flag

s = input('enter a string: ')
print(symetric(s))