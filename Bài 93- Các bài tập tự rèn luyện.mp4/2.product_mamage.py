from save_read_file_openMedthod import *
def inputString():
    loop1 = True
    while loop1:
        name = input('')
        plainName = name.replace(' ', '').isalpha()
        flag = True if plainName else True
        if flag is True:
            loop1 = False
            return name
########################### _____ ###########################
def createCategory():
    data = []
    id = 0
    while True:
        id +=1
        print('enter product name : ')
        name = inputString()
        data.append(str(id) + ',' + name)
        print('*'*30)
        print("continue? press 'n' to exit")
        if input() == 'n':
            break
    print("do you wanna save this ? press 'n' to skip saving1")
    if input() =='n':
        print('this will be not saved!')
        exit()
    saveFile('categories.txt',data)
    return data
########################### _____ ###########################
def createProduct():
    products = []
    id = 0
    while True:
        flag = True
        prod = ''
        id += 1
        print('enter product name : ')
        name = inputString()
        type_id = 0
        while flag:
            print('enter type name : ')
            type_name = inputString().strip()
            typeData = readFile('categories.txt')
            for i in range(len(typeData)):
                type = typeData[i].split(',')
                typeTuple = type[1].strip()
                if typeTuple == type_name:
                    type_id = type[0]
                    prod = str(id)+','+name+','+type_id
                    flag = False
        products.append(prod)
        print("continue? press 'n' to exit")
        if input() == 'n':
            break
    print("do you wanna save this ? press 'n' to skip saving1")
    if input() == 'n':
        print('this will be not saved!')
        exit()
    saveFile('products.txt',products,'a')
    return products
########################### _____ ###########################
def clearEmpty(arr):
    a = []
    for x in arr:
        if x != '':
            a.append(x.strip())
    return a
########################### _____ ###########################
def delProd(id):
    products = readFile('products.txt')
    lst = []
    lst = clearEmpty(products)
    print(lst)
    for i in range(len(lst)-1,-1,-1):
        prod = (lst[i].split(','))[0].strip()
        if id == int(prod):
            lst.pop(i)
    a = clearEmpty(lst)
    # print(a)
    saveFile('products.txt',a,'w')
########################### _____ ###########################
# createProduct()
# print(readFile('products.txt'))
delProd(2)
print(readFile('products.txt'))
