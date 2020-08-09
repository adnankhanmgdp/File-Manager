import os
import time
from sys import platform
from colorama import Fore, Back, Style
"""
Python File Manager
Author- Lucifer
Project- Open source
Date- 09/08/2020
"""
def clear():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')
def directory_details():

    print(f"""{Style.RESET_ALL}
        {Fore.RED}{Style.BRIGHT}Python File manager  ~by lucifer

        {Fore.GREEN}*** Instructions ***
        1. Type full File name to read file contents
        2. Type full Directory name to go to directory
        3. Type .. to go to Parent directory
        4. Type Exit to exit File Manager.

        {Fore.CYAN}Fetching Files and Directories...{Style.RESET_ALL}
        """)
    time.sleep(1)
    dir = os.listdir()
    cwd = os.getcwd()
    print(f"\n{Fore.RED}Current Working Directory:-->{Fore.RESET} {Back.CYAN}{Fore.RED}{cwd}{Style.RESET_ALL}\n")
    directories=cwd.replace('\\','/').split('/')
    wd=directories[len(directories)-1]
    dirlist=[]
    filelist=[]
    # print(dir)
    # print()
    print(f"{Fore.RED}Directory Name ---> {Back.CYAN}{Fore.RED}*** {wd.upper()} ***{Style.RESET_ALL}\n")
    for items in dir:
        if os.path.isfile(items):
            filelist.append(items)
        elif os.path.isdir(items):
            dirlist.append(items)
    if len(filelist)!=0:
        print(f"{Style.BRIGHT}{Fore.YELLOW}*** Files ***{Style.RESET_ALL}")
        for items in filelist:
            print(Fore.GREEN,items,Fore.RESET)
    else:
        print(f"\n{Style.BRIGHT}{Fore.YELLOW}*** No Files found ***{Style.RESET_ALL}")
    if len(dirlist)!=0:
        print(f'\n{Style.BRIGHT}{Fore.YELLOW}*** Directories ***{Style.RESET_ALL}')
        for items in dirlist:
            print(Fore.BLUE,items,Fore.RESET)
    else:
        print(f"\n{Style.BRIGHT}{Fore.YELLOW}*** No Directory found ***{Style.RESET_ALL}")

if __name__ == '__main__':
    clear()
    directory_details()
    a=True
    while a:
        b = input(f'\n\n{Back.CYAN}{Fore.RED}Enter filename or directory name to open:{Style.RESET_ALL} {Style.BRIGHT}{Fore.GREEN}')
        if b in os.listdir():
            if os.path.isfile(b):
                clear()
                try:
                    f=open(b,"r")
                    print(f"\n{Style.BRIGHT}{Fore.YELLOW}*** Starting of {b} ***{Fore.RESET}\n\n{f.read()}\n\n{Fore.YELLOW}*** Ending of {b} ***{Fore.RESET}\n\n")
                except:
                    print(f"\n\n{Style.BRIGHT}{Fore.RED}*** {b} could not be read!\nMay it {b} is not a text file{Fore.RESET}\n\n")
                time.sleep(5)
                directory_details()
            elif os.path.isdir(b):
                cwd=os.getcwd().replace('\\','/')
                wd=cwd+'/'+b
                os.chdir(wd)
                clear()
                directory_details()
        elif b=='..':
            os.chdir('..')
            clear()
            directory_details()

        elif b=='Exit' or b=='exit':
            clear()
            print(Style.BRIGHT,Fore.RED,'    ~lucifer',Style.RESET_ALL)
            a=False

        else:
            clear()
            print(f'\n\n{Style.BRIGHT}{Fore.RED}"{b}": *** No such file or directory ***\n!*GO UP and Read Instructions Carefully*!{Style.RESET_ALL}\n\n')
            time.sleep(2)
            directory_details()
