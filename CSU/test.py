# a = '\u0001'
# print(a.decode('unicode_escape'))
str1 = '\u0001'
print(str1)
str2 = str1.decode("unicode-escape")
print(str2)