import sqlite3

con = sqlite3.connect("/Users/ricar/OneDrive/Desktop/Projects/Other_Projects/Login_system/users.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users
(name NOT NULL, password NOT NULL) """)

cur.execute("""INSERT INTO users VALUES 
("John", "magicpassword")""")

def verify_login(name, password):
    cur.execute("""SELECT * FROM users WHERE name = ? AND password = ?""",(name, password))
    if cur.fetchall():
        return True
    else:
        return False 


con.commit

for i in cur.execute("""SELECT * FROM users"""):
    print(i)