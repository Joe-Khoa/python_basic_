g = 5
def increment():
     global g   # g = 3
     g = 2
     g+=1
# increment()
# print(g)
# x =10
def decrease():
    global x
    x=1
decrease()
print(x)