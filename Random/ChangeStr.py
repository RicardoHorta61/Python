def change_str(str):
    new_str = str.split()
    new_str = new_str[::-1]
    new_str= " ".join(new_str)
    print(new_str)    

change_str("My name is Ricardo")
change_str("Dog and Cat")