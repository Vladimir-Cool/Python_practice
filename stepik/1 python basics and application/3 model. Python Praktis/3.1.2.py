s = input()
t = input()
count = 0

while s.count(t):
    s = s[s.find(t) + 1:]
    count += 1

print(count)



