
time = int(input("enter the time number"))

hour = time//3600%24
min = time%3600//60
sec = time%3600%60
print(hour,":",min,":",sec)