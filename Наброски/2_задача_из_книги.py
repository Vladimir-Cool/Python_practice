vowels = ('а', 'е', 'о', 'и', 'у', 'я', 'ю', 'ы')
word = input("Введите слово или фразу: ").lower()  #Метод который приводит все символы к нижнему регистру.
found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)   #Если такого ключа нет в словаре то создаем его.
        found[letter] += 1

for k, v in found.items():
    if not v == 0:
        print('Буква', k, 'встречаеться ', v, 'раз.')