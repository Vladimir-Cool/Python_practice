from datetime import datetime

'''Фильтр по времени. Строку времени приобразуем в тип "Время" для сравнения'''
def Filtertime(DATE_min:str, DATE_max:str, DATE:str) -> bool:
  d_min, m_min, y_min = map(int, DATE_min.split('.'))
  d_max, m_max, y_max = map(int, DATE_max.split('.'))
  d, m, y = map(int, DATE.split('.'))
  Datemin = datetime(y_min, m_min, d_min)
  Datemax = datetime(y_max, m_max, d_max)
  Date = datetime(y, m, d)
  if not(Datemin <= Date <= Datemax):
      return True

'''Сортирует словари в списке по значению ключа "id"'''
def Sortlistdict(L:list) ->list :
  i = 0
  while i < len(L) - 1:
    j = 0
    while j < len(L) - 1 - i:
      if L[j]['id'] > L[j + 1]['id']:
        L[j], L[j + 1] = L[j + 1], L[j]
      j += 1
    i += 1

'''Фильтр по подстраки в поле "name" и по "price". Затем вызов фильтра по времени и сортировка словарей в списке'''
def Filter(List, NAME_contain, PRICE_min, PRICE_max, DATE_min, DATE_max):
  for i in range(len(List) - 1, -1, -1):
    if List[i]['name'].lower().find(NAME_contain) == -1:
      List.pop(i)
    elif not(PRICE_min <= List[i]['price'] <= PRICE_max):
        List.pop(i)
    elif Filtertime(DATE_min, DATE_max, List[i]['date']):
      List.pop(i)
  Sortlistdict(List)
  return List


List = [{"id": 1, "name": "Asus notebook", "price": 1564, "date": "23.09.2021"},
        {"price": 2500, "id": 3, "date": "05.06.2020", "name": "Keyboardpods"},
        {"date": "23.09.2021", "name": "Airpods","id": 5, "price": 2300},
        {"name": "EaRPoDs", "id": 2, "date": "01.01.2022", "price": 2200},
        {"id": 4, "date": "23.09.2021", "name": "Dell notebook",  "price": 2300}]

NAME_CONTAINS = 'pods'
PRICE_GREATER_THAN = 2200
PRICE_LESS_THAN = 2400
DATE_AFTER = '23.09.2021'
DATE_BEFORE = '02.01.2022'

print(Filter(List, NAME_CONTAINS, PRICE_GREATER_THAN, PRICE_LESS_THAN, DATE_AFTER, DATE_BEFORE))

