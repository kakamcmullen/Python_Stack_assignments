
a = ['magical unicorns', 19, 'hello', 98, 'world']
b = [2, 3, 1, 7, 4, 12]
c = ['magical', 'unicorns']

li = a
newli = ""
s = 0.00
for item in li:
    if type(item) is int:
        s = s + item
    elif type(item) is str:
        newli = newli + " " + item
print newli
print s


