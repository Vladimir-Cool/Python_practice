

def searсhwidth(parent, class1, checkset = set()):
    checkset = set()
    while parent:
        parentcopy = set()
        if class1 in parent:
            print('Yes')
            parent = set()
        else:
            for i in parent:
                if not i in checkset:
                    parentcopy = parentcopy.union(base[i])
                    checkset.add(i)
            if parentcopy != set():
                parent = parentcopy
            else:
                parent = set()
                print('No')


base = dict()

n = int(input())
while n:
    x, *d = input()
    d = set(d)
    for i in [' ', ':']:
        if i in d:
            d.remove(i)
    base[x] = set(d)
    n -= 1
k = int(input())

while k:
    l = input()
    class1 = l[0:1]
    class2 = l[-1:]
    if class1 == class2:
        parent = 0
        print('Yes')
    elif base[class2] != set():
        parent = base[class2]
    else:
        parent = 0
        print('No')
    searсhwidth(parent, class1)
    k -= 1


