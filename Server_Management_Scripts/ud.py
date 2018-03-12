#!/usr/local/bin/python3.6
import sqlite3
conn = sqlite3.connect('users.db')
from passlib.hash import pbkdf2_sha256
c = conn.cursor() # create a cursor to iterate through database

#Create table. Yes it's this easy with sqlite3.
c.execute('''CREATE TABLE users
                (username text, password_hash text)''')
username='benuser'
password='password'
hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)



# Insert a row of data
print(username)
#c.execute("INSERT INTO users VALUES ($username,$hash)")
c.execute("INSERT INTO users (username, password_hash) values (?, ?)",
            (username, hash))

username='alyssauser'
password='password'
hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
print(username)
c.execute("INSERT INTO users (username, password_hash) values (?, ?)",
            (username, hash))



username='gilluser'
password='password'
hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
print(username)
c.execute("INSERT INTO users (username, password_hash) values (?, ?)",
            (username, hash))

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


conn = sqlite3.connect('users.db')
c = conn.cursor()

# Do this instead
t = ('benuser',)
c.execute('SELECT * FROM users WHERE username=?', t)
hash=c.fetchone()[1]
print(hash)



#row = c.fetchone()
#assert type(row[0]) is str
