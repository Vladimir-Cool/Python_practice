def isparkingfull(cars, n):
    evetns = []
    for car in cars:
        timein, timeout, placefrom, placeto = car[i]
        evetns.append((timein, 1, placeto - placefrom + 1))
        evetns.append((timeout, -1, placeto - placefrom + 1))
    events.sort()
    occupide = 0
    for i in range(len(evetns)):
        if evetns[i][1] == -1:
            occupide -= evetns[i][2]
        elif evetns[i][1] == 1:
            occupide += evetns[i][2]
        if occupide == n:
            return True
    return False
