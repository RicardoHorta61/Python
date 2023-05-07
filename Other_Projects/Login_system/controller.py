import sqlite3

conn = sqlite3.connect("/Users/ricar/OneDrive/Desktop/Projects/Other_Projects/Login_system/databases/users.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, password TEXT)")
#cur.execute("INSERT INTO users (name, password) VALUES (?, ?)", ('Admin', 'admin123'))
conn.commit()

def verify_user(name, password):
    conn = sqlite3.connect("/Users/ricar/OneDrive/Desktop/Projects/Other_Projects/Login_system/databases/users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name =? AND password=?", (str(name), str(password)))
    if cur.fetchone():
        return True
    else:
        return False

def create_user(name, password):
    conn = sqlite3.connect("/Users/ricar/OneDrive/Desktop/Projects/Other_Projects/Login_system/databases/users.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, password))
    conn.commit()

def create_users_list():
    lista = []    
    for i in cur.execute("""SELECT name FROM users"""):
        i= "".join(i)
        lista.append(i)
        
    return lista
