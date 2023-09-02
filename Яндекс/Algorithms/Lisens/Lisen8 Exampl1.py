    '''Менеджер файлов'''
def initmemory(maxn):
    memory = []
    for i range(maxn):
        memory.append([0, i + 1, 0]) #Ключь, "левый сын", "правый сын"
        return [memory, 0]           #Список, указатель на первый свободный

def newnod(memstruct):
    memory, firstfree = memstruct
    memstruct[1] = memory[firstfree][1]
    return firstfree

def delnode(memstruct, index):
    memory, firstfree = memstruct
    memory[index][1] = firstfree
    memstruct[1] = index

    '''Бинарное дерево'''

def find(memstruct, root, x):
    key = memstruct[0][root][0]
    if x == key:
        return root
    elif x < key:
        left = memstruct[0][root][1]
        if left == -1:
            return -1
        else:
            return find(memstruct, left, x)
    elif x > key:
        right = memstruct[0][root][2]
        if right == -1
            return -1
        else:
            return find(memstruct, right, x)

def createfillnode(memstruct, key):
    index = newnode(memstruct)
    memstruct[0][index][0] = key
    memstruct[0][index][1] = -1
    memstruct[0][index][2] = -1
    return index

def add(memstruct, root, x):
    key = memstruct[0][root][0]
    if x < key:
        left = memstruct[0][root][1]
        if left = -1:
            memstruct[0][root][1] = createfillnode(memstruct, x)
        else:
            add(memstruct, left, x)
    elif x > key:
        rigth = memstruct[0][root][2]
        if rigth == -1
            memstruct[0][root][2] = createfillnode(memstruct, x)
        else:
            add(memstruct, rigth, x)


memstruct = initmemory(20)
root = createfillnode(memstruct, 8)
add(memstruct, root, 10)