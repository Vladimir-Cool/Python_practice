import os

folder_path = '/\\Eltex_Dir'

def get_file_names():
    subfolder_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()] #мне это не понятно
    list = [f2 for f2 in subfolder_paths if "Eltex8IP_pbx_" in f2]                #Но я как то это написал
    return list
#Выводит список в столбец, мне так удобнее
A = get_file_names()

for i in A:
    start = int(i.rfind("_") + 1)
    end = start + 12
    print(i)
    print(i[start:end])

