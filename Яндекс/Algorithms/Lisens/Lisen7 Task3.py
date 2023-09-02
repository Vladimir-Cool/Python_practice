def bosscounters(n, tin, tout, m, tboss):
    events = []
    for i in range(n):
        events.append((tin[i], -1))
        events.append((tout[i], 1))
    for i in range(m):
        events.append((tboss[i], 0))
    events.sort()
    online = 0
    bossant = []
    for i in range(len(events))
        if events[i][1] == -1:
            online += 1
        elif events[1][1] == 1:
            online -= 1
        else:
            bossant.append(online)
    return bossant