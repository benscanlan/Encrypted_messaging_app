#!/usr/local/bin/python3.6
import sqlite3
from passlib.hash import pbkdf2_sha256
conn = sqlite3.connect('users.db')
c = conn.cursor() # create a cursor to iterate through database

#Create table. Yes it's this easy with sqlite3.
c.execute('''CREATE TABLE users
                (username text, password_hash text)''')
username='Ben_Scanlan'
password='password'
hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)



# Insert a row of data
print(username)
#c.execute("INSERT INTO users VALUES ($username,$hash)")
c.execute("INSERT INTO users (username, password_hash) values (?, ?)",
            (username, hash))

username='David_Ziechick'
password='password'
hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
print(username)
c.execute("INSERT INTO users (username, password_hash) values (?, ?)",
            (username, hash))


username='Kevin_Buffardi'
password='password'
hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
print(username)
c.execute("INSERT INTO users (username, password_hash) values (?, ?)",
            (username, hash))

username='Alyssa_Wong'
password='password'
hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
print(username)
c.execute("INSERT INTO users (username, password_hash) values (?, ?)",
            (username, hash))

username='Russell_Walawitz'
password='password'
hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
print(username)
c.execute("INSERT INTO users (username, password_hash) values (?, ?)",
            (username, hash))


username='Jennifer_Decker'
password='password'
hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
print(username)
c.execute("INSERT INTO users (username, password_hash) values (?, ?)",
            (username, hash))


username='Sterling_Baldwin'
password='password'
hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
print(username)
c.execute("INSERT INTO users (username, password_hash) values (?, ?)",
            (username, hash))


username='John_Bester'
password='password'
hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
print(username)
c.execute("INSERT INTO users (username, password_hash) values (?, ?)",
            (username, hash))

username='Jeff_Grave'
password='password'
hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
print(username)
c.execute("INSERT INTO users (username, password_hash) values (?, ?)",
            (username, hash))

username='Jose_Grave'
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
t = ('Ben_Scanlan',)
c.execute('SELECT * FROM users WHERE username=?', t)
hash=c.fetchone()[1]
print(hash)



#row = c.fetchone()
#assert type(row[0]) is str
