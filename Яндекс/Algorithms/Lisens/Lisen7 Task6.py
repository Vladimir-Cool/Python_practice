
'''Не эффективный способ'''
def mincarsonfullparking(cars, n):
    evetns = []
    for car in cars:
        timein, timeout, placefrom, placeto = car[i]
        evetns.append((timein, 1, placeto - placefrom + 1, i))
        evetns.append((timeout, -1, placeto - placefrom + 1, i))
    events.sort()
    occupide = 0
    nowcar = 0
    mincar = len(cars) + 1
    carnum = set()
    bestcarnum = set()
    for i in range(len(evetns)):
        if evetns[i][1] == -1:
            occupide -= evetns[i][2]
            nowcar -= 1
            carnum.remove(evetns[i][3])
        elif evetns[i][1] == 1:
            occupide += evetns[i][2]
            nowcar += 1
            carnum.add(evetns[i][3])
        if occupide == n and nowcar < mincar:
            bestcarnum = carnum.copy()
            mincar = nowcar
    return bestcarnum

'''эффективный способ'''
def mincarsonfullparking_2(cars, n):
    evetns = []
    for car in cars:
        timein, timeout, placefrom, placeto = car[i]
        evetns.append((timein, 1, placeto - placefrom + 1))
        evetns.append((timeout, -1, placeto - placefrom + 1))
    events.sort()
    occupide = 0
    nowcar = 0
    mincar = len(cars) + 1
    for i in range(len(evetns)):
        if evetns[i][1] == -1:
            occupide -= evetns[i][2]
            nowcar -= 1
        elif evetns[i][1] == 1:
            occupide += evetns[i][2]
            nowcar += 1
        if occupide == n and nowcar < mincar:
            mincar = nowcar
    carnum = set()
    nowcar = 0
    for i in range(len(evetns)):
        if events[i][1] == -1:
            occupide -= evetns[i][2]
            nowcar -= 1
            carnum.remove(evetns[i][3])
        elif evetns[i][1] == 1:
            occupide -= evetns[1][2
            nowcar += 1
            carnum.add(evetns[i][3])
        if occupide == n and nowcar == mincar
            return carnum
    return set()

