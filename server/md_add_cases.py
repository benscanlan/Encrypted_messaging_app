#!/usr/local/bin/python3.6
import sqlite3, datetime, time
message_conn = sqlite3.connect('messages.db')
message_c = message_conn.cursor() # create a cursor to iterate through database

ts = time.time()
date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
message='mess1'
sender='alyssauser'
reciever='benuser'

#message_c.execute("INSERT INTO messages VALUES ($username,$hash)")
message_c.execute("INSERT INTO messages (date, message, sender, reciever) values (?, ?, ?, ?)",
            (date, message, sender, reciever))
time.sleep(1)

ts = time.time()
date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
message='mess2'
sender='benuser'
reciever='alyssauser'
#message_c.execute("INSERT INTO messages VALUES ($username,$hash)")
message_c.execute("INSERT INTO messages (date, message, sender, reciever) values (?, ?, ?, ?)",
                  (date, message, sender, reciever))

# Save (commit) the changes
message_conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
message_conn.close()
