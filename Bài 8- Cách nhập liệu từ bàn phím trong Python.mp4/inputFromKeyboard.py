# ********************* STRING

# print("plz enter sth: ")
# s=float(input("plz enter sth: "))
# print("entered :",s)
# print("type of data:", type(s))

# ********************* STRING
#     x = int(input())
#     print('enter x: ',x)
#
def StrToBool(s):
    return s.lower() in ('yes','true','t',"1")
x = StrToBool(input("plz enter true or false"))
print("x bool:",x)
print("type x: ", type(x))

# ***************
# s = input("plz enter sth:")
# print(s)
