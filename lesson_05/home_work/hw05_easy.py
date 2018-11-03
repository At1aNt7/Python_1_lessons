# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys
import shutil

"""
try:
    for i in range(1, 9):
        os.mkdir("dir_" + str(i))
except FileExistsError:
    print("Папка создана")

try:
    for i in range(1, 9):
        os.rmdir("dir_" + str(i))
except FileExistsError:
    print("Папка удалена")
"""

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
"""
list = os.listdir()
for i in list:
    print(i)
"""
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
"""
def script_copy():
    shutil.copy(sys.argv[0], f'{os.getcwd()}\\copy.py')
script_copy()
"""