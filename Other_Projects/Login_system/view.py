import controller as con
from time import sleep
    
def main():
    name, password = "", ""
    Menu = "\n"*10 +"|Login System|"+"\n"*2 + "1- Login\n2- Sign up\n3- Exit\n4- Users\n5- Admin\n Option: "
    command = input(Menu).split(" ")
    while True:
        if command[0] == "1":
            make_login(name, password)
            return_menu()
            break
        if command[0] == "2":
            make_signup(name, password)
            return_menu()
            break
        if command[0] == "3":
            print("\n"*10 +" Goodbye!"+"\n"*5)
            break
        if command[0] == "4":
            print(con.create_users_list())
            return_menu()
            break
        if command[0] == "5":
            pass
        else:
            print("\n"*10 + "1,2,3,4 and 5 are the only options available. Try again.")
            sleep(1)

def make_login(name, password):
    name = input("\n"*5 + "Name: ")
    password = input("Password: ")
    result = con.verify_name_pass_user(name, password)
    if result == True:
        print("\n"*10+"Success!"+"\n"*3)
    else:
        print("\nUnsuccess!")

def make_signup(name, password):
    while True:
        name = input("\n"*5 + "Name: ")
        password = input("Password: ")
        result = con.verify_signup_user(name)
        if result == True:
            print("User already exists.")
            sleep(1)
        else:
            con.create_user(name, password)
            print("New user created with success!")
            break

def return_menu():
    print("\n1- Return to Menu\n2- Exit")
    command = input("Option: ")
    if command == "1":
        main()
    if command == "2":
        return print("\n"*10 +" Goodbye!"+"\n"*5)
    else:
        print("\n"*10 + "1,2,3 and 4 are the only options available. Try again.")
        return_menu()
