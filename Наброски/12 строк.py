#x, y, z = input().strip().split()
#x, y, z = map(int, (x, y, z))

#from functools import reduce
#
#volume = reduce(
#    lambda x, y: x * y,
#    map(int, input().strip().split())
#)

names = ["Вова", "Петя", "Алена", "Вася", "Антон"]
newnames = [name for name in names if name.startswith("А")]
print(newnames)
