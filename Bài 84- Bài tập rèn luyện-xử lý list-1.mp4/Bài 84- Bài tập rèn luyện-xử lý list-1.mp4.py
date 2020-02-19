from random import randrange


def listCreate(n):
    lst = [1]*n
    for i in range(n):
        lst[i] = randrange(0,101)
    return lst


def appendList(lst,e,p):
    p = str(p)
    if p.isnumeric() == False:
        lst.append(e)
    else:
        lst.insert(e,int(p))
    return lst

# n = int(input('enter no of element : '))
# n = 5
# list = listCreate(n)
# print(list)
############################### TASK 2 ###############################
# e = input('enter an element : ')
# p = input('position: ')
# apList = appendList(list,e,p)
# print(apList)

############################### TASK 3 ###############################
# list = ['a','b','c','a', '1',2,5,2,2,5,3,5,'a']
# k = input('enter k to be search : ')
# def searchStr(list,k):
#     if k.isnumeric() == True:
#         k = int(k)
#     return list.count(k)
# count = searchStr(list,k)
# print(count)

############################### TASK 3 ###############################
list = ['a','b','c','a', '1',2,5,2,2,5,3,5,'a']

def checkPrimNo(n):
    count = 0
    for i in range(1,n):
        if n%i == 0:
            count+=1
    if count == 1:
        return True
    else:
        return False

# def primeNoSum(list):
#     sum = 0
#     for c in list:
#         c = str(c)
#         if c.isnumeric() == True:
#             c = int(c)
#             if checkPrimNo(c) == True:
#                 # print(c ,end='\t')
#                 sum +=c
#                 # print(sum ,end='\t')
#     return sum
#
# sum = primeNoSum(list)
# print(sum)

############################### TASK 3 ###############################
# list = [2,5,2,2,5,3,5]
# print(list)
# l= sorted(list)
# list.sort()
# print(list)
# print(l)

list = [2,5,2,2,5,3,5]

def deleleList(list,P_V,data):
    if P_V == 'p':
        list.pop(data)
    elif P_V == 'v':
        for i in range(len(list)-1,-1,-1):
            if list[i] == data:
                list.pop(i)
            # print(len(list))
            # print(i)
    else:
        return 'choose action!'

deleleList(list,'v',5)
print(list)









