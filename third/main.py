from pathlib import Path
import sys
import os
from colorama import Fore, Back, Style

path = sys.path[0]
print('thats the path: ', path)

def structure(path):

    level1 = os.listdir(path)
    
    for file in level1:
        new_path0 = path + '\\' + file
        if os.path.isfile(new_path0):
            print(Fore.RED + "-", file)
        else:
            print(Fore.GREEN + "-", file)
            
            level2 = os.listdir(new_path0)

            for file in level2:
                new_path1 = new_path0 + '\\' + file
                if os.path.isfile(new_path1):
                    print(Fore.RED +"    -", file)
                else:
                    print(Fore.GREEN + "    -", file)

                    level3 = os.listdir(new_path1)

                    for file in level3:
                        new_path2 = new_path1 + '\\' + file
                        if os.path.isfile(new_path2):
                            print(Fore.RED +"         -", file)
                        else:
                            print(Fore.GREEN + "         -", file)

                            level4 = os.listdir(new_path2)

                            for file in level4:
                                new_path3 = new_path2 + '\\' + file
                                if os.path.isfile(new_path3):
                                    print(Fore.RED +"             -", file)
                                else:
                                    print(Fore.GREEN + "             -", file)

                                    level5 = os.listdir(new_path3)

                                    for file in level5:
                                        new_path4 = new_path3 + '\\' + file
                                        if os.path.isfile(new_path4):
                                            print(Fore.RED +"                -", file)
                                        else:
                                            print(Fore.GREEN + "                 -", file)
    stopper = '-----------------------------------'
    return stopper                                

result = structure(path)
print(result)

