import controller
from time import sleep
    
def main():
    name, password = "", ""
    Menu = "\n"*10 +"|Login System|"+"\n"*2 + "1- Login\n2- Sign up\n3- Exit\nOption: "
    command = input(Menu).split(" ")
    while True:
        if command[0] == "1":
            make_login(name, password)
            break
        if command[0] == "2":
            print("2")
            break
        if command[0] == "3":
            print("\n"*10 +" Goodbye!"+"\n"*5)
            break
        else:
            print("\n"*10 + "1,2 and 3 are the only options available. Try again.")
            sleep(1)

def make_login(name, password):
    name = input("\n"*5 + "Name: ")
    password = input("Password: ")
    result = controller.verify_login(name, password)
    if result == True:
        print("\n"*10+"Success!"+"\n"*3)
    else:
        print("\nUnsuccess!")





def make_register():
    pass