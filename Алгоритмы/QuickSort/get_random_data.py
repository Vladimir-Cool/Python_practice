import random

with open("list1000.txt", "w") as file:
    for el in range(1000):
        file.write(str(random.randint(1, 10000)) + "\n")

