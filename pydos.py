# Fake DOS in python called PYDOS #

# Packages #
import pydoschooseadv.py 

# Welcome Message #
print("Welcome to PYDOS! type 'help' to get list of commands. press 'q' to quit")

# Commands #

cmd = input('C:\> ')

if cmd == 'help'.lower():
    print("help: bring up commands  (cd)games: find games ")
elif cmd == 'q'.lower():
    quit
elif cmd == 'cd games'.lower():
    gcmd = input("C:\Games\> ")

    if gcmd == 'ls'.lower():
        print("'chooseadventure' ")

    gcmd = input("C:\Games\> ")

    if gcmd == 'Chooseadventure'.lower():
            execfile('pydoschooseadv.py')

