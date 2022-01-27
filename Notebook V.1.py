import time
def startup_print():
    print("(1) Read Notes\n(2) Add Note\n(3) Delete All Notes\n(4) Delete Previous Note\n(5) Quit\n")
def ERROR02():
    print("Error02. INPUT NOT A NUMBER")
def read_file():
    readfile = open('notebook.txt','r')
    content = readfile.read()
    print(content)
    readfile.close()
def new_note():
    myfile = open('notebook.txt','a')
    addedtext = userinput02
    myfile.write(addedtext)
    myfile.write(' ')
    myfile.write(time.strftime("%X %x"))
    myfile.write('\n')
    myfile.close()
def clear_notes():
    myfile = open('notebook.txt','r+')
    myfile.truncate(0)
    myfile.close()
def delete_previous_note():
    with open("notebook.txt",'r') as f:
        lines = f.readlines()
        lines.remove(userinput02)
        with open('notebook.txt','w') as f:
            for line in lines:
                f.write(null)
def ERROR01():
    print("ERROR01. INPUT MUST BE A NUMBER IN RANGE (1-4)")
print("NOTEBOOK")
myfile = open("notebook.txt","w")
while True:
    startup_print()
    
    try:
        userinput01 = int(input('please select one: '))
    except ValueError:
        ERROR02()
    input01 = userinput01
    if input01 in range(0,6):
        if input01 == 1:
            read_file()
        elif input01 == 2:
            userinput02 = input("type new note: ")
            new_note()
        elif input01 == 3:
            clear_notes()
        elif input01 == 4:
            delete_previous_note()
        elif input01 == 5:
            myfile.close()
            break
    elif input01 != range(0,6):
        ERROR01()
print('Notebook shutting down!')
input('press ENTER to exit')
#code = userinput02:
        #delete code
#4 break myfile.close()
#2 input 2 = input
#
