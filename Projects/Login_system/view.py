import controller
from time import sleep

while True:
    Menu = "\n"*10 +"|Login System|"+"\n"*2 + "1- Login\n2- Register\n3- Exit\nOption: "
    command = input(Menu).split(" ")
    if command[0] == "1":
        print("1")
        break
    if command[0] == "2":
        print("2")
        break
    if command[0] == "3":
        print("\n"*10+" Goodbye!"+"\n"*5)
        break
    else:
        print("\n"*10+ "1,2 and 3 are the only options available. Try again.")
        sleep(1)

def make_login():
    pass

def make_register():
    pass