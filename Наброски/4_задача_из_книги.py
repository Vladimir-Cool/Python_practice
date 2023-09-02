
def glassnue(phrase:str) -> set:
    '''Возвращает гласные найденные в веденном слове'''
    vowels = {'а', 'е', 'о', 'и', 'у', 'я', 'ю', 'ы'}
    found = vowels.intersection(set(phrase.lower()))  #Ну тут я конечно намудрил.
    return found

word = input("Введите слово или фразу: ")
print(glassnue(word))
