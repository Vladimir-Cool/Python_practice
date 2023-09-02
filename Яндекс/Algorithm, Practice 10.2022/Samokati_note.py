
with open('input5.txt') as file:
    matrix = []
    truck = []
    time = 0
    i = 0
    for line in file:
        if time == 0:
            n, m, k = map(int, line.split())
            time += 1
        elif time <= n + m + 1:
            matrix.append(list(map(int, line.split())))
            i += 1
            time += 1
        else:
            truck = tuple(map(int, line.split()))
for i in matrix:
    print(i)



''' Выбирает не посященный самокат из ближайших 
    и передвигаемсяся на его точку.
    Точки собранных самокатов меняются на +inf (9000000)'''
def serchfreescooters(start:int, minpoint:int, minindex:int, filled:int, routelength:int):
    if minindex in scooters:
        matrix[start][minindex] = 9000000
        start, routelength = gotoscooters(minpoint, minindex, routelength)
        filled += 1
        return start, filled, routelength
    else:
        matrix[start][minindex] = 9000000
        return start, filled, routelength


''' Выбираем свободное парковочное место из ближайших
    и передвигаемсяся на его точку.
    Точки занятых парковочных мест меняются на +inf (9000000)'''
def serchfreeparking(start:int, minpoint:int, minindex:int, filled:int, routelength:int):
    if minindex in parking:
        matrix[start][minindex] = 9000000
        start, routelength = gotoparking(minpoint, minindex, routelength)
        filled -= 1
        return start, filled, routelength
    else:
        matrix[start][minindex] = 9000000
        return start, filled, routelength


''' Примерное количество самокатов на грузовик.
    При малых велечинах самокатов помагает распределить самокаты на
    все грузовики, но при больших пока не знаю...
    Тут пока я думаю надо оно мне =/'''
def approximateamount(n:int, k:int, trucknum:int, truckleft:int):
    buffer = 0
    if trucknum == 0:
        trucknum += 1
        truckleft -= 1
        if n <= k * 25:
            limit = n // k + 1
        else:
            limit = 25
            buffer = (n // k) - limit
    else:
        if len(scooters) <= (truckleft * 25):
            limit = len(scooters) // truckleft
            truckleft -= 1
        else:
            limit = 25
            buffer = len(scooters) // truckleft - limit
            truckleft -= 1
    return limit, buffer, trucknum, truckleft