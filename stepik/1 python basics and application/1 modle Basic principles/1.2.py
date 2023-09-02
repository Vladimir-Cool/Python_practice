#objects = [1, True, 0, False] #6
objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
ans = 0
check = []
#checkbool = [0, 1, True, False]
for obj in objects:
    if obj not in check:
        check.append(obj)
        ans += 1


print(ans)



