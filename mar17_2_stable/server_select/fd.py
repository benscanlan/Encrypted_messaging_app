#!/usr/local/bin/python3.6
import sqlite3, datetime, time
file_conn = sqlite3.connect('files.db')
file_c = file_conn.cursor() # create a cursor to iterate through database

#Create table. Yes it's this easy with sqlite3.
file_c.execute('''CREATE TABLE files
                (date text, file text, sender text, reciever text)''')



ts = time.time()
date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
file='s'
sender='alyssauser'
reciever='benuser'

#file_c.execute("INSERT INTO files VALUES ($username,$hash)")
file_c.execute("INSERT INTO files (date, file, sender, reciever) values (?, ?, ?, ?)",
            (date, file, sender, reciever))
time.sleep(1)
ts = time.time()
date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
file='s1'
sender='alyssauser'
reciever='gilluser'

#file_c.execute("INSERT INTO files VALUES ($username,$hash)")
file_c.execute("INSERT INTO files (date, file, sender, reciever) values (?, ?, ?, ?)",
            (date, file, sender, reciever))
time.sleep(1)
ts = time.time()
date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
file='s2'
sender='benuser'
reciever='alyssauser'

#file_c.execute("INSERT INTO files VALUES ($username,$hash)")
file_c.execute("INSERT INTO files (date, file, sender, reciever) values (?, ?, ?, ?)",
            (date, file, sender, reciever))
time.sleep(1)
ts = time.time()
date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
file='s3'
sender='gilluser'
reciever='benuser'

#file_c.execute("INSERT INTO files VALUES ($username,$hash)")
file_c.execute("INSERT INTO files (date, file, sender, reciever) values (?, ?, ?, ?)",
            (date, file, sender, reciever))
time.sleep(1)


# Save (commit) the changes
file_conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
file_conn.close()


file_conn = sqlite3.connect('files.db')
file_c = file_conn.cursor()

# Do this instead
t = ('alyssauser',)
file_c.execute('SELECT * FROM files WHERE sender=?', t) #sender | reciever
#hash=file_c.fetchone()[1]
print(file_c.fetchall())
#print(hash)



#row = file_c.fetchone()
#assert type(row[0]) is str
