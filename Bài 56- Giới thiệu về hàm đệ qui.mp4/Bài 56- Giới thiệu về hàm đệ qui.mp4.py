# Bài 56- Giới thiệu về hàm đệ qui.mp4

def factorial(n):
    if n is 0:
        return 1
    else:
        return n*factorial(n-1)
n = int(input('enter n: '))
f = factorial(n)
print('{0}! = {1}'.format(n,f))


