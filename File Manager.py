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
def intro():
    print(f"""{Style.RESET_ALL}
                {Fore.RED}{Style.BRIGHT}Python File Manager(CLI) ~by lucifer

                {Fore.GREEN}*** Instructions ***
                1. Type full File name to read file contents
                2. Type full Directory name to go to directory
                3. Type .. to go to Parent directory
                4. Type ls to get directory details
                5. Type help for help options
                6. Type rm <directory name> to remove directory
                7. Type mv to move file/directory to new path
                8. Type cp to copy file
                9. Type clear to clear screen
                10. Type Exit to exit File Manager.
                

                {Fore.CYAN}Fetching Files and Directories...{Style.RESET_ALL}
                """)
def check(file):
    dirlist = []
    filelist = []
    for items in os.listdir():
        if os.path.isfile(items):
            filelist.append(items)
        elif os.path.isdir(items):
            dirlist.append(items)
    if file in dirlist:
        return True
    else:
        return False
def directory_details():

    dir = os.listdir()
    cwd = os.getcwd()
    print(f"\n{Fore.RED}Current Working Directory:-->{Fore.RESET} {Back.CYAN}{Fore.RED}{cwd}{Style.RESET_ALL}\n")
    directories=cwd.replace('\\','/').split('/')
    wd=directories[len(directories)-1]
    # global dirlist
    # global filelist
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
    # intro()
    time.sleep(1)
    a=True
    while a:

        b = input(f'\n{Back.CYAN}{Fore.RED}Explorer:~[{os.getcwd()}]{Style.RESET_ALL}>>> {Fore.GREEN}')
        if b in os.listdir():
            if os.path.isfile(b):
                # clear()
                # intro()
                try:
                    f=open(b,"r")
                    print(f"\n{Style.BRIGHT}{Fore.YELLOW}*** Starting of {b} ***{Fore.RESET}\n\n{f.read()}\n\n{Fore.YELLOW}*** Ending of {b} ***{Fore.RESET}\n\n")
                except:
                    print(f"\n\n{Style.BRIGHT}{Fore.RED}*** {b} could not be read!\nMay it {b} is not a text file{Fore.RESET}\n\n")
                time.sleep(5)
            elif os.path.isdir(b):
                cwd=os.getcwd().replace('\\','/')
                wd=cwd+'/'+b
                os.chdir(wd)
                # clear()
                # intro()
        elif b == "":
            continue
        elif b == '..':
            os.chdir('..')
            # clear()
        elif b=='ls':
            directory_details()
        elif b=='pwd':
            cwd = os.getcwd()
            print(f"\n{Fore.RED}Current Working Directory:-->{Fore.RESET} {Back.CYAN}{Fore.RED}{cwd}{Style.RESET_ALL}\n")

        elif b=='Exit' or b=='exit':
            clear()
            # intro()
            print(Style.BRIGHT,Fore.RED,'    ~lucifer',Style.RESET_ALL)
            a = False
        elif b == 'cp':
            file = input('Enter file/directory to be copied: ')
            if file in os.listdir() and check(file)== False:
                if len(file.split(' ')) > 1:
                    file = '"' + file + '"'
                adr = input('Enter destination path: ')
                ad = adr
                adr = adr.replace('\\','/')
                try:
                    if platform == "linux" or platform == "linux2":
                        # os.system('clear')
                        cp = 'cp -r ' + file + ' ' + ad
                        os.system(cp)
                    elif platform == "win32":
                        # os.system('cls')
                        cp = 'copy ' + file + ' ' + ad
                        print(cp)
                        os.system(cp)

                except:
                    print(f"wrong path --> {adr}")
                    cwd = os.getcwd().replace('\\', '/')
                    os.chdir(cwd)
            else:
                print(f'\n\n{Style.BRIGHT}{Fore.RED}"{file}": *** No such file to copy ***{Style.RESET_ALL}\n\n')

        elif b == 'mv':
            file = input('Enter file/directory to be moved: ')
            if file in os.listdir():
                if len(file.split(' ')) > 1:
                    file = '"' + file + '"'
                adr = input('Enter destination path: ')
                ad = adr
                adr = adr.replace('\\', '/')
                try:
                    if platform == "linux" or platform == "linux2":
                        # os.system('clear')
                        cp = 'mv ' + file + ' ' + ad
                        os.system(cp)
                    elif platform == "win32":
                        # os.system('cls')
                        cp = 'move ' + file + ' ' + ad
                        print(cp)
                        os.system(cp)
                except:
                    print(f"wrong path --> {adr}")
                    cwd = os.getcwd().replace('\\', '/')
                    os.chdir(cwd)
            else:
                print(f'\n\n{Style.BRIGHT}{Fore.RED}"{file}": *** No such file or directory ***{Style.RESET_ALL}\n\n')

        elif b.startswith('rm '):
            s=b.split(' ')
            if len(s)>2:
                for i in range(2,len(s)):
                    s[1]=s[1]+' '+s[i]
                if s[1] in os.listdir() and check(s[1]):
                    try:
                        os.rmdir(s[1])
                        print(f"dir(\"{s[1]}\") removed successfully")
                    except:
                        print(f'cannot remove!\n{s[1]}: not a directory')
            elif s[1] in os.listdir():
                try:
                    os.rmdir(s[1])
                    print(f"dir(\"{s[1]}\") removed successfully")
                except:
                    print(f'cannot remove!\n{s[1]}: not a directory')
            else:
                print(f'\n\n{Style.BRIGHT}{Fore.RED}"{s[1]}": *** No such directory ***{Style.RESET_ALL}\n\n')

        elif b == 'clear':
            clear()
            # intro()
        elif b == 'help' or b == '?':
            print("Help :")
            intro()

        else:
            print(f'\n\n{Style.BRIGHT}{Fore.RED}"{b}": *** No such file or directory ***\n\"{b}\" *is not recognized as internal command*\n!*GO UP and Read Instructions Carefully*!{Style.RESET_ALL}\n\n')


