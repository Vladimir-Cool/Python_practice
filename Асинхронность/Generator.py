from time import time


def gen_filename():
    while True:
        pattern = "file-{}.jpeg"
        t = int(time() * 1000)
        yield pattern.format(str(t))


## Round Robin
def gen1(stroca):
    for i in stroca:
        yield i

def gen2(n):
    for i in range(n):
        yield i

g1 = gen1("VovaCool")
g2 = gen2(15)

tasks = [g1, g2]

while True:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
