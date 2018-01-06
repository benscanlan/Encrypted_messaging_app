#!/usr/local/bin/python3.6
import sqlite3, datetime, time, random
username='benuser'

#get all previous
def getallmessages():
    print(username)
    message_conn = sqlite3.connect('messages.db')
    message_c = message_conn.cursor()
    t =(username,username)
    message_c.execute("SELECT * FROM messages WHERE reciever = ? OR sender = ?", t)
    #date_accessed = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print(message_c.fetchall())

#not needed not that we are using sql as a 4gl
#i = 0
#for result in message_c.execute("SELECT * FROM messages WHERE reciever = ? OR sender = ?", t):
#    i = i + 1
#i = i
#print(i)


#add solo message
def addsolomessage():
    message_conn = sqlite3.connect('messages.db')
    message_c = message_conn.cursor() # create a cursor to iterate through database
    ts = time.time()
    date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    message=random.randint(1, 100000)
    sender='alyssauser'
    reciever='benuser'
    #message_c.execute("INSERT INTO messages VALUES ($username,$hash)")
    message_c.execute("INSERT INTO messages (date, message, sender, reciever) values (?, ?, ?, ?)",
                (date, message, sender, reciever))

    message_conn.commit()
    message_conn.close()


#getlast message
def getlastmessages():
    #get last message
    message_conn = sqlite3.connect('messages.db')
    message_c = message_conn.cursor()
    t =(date_accessed,username,username)
    message_c.execute("SELECT * FROM messages WHERE date >= ? AND (reciever = ? OR sender = ?) ORDER BY date DESC", t)
    print(message_c.fetchone())
    #message_c.execute("SELECT * FROM messages WHERE date >= ? AND (reciever = ? OR sender = ?)", t)
    #print(message_c.fetchone())[message_c.]
    #"SELECT COUNT(*) FROM messages WHERE date >= ? AND (reciever = ? OR sender = ?)"

getallmessages()
ts = time.time()
date_accessed = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
addsolomessage()
time.sleep(1)

getlastmessages()


addsolomessage()
#date_accessed = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
time.sleep(1)

getlastmessages()
addsolomessage()
getlastmessages()






#maybe just handle on client side as a value

#have no wrote code yet to pass messages back to client




