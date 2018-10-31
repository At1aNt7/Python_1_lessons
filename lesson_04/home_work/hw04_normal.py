# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
"""
#с re

import re

foo = "mtMmEZUOmcq"
low_foo = re.findall(r"([a-z]+)", foo)
print(low_foo)

#без re

bar = "mtMmEZUOmcq"
bar = list(bar)
for letters in bar:
    if letters.isupper():
        bar[bar.index(letters)] = "."
bar = ''.join(bar)
bar = bar.split(".")
lower_letters = [letters_lower for letters_lower in bar if letters_lower.islower()]
print(lower_letters)
"""

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
"""
import re

letters = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
pattern = (r"[a-z]{2}([A-Z]+)[A-Z]{2}")
new_letters = re.findall(pattern, letters)
print(new_letters)
"""

#без re (попытался попробовать предыдущим способом, как задаче 1 =) )

bar = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
bar = list(bar)
for letters in bar:
    if letters.islower():
        bar[bar.index(letters)] = "."
bar = ''.join(bar)
bar = bar.split(".")
isupper_letters = [letters_isupper for letters_isupper in bar if letters_isupper.isupper()]
print(isupper_letters)



# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

