import sqlite3

conn = sqlite3.connect("/Users/ricar/OneDrive/Desktop/Projects/Other_Projects/Login_system/users.db")
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, password TEXT)')
#cur.execute("INSERT INTO users (name, password) VALUES (?, ?)", ('Admin', 'admin123'))
conn.commit()

def verify_login(name, password):
    
    conn = sqlite3.connect("/Users/ricar/OneDrive/Desktop/Projects/Other_Projects/Login_system/users.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, password) VALUES (?, ?)", ('john', '123'))
    cur.execute("SELECT * FROM users WHERE name =? AND password=?", (str(name), str(password)))
    if cur.fetchone():
        return True
    else:
        return False

#for i in cur.execute("""SELECT * FROM users"""):
    #print(i)
