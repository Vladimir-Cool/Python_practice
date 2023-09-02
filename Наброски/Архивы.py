### Модуль tarfile
import tarfile

#Разархивирует TAR архив в указанную директорию.
#with tarfile.open("C:\\Users\\fagot\\PycharmProjects\\Учеба\\Eltex_Dir\\config_EltexTAU8_template.tgz") as tar:
#    tar.extractall("C:\\Users\\fagot\\PycharmProjects\\Учеба\\Eltex_Dir\\")

#Создание архива TAR
#with tarfile.open("C:\\Users\\fagot\\PycharmProjects\\Учеба\\Eltex_Dir\\New_tar.tgz", "w:gz") as new_tar:
#    new_tar.add(".\\tmp", recursive=True)
#Архив создается, но добавляются лишние директории, надо разбираться.

#Выдает список файлов в архиве
#with tarfile.open("C:\\Users\\fagot\\PycharmProjects\\Учеба\\Eltex_Dir\\test_arhiv.tgz", "r") as add_tar:
#    print(add_tar.getmembers())

# Попытка добавить файл в сжатый архив, неуспешно
#with tarfile.open("C:\\Users\\fagot\\PycharmProjects\\Учеба\\Eltex_Dir\\test_arhiv.tgz", "w:gz") as add_tar:
#    add_tar.add("C:\\Users\\fagot\\PycharmProjects\\Учеба\\Eltex_Dir\\Eltex8IP_pbx_e0d9e37d7fea.cfg", arcname="tmp/etc/config/pbx")

#--------------------------------------------------------------------------------------------------------------------------------
### Модуль shutil
import shutil

ShutilNew = "C:\\Users\\fagot\\PycharmProjects\\Учеба\\Eltex_Dir\\ShutilNew"
root_dir = "/\\Eltex_Dir\\tmp0"
base_dir = "tmp"
shutil.make_archive(ShutilNew, 'gztar', root_dir, base_dir)

