def maxway(list):
    maxw = 0
    home = []
    market = []
    for i in range(len(list)):
        if list[i] == 1:
            home.append(i)
        elif list[i] == 2:
            market.append(i)
    for i in range(len(home)):
        noww = 0
        minw = 10
        for j in range(len(market)):
            noww = abs(market[j] - home[i])
            minw = min(noww, minw)
        maxw = max(maxw, minw)
    return maxw

list = (list(map(int, input().split())))

print(maxway(list))


