# -*- coding: cp1252 -*-
import time
usernotebook = 'notebook.txt'
extra = False
loop = True
debug = False
defaultnotebook = False
list01 = []

def startup_print():
        if extra == True:
                print("\nThe time now is",time.strftime("%X %x"),'\n')
                print('Extra Settings Enabled\n')
        print('now using file',usernotebook)
        print('(1) Read the Notebook\n(2) Add Note\n(3) Delete Note [Coming Soon!]\n(4) Empty Notebook')
        print('(5) Change The Notebook\n(6) Extra\n(7) DEBUG\n(8) Quit\n')
def Error01():
        print('ERROR01. INPUT NOT A NUMBER')
def read_file():
        readfile = open(usernotebook,'r')
        content = readfile.read()
        print(content)
        readfile.close()
def new_note():
        myfile = open(usernotebook,'a')
        addedtext = userinput02
        myfile.write(addedtext)
        if extra == True:
                myfile.write(' ')
        elif extra == False:
                myfile.write(':::')
        myfile.write(time.strftime("%X x%"))
        myfile.write('\n')
        myfile.close()
        try:
                list01.append(userinput02)
        except (ValueError, TypeError):
                print("ERROR02")
def search(x):
        try:
                result = list01.index(x)
                return result
        except (ValueError):
                if debug == True:
                        print("Error in Search module")
def clearnotes():
        try:
                myfile = open(usernotebook,'r+')
                myfile.truncate(0)
                myfile.close()
        except (ValueError,TypeError):
                if debug == True:
                        print("Error in clearnotes module")
def ERROR01():
        if debug == False:
                print('invalid input')
if extra == True:
        print('NOTEBOOK')
if defaultnotebook == False:
        try:
                readfile = open('notebook.txt','r')
                readfile.close()
                try:
                        myfile = open('notebook.txt','a')
                        usernotebook = 'notebook.txt'
                except (ValueError):
                        pass
        except (FileNotFoundError):
                myfile = open('notebook.txt','a')
                print('no default notebook was found. New notebook created')
                usernotebook = 'notebook.txt'
                if extra == True:
                        print('new notebook was given name:',usernotebook)
if defaultnotebook == True:
        try:
                readfile = open(usernotebook,'r')
                readfile.close()
                try:
                        myfile = open(usernotebook,'a')
                        defaultnotebook = True
                except (ValueError):
                        pass
        except(FileNotFoundError):
                myfile = open('notebook.txt','a')
                print('no default notebook was found. New notebook created')
                defaultnotebook = False
                usernotebook = 'notebook.txt'
                if extra == True:
                        ('default notebook missing')
                if debug == True:
                        print('default notebook missing,\n(defaultnotebook=true) when no default notebook is present. defaultnotebook set to false.\n\n')
while loop == True:
        loop_1 = True
        loop_2 = False
        while loop_1 == True:
                startup_print()
                try:
                        z = int(input('Please select one: '))
                        if z == 1:
                                read_file()
                        elif z == 2:
                                userinput02 = input("write a new note: ")
                                new_note()
                        elif z == 4:
                                clear_notes()
                        elif z == 5:
                                loop_1 = False
                                try:
                                        userinput03 = input('give the name of the new file: ')
                                        try:
                                                readfile = open(userinput03,'r')
                                                readfile = close()
                                        except (FileNotFoundError):
                                                try:
                                                        myfile = open(userinput03,'a')
                                                        print('no name with that input detected, created one')
                                                except (ValueError):
                                                        pass
                                        defaultnotebook = True
                                        usernotebook = userinput03
                                except (ValueError):
                                        pass
                        elif z== 3:
                                if debug == True or extra == True:
                                        print('\n\nUnsupported as of yet\n\n')
                                if debug == False and extra == False:
                                        pass
                        elif z == 6:
                                if extra == False:
                                        extra = True
                                        print('\n\nExtra settings now enabled\n\n')
                                elif extra == True:
                                        extra = False
                                        print('\n\nExtra settings now disabled\n\n')
                        elif z == 7:
                                if debug == False:
                                        debug = True
                                        print('\n\nDEBUG MODE NOW ENABLED\n\n')
                                elif debug == True:
                                        debug = False
                                        print('\n\nDEBUG MODE NOW DISABLED\n\n')
                        elif z == 8:
                                loop = False
                                loop_01 = False
                                if debug == True:
                                        print('\n\nTest Successful?\n\n')
                                        loop = False
                                        loop01 = False
                                        break
                        elif z != 1 or z != 2 or z != 3 or z != 4 or z != 5 or z != 6 or z != 7 or z != 8:
                                if debug == True:
                                        print('\n\nERROR INPUT NOT A DIGIT IN RANGE 1-8\n\n')
                                elif extra == True:
                                        print('invalid input')
                                else:
                                        pass
                except Exception as a:
                        if extra == True:
                                print(a)
                        elif debug == True:
                                print(a)
                        else:
                                pass
else:
        if extra == True:
                print('\n\nnotebook shutting down, thank you.\n\n')
                input('press ENTER to exit')
        if extra == False:
                print('notebook shutting down, thank you.')
