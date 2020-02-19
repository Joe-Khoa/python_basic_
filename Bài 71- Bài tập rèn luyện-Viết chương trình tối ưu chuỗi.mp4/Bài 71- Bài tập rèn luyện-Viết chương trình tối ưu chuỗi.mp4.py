
s = "   Nguyễn Văn  Lam "
s1 = s.strip()
print(len(s))
print(len(s1))
arrS2 = s1.split(" ")
string = ''
for i in arrS2:
    if len(i.strip()) != 0:
        string = string + i + ' '
string = string.strip()
print(len(string))
print(string)

