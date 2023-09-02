def maxvisitorsonline(n, tin, tout):
    events = []
    for i in range(n):
        events.append((tin[i], -1))
        events.append((tout[i], 1))
    events.sort()
    online = 0
    notymptytime = 0
    for i in range(len(events)):
        if online > 0:
            notymptytime += events[i][0] - events[i - 1][0]
        if events[i][1] == -1:
            online += 1
        else:
            online -= 1
    return notymptytime