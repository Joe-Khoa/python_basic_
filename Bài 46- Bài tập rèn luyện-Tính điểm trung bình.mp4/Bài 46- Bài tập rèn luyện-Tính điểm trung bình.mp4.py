print('count the avg score : ')

math,physic,chemistry = eval(input("math,physic,chemistry : "))
average = (math+physic+chemistry)/3
print('the avg is ', average)
print('avg after round ', round(average,2))