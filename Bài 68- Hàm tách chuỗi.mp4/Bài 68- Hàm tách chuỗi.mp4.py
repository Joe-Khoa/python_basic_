# s = "sv01;nguyen van a;1/1/1990"
# arr = s.split(';')
# print(len(arr))
# for item in arr:
#     print(item)
#
# a = "obama"
# b = "kim un un "
# # c = a + b
# # print(c.strip())
# s = """Obama
#     hahaha
#     ali33
#     """
# arr  = s.splitlines()
# for line in arr:
#     print(line,'=>',line.count('a'))


s = """sv01;nguyen van a;1/1/1990
    sv02;nguyen van b;1/1/1992
    sv02;nguyen van c;1/1/1991
    sv; Hồ Đồ;
    """

arr = s.splitlines()
for line in arr:
    arrfor = line.strip().split(';')
    # print(arrfor)
    if len(arrfor) == 3:
        print(arrfor)