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
                1. Type cat <file name> to read file contents
                2. Type cd √[Press Enter] type Directory name or\n\t\t   complete path to go to directory
                3. Type ls to get directory details
                4. Type help for help options
                5. Type rm <directory name> to remove directory
                6. Type mv to move file/directory to new path
                7. Type cp to copy file
                8. Type clear to clear screen
                9. Type Exit to exit File Manager.
                10. Type mkdir <directory name> to make new directory.{Style.RESET_ALL}
                
                """)
def check(file):
    dirlist = []   # List of all directories in Current Working Directory.
    filelist = []  # List of all files in Current Working Directory.
    for items in os.listdir():
        if os.path.isfile(items):
            filelist.append(items)  # List all files in filelist
        elif os.path.isdir(items):
            dirlist.append(items)   # List all files in dirlist
    if file in dirlist:
        del dirlist
        return True  # Return true if Function Argument is a Directory in Current Working Directory.
    elif file in filelist:
        del filelist
        return False   # Return true if Function Argument is a File in Current Working Directory.
def directory_details():

    dir = os.listdir()   # List of Directories and files
    cwd = os.getcwd()  # Current Working Directory.
    print(f"\n{Fore.RED}Current Working Directory:-->{Fore.RESET} {Back.CYAN}{Fore.RED}{cwd}{Style.RESET_ALL}\n")
    directories=cwd.replace('\\','/').split('/')    # Current Working Directory.
    wd=directories[len(directories)-1]  # Working Directory.
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
    del dir
    del cwd
    del wd
    del filelist
    del dirlist

def main():
    clear()
    # intro()
    print(f"\t\t{Fore.CYAN}Fetching Files and Directories...{Style.RESET_ALL}\n")
    time.sleep(1)
    a = True
    while a:

        b = input(f'\n{Back.CYAN}{Fore.RED}Explorer:~[{os.getcwd()}]{Style.RESET_ALL}>>> {Fore.GREEN}')
        if b.startswith('cat '):
            b = b.replace('cat ', '')
            # if b in os.listdir():
            if os.path.isfile(b):
                # clear()
                # intro()
                try:
                    f = open(b, "r")
                    print(
                        f"\n{Style.BRIGHT}{Fore.YELLOW}*** Starting of {b} ***{Fore.RESET}\n\n{f.read()}\n\n{Fore.YELLOW}*** Ending of {b} ***{Fore.RESET}\n\n")
                except:
                    print(
                        f"\n\n{Style.BRIGHT}{Fore.RED}*** {b} could not be read!\nMay \'{b}\' is not a text file{Style.RESET_ALL}\n\n")
                time.sleep(5)
                # clear()
                # intro()
        elif b == "cd":
            path = input('Enter valid path: ').replace('\\', '/')
            if os.path.isdir(path) and check(path):
                cwd = os.getcwd().replace('\\', '/')
                wd = cwd + '/' + path
                os.chdir(wd)
            elif path == '..':
                os.chdir('..')
            else:
                try:
                    os.chdir(path)
                except:
                    print(f"\'{path}\': is invalid")
        elif b == "":
            print("\033[A\033[A")
            continue
            # clear()
        elif b == 'ls':
            directory_details()
        elif b == 'pwd' or b == 'cwd':
            cwd = os.getcwd()
            print(
                f"\n{Fore.RED}Current Working Directory:-->{Fore.RESET} {Back.CYAN}{Fore.RED}{cwd}{Style.RESET_ALL}\n")

        elif b == 'Exit' or b == 'exit' or b == 'EXIT':
            clear()
            # intro()
            print(Style.BRIGHT, Fore.RED, '    ~lucifer', Style.RESET_ALL)
            a = False
        elif b == 'cp':
            file = input('Enter file name to be copied: ')
            if file in os.listdir() and check(file) == False:
                if len(file.split(' ')) > 1:
                    file = '"' + file + '"'
                adr = input('Enter destination path: ')
                ad = adr
                adr = adr.replace('\\', '/')
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
                        mv = 'mv ' + file + ' ' + ad
                        print(mv)
                        os.system(mv)
                    elif platform == "win32":
                        # os.system('cls')
                        mv = 'move ' + file + ' ' + ad
                        print(mv)
                        os.system(mv)
                except:
                    print(f"wrong path --> {adr}")
            else:
                print(f'\n\n{Style.BRIGHT}{Fore.RED}"{file}": *** No such file or directory ***{Style.RESET_ALL}\n\n')

        elif b.startswith('mkdir '):
            b = b.replace('mkdir ', '')
            print('\nThis feature (making new Directory) is not yet added\n')
        elif b.startswith('rm '):
            b = b.replace('rm ', '')

            if b in os.listdir() and check(b):
                if platform == "win32":
                    os.rmdir(b)
                    print(f"dir(\"{b}\") removed successfully")
                elif platform == "linux" or platform == "linux2":
                    try:
                        os.rmdir(b)
                        print(f"dir(\"{b}\") removed successfully")
                    except:
                        if ' ' in b:
                            b = '"' + b + '"'
                        os.system(f'rm -rf {b}')
                        print(f"dir(\"{b}\") removed successfully")

            elif b in os.listdir() and check(b) == False:
                if ' ' in b:
                    b = '"' + b + '"'
                if platform == "win32":
                    os.system(f'del /f {b}')
                    print(f"file(\"{b}\") removed successfully")

                elif platform == "linux" or platform == "linux2":
                    os.system(f'rm {b}')
                    print(f"file(\"{b}\") removed successfully")
            else:
                print(f'\n\n{Style.BRIGHT}{Fore.RED}"{b}": *** No such file or directory ***{Style.RESET_ALL}\n\n')

        elif b == 'clear':
            clear()
            # intro()
        elif b == 'help' or b == '?':
            print("Help :")
            intro()

        else:
            print(
                f'\n\n{Style.BRIGHT}{Fore.RED}"{b}": *** is not recognized as an internal command ***\n*** Type \"help\" to read instructions ***{Style.RESET_ALL}\n\n')

if __name__ == '__main__':
    main()

