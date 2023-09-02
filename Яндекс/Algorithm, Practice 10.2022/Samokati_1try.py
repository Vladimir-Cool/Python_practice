from random import randint


'''Распоковка данных из файла в значения n, m, k. В матрицу matrix и картеж truck'''
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


'''Ищем самый близкий самокат, Мин растояние от текущей точки до самоката'''
def serchnearscoters(start:int, n:int ):
    if n+1 <= start <= m+n+1:
        minpoint = min(matrix[start][1 : n+1])
        minindex = matrix[start].index(minpoint, 1, m+n+1)
    else:
        minpoint = min(matrix[start][1: start] + matrix[start][start +1: n+1])
        minindex = matrix[start].index(minpoint, 1, n+1)
    if minindex in scooters:
        return minindex, minpoint
    else:
        matrix[start][minindex] = 9000000
        return serchnearscoters(start, n)



'''Передвижение грузовика к самокату'''
def gotoscooters(minpoint:int, minindex:int, routelength:int):
    routelength -= minpoint
    temporarypath.append(minindex)      #path['номер грузовика'] деления путей для каждого грузовика
    scooters.remove(minindex)
    start = minindex
    return start, routelength


def collectionscooters(start:int, n:int, routelength:int, filled:int, limit:int):
    while filled != limit:
        minindex, minpoint = serchnearscoters(start, n)
        start, routelength = gotoscooters(minpoint, minindex, routelength)
        filled += 1
        if routelength < 0:
            start, routelength, limit = checkroutelengthcollection(filled, savest,)
            start, routelength, filled = collectionscooters(start, n, routelength, filled, limit)
            return start, routelength, filled
        else:
            return start, routelength, filled


def checkroutelengthcollection( filled, savest:tuple,):
    limit = filled // 2 - 1
    matrix, temporarypath, start, routelength, sumparking = savest
    start, routelength, filled = collectionscooters(start, n, routelength, filled, limit)
    return start, routelength, limit


'''Ищем самое близкое парковочное место, Мин растояние от текущей точки до парковочного места'''
def serchnearparking(start:int, n:int, m:int ):
    if start < (n + 1):                                 #Выезд из 'квадрата' самокатов в 'квадрат' парковок
        minpoint = min(matrix[start][n+1: m+n+1])
        minindex = matrix[start].index(minpoint, n+1, m+n+1)
    else:                                               #Поездки внутри 'квадрата' парковок
        minpoint = min(matrix[start][n+1: start] + matrix[start][start+1: m+n+1])
        minindex = matrix[start].index(minpoint, n+1, m+n+1)
    if minindex in parking:
        return minindex, minpoint
    else:
        matrix[start][minindex] = 9000000
        return serchnearparking(start, n, m)


'''Передвижение грузовика к парковочному месту'''
def gotoparking(minpoint:int, minindex:int, routelength:int):
    routelength -= minpoint
    temporarypath.append(minindex)       #path['номер грузовика'] деления путей для каждого грузовика
    parking.remove(minindex)
    start = minindex
    return start, routelength


def parkingscooters(start:int, n:int, m:int, routelength:int, filled:int , sumparking:int):
    while filled != 0:
        minindex, minpoint = serchnearparking(start, n, m)
        start, routelength = gotoparking(minpoint, minindex, routelength)
        filled -= 1
        sumparking += 1
        if routelength < 0:
            start, routelength, limit = checkroutelengthparking(filled, savest, )
            start, routelength, filled, sumparking = parkingscooters(start, n, m, routelength, filled, sumparking)
        else:
            return start, routelength, filled, sumparking


def checkroutelengthparking(filled, savest:tuple,):
    limit = (50 - filled) // 2 - 1
    matrix, temporarypath, start, routelength, sumparking = savest
    start, routelength, filled = collectionscooters(start, n, routelength, filled, limit)
    return start, routelength, limit


def savestate(matrix:list, temporarypath:list, start:int, routelength:int, sumparking:int):
    copymatrix = matrix[:]
    copytemporarypath = temporarypath[:]
    copystart = start
    copyroutelength = routelength
    copysumparking = sumparking
    return copymatrix, copytemporarypath, copystart, copyroutelength, copysumparking


'''Среднее растояние между точками, для оценки количества перевозимых самокотов'''
def meandistance(n:int, m:int):
    sumdis = 0                  #сумма всех растояний для деления на кол-во
    F = f = (n + m) // 2        #Количество выборки
    while f != 0:
        i = randint(1, n + m)
        j = randint(1, n + m)
        if i != j:
            sumdis += matrix[i][j]
            f -= 1
    meandis = sumdis // F  #среднее растояние в матрице
    return meandis
print('mean distans =', meandistance(n, m))


def approximateamount(routelength:int, meandis:int):
    buffer = (routelength // meandis) - 1                #'-1' это для того чтобы примерно выйти в + по растоянию # после того как развезем самокаты
    if buffer > 25:
        buffer, limit = buffer - 25, 25
    else:
        limit, buffer = buffer, 0
    return buffer, limit



'''Туча переменных'''
path = []   #path = [[]] * k
minpiont = 0
scooters = set(range(1, n+1))
parking = set(range(n+1, m+n+1))
#truckleft = k
#trucknum = 0
meandis = meandistance(n, m)


'''Начало программы'''
for routelength in truck:                   # ТУТ надо придумать как менять местами порядок грузовиков в тапле =/ а никак надо в списке!
    start = 0
    filled = 0
    sumparking = 0
    temporarypath = []
    limit = 25
    savest = ()

    while routelength > meandis:              #А если самокаты закончаться?
        savest = savestate(matrix, temporarypath, start, routelength, sumparking)

        start, routelength, filled = collectionscooters(start, n, routelength, filled, limit)
        #print(path)
        print('собрано самокатов', filled)
        print('точка start', start)
        print(routelength)
        print()
        #Первая проверка. Если растояние падает ниже "0" то фиксируем filled, limit = filled // 2 - 1
        #Таким образом стараемся взять самокаты и довести их до точек

        start, routelength, filled, sumparking = parkingscooters(start, n, m, routelength, filled, sumparking)
        #print(path)
        print('собрано самокатов', filled)
        print('точка start', start)
        print(routelength)
        print()
        print('temporarypath', temporarypath)
        #Вторая проверка. Если растояние падает ниже "0" то фиксируем filled, limit = 50 - filled // 2 - 1
        #Таким образом стараемся взять самокаты и довести их до точек

    temporarypath.append(sumparking)
    path.append(temporarypath)


'''Выводы для проверки'''
#for i in matrix:
#    print(i)
#print('Scooters', scooters)
#print('Parking', parking)

for i in path:
    print('sum',i[-1],  'path', i)
