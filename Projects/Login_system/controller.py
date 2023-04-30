import sqlite3

con = sqlite3.connect("users_data_base.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users
(name text, password text) """)

cur.execute("""INSERT INTO users VALUES 
("Ricardo", "hello")""")

con.commit

for i in cur.execute("""SELECT * FROM users"""):
    print(i)