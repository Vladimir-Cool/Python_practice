
s = input()
a = input()
b = input()

num = 0
while s.count(a):

    if a in s:
        s = s.replace(a, b)
    num += 1

    if num > 999:
        break

if num > 999:
    print('Impossible')
else:
    print(num)