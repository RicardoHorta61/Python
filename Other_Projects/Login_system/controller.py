import sqlite3

conn = sqlite3.connect("/Users/ricar/OneDrive/Desktop/Projects/Other_Projects/Login_system/databases/users.db")
cur = conn.cursor()


cur.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, password TEXT)")
#cur.execute("INSERT INTO users (name, password) VALUES (?, ?)", ('Admin', 'admin123'))
conn.commit()

def connect():
    conn = sqlite3.connect("/Users/ricar/OneDrive/Desktop/Projects/Other_Projects/Login_system/databases/users.db")
    cur = conn.cursor()  

#-------------------------------------------------------------------------------------------------------------------#  
def verify_name_pass_user(name, password):
    # This fuction is responsible for verify the name and the password of a user. Used to make logins
    connect()
    cur.execute("SELECT * FROM users WHERE name =? AND password=?", (str(name), str(password)))  
    if cur.fetchone():
        return True
    else:
        return False
#-------------------------------------------------------------------------------------------------------------------#  

#-------------------------------------------------------------------------------------------------------------------#  
def verify_signup_user(name):
    # Responsible for verify the existence of a username. Used to make Sign Up and eliminate a user.
    connect()
    cur.execute("SELECT * FROM users WHERE name = ? ", (str(name)))
    if cur.fetchone():
        return True
    else:  
        return False
#-------------------------------------------------------------------------------------------------------------------#  

#-------------------------------------------------------------------------------------------------------------------#  
def create_user(name, password):
    # Creates a new user.
    connect()
    cur.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, password))
    conn.commit()
#-------------------------------------------------------------------------------------------------------------------#  

#-------------------------------------------------------------------------------------------------------------------#  
def eliminate_user(name):
    
    pass
#-------------------------------------------------------------------------------------------------------------------#  

#-------------------------------------------------------------------------------------------------------------------#  
def create_users_list():
    # Creates a list with all usernames.
    lista = []    
    for i in cur.execute("""SELECT name FROM users"""):
        i= "".join(i)
        lista.append(i)  
    return lista
#-------------------------------------------------------------------------------------------------------------------#  
