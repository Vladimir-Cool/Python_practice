"""
Усложнил все, думаю можно было сделать проще.
"""

count_data = int(input())
dict_data = dict()
while count_data != 0:
    temporary_data = input().split(' : ')
    if temporary_data[1:]:
        dict_data[temporary_data[0]] = (temporary_data[1].split())
    else:
        dict_data[temporary_data[0]] = temporary_data[1:]
    count_data -= 1

count_call = int(input())
list_call = []
while count_call != 0:
    list_call.append(input())
    count_call -= 1


def parent_serch(el, dict_data):
    if dict_data[el]:
        list_parent = dict_data[el].copy()
        temporary_list = dict_data[el].copy()
        while temporary_list:
            i = temporary_list.pop(0)
            if dict_data[i]:
                for j in dict_data[i]:
                    if not j in list_parent:
                        list_parent.append(j)
                        temporary_list.append(j)

    else:
        list_parent = dict_data[el]

    return list_parent


resalt = []
errors = []
for el_call in list_call:
    list_parent = parent_serch(el_call, dict_data)
    if resalt:
       if set(list_parent) & set(resalt):
           errors.append(el_call)
       else:
           resalt.append(el_call)
    else:
        resalt.append(el_call)

for er in errors:
    print(er)

