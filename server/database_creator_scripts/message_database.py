#!/usr/local/bin/python3.6
import sqlite3, datetime, time
message_conn = sqlite3.connect('messages.db')
message_c = message_conn.cursor() # create a cursor to iterate through database

#Create table. Yes it's this easy with sqlite3.
message_c.execute('''CREATE TABLE messages
                (date text, message text, sender text, reciever text)''')



ts = time.time()
date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
message='s'
sender='alyssauser'
reciever='benuser'

#message_c.execute("INSERT INTO messages VALUES ($username,$hash)")
message_c.execute("INSERT INTO messages (date, message, sender, reciever) values (?, ?, ?, ?)",
            (date, message, sender, reciever))
time.sleep(1)
ts = time.time()
date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
message='s1'
sender='alyssauser'
reciever='gilluser'

#message_c.execute("INSERT INTO messages VALUES ($username,$hash)")
message_c.execute("INSERT INTO messages (date, message, sender, reciever) values (?, ?, ?, ?)",
            (date, message, sender, reciever))
time.sleep(1)
ts = time.time()
date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
message='s2'
sender='benuser'
reciever='alyssauser'

#message_c.execute("INSERT INTO messages VALUES ($username,$hash)")
message_c.execute("INSERT INTO messages (date, message, sender, reciever) values (?, ?, ?, ?)",
            (date, message, sender, reciever))
time.sleep(1)
ts = time.time()
date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
message='s3'
sender='gilluser'
reciever='benuser'

#message_c.execute("INSERT INTO messages VALUES ($username,$hash)")
message_c.execute("INSERT INTO messages (date, message, sender, reciever) values (?, ?, ?, ?)",
            (date, message, sender, reciever))
time.sleep(1)


# Save (commit) the changes
message_conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
message_conn.close()


message_conn = sqlite3.connect('messages.db')
message_c = message_conn.cursor()

# Do this instead
t = ('alyssauser',)
message_c.execute('SELECT * FROM messages WHERE sender=?', t) #sender | reciever
#hash=message_c.fetchone()[1]
print(message_c.fetchall())
#print(hash)



#row = message_c.fetchone()
#assert type(row[0]) is str
