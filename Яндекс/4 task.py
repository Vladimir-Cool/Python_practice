J = input()
S = input()
#J = "ab"
#S = "aabbccd"
result = 0
for s in S:
    if s in J:
        result += 1
print(result)