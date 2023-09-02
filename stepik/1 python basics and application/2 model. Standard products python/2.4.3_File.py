from os import listdir, getcwd, chdir, walk
from os.path import abspath
from shutil import copy, copytree

# переход в новую директорию
# print(chdir('main'))

# Узнать в какой директории мы сейча
# print(getcwd())

# Узнаем обсялютный путь
#print(abspath('main'))

#копирует файл
#copy('test1.txt', 'copytest1.txt')


answer = []
# рекурсивный проход по папкам Как по дереву видимо
for current_dir, dirs, files in walk('C:\main'):

    for file in files:
        if file[-3:] == '.py':
            answer.append(current_dir[3:])

            break


answer = list(set(answer))
answer.sort()
print(repr(answer))

with open('answer.txt', 'w') as ans:
    ans.write('\n'.join(answer))




