import  os
import time
from sys import platform

"""
Python File Manager
Author- Lucifer
Project- Open source
Date- 09/08/2020
"""
def directory_details():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')
    print("""
        Python File manager  ~by lucifer

        *** Instructions ***
        1. Type full File name to read file contents
        2. Type full Directory name to go to directory
        3. Type .. to go to Parent directory
        4. Type False to exit File Manager.

        Fetching Files and Directories...
        """)
    time.sleep(1)
    dir = os.listdir()
    cwd = os.getcwd()
    print(f"\nCurrent Working Directory:--> {cwd}\n")
    directories=cwd.replace('\\','/').split('/')
    wd=directories[len(directories)-1]
    dirlist=[]
    filelist=[]
    # print(dir)
    # print()
    print(f"Directory Name ---> *** {wd.upper()} ***\n")
    for items in dir:
        if os.path.isfile(items):
            filelist.append(items)
        elif os.path.isdir(items):
            dirlist.append(items)
    if len(filelist)!=0:
        print("*** Files ***")
        for items in filelist:
            print(items)
    else:
        print("\n*** No Files found ***")
    if len(dirlist)!=0:
        print('\n*** Directories ***')
        for items in dirlist:
            print(items)
    else:
        print("\n*** No Directory found ***")

if __name__ == '__main__':

    directory_details()
    a=True
    while a:
        b = input('\n\nEnter filename or directory name to open: ')
        if b in os.listdir():
            if os.path.isfile(b):
                try:
                    f=open(b,"r")
                    print(f"\n*** Starting of {b} ***\n\n{f.read()}\n\n*** Ending of {b} ***\n\n")
                except:
                    print(f"\n\n*** {b} could not be read!\nMay it {b} is not a text file\n\n")
                time.sleep(5)
                directory_details()
            elif os.path.isdir(b):
                cwd=os.getcwd().replace('\\','/')
                wd=cwd+'/'+b
                os.chdir(wd)
                directory_details()
        elif b=='..':
            os.chdir('..')
            directory_details()

        elif b=='False':
            a=False

        else:

            print(f'\n\n"{b}": *** No such file or directory ***\n!*GO UP and Read Instructions Carefully*!\n\n')
            time.sleep(3)
            directory_details()

