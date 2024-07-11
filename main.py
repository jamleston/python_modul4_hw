# from pathlib import Path
# import sys

# def structure(path):
#     pass

# p = Path("C:\\Users\\kasht\\OneDrive\\Documents\\GitHub\\python_modul4_hw\\third")
# result = structure(p)
# print(result)

# print(sys.modules["colorama"])

from colorama import Fore, Back, Style

print(Fore.RED + 'Це червоний текст')
print(Back.GREEN + 'Це текст на зеленому фоні')
print(Style.RESET_ALL)
print('Це звичайний текст після скидання стилю')