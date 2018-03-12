#test first but im pretty sure all these def (need self). 
import os, socket, sys, ssl, sqlite3, datetime, time
from passlib.hash import pbkdf2_sha256 #'pip install passlib' on server running server code
ts = time.time()
date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

class User:
    def __init__(self):
       
        self._conn = " "
        self._encrypted = " "
        self._returning_user = " "
        self._username = "default"
        self._password = "default"
        self._reciever = "default"
        self._date_accessed = " "
        self._first_get_covno_call = " "
        self._entered_message = "default"
        #self._static = "static"
        self._verified = 0
        self._order_number = 0
        self._action = "getconvo"
        self._basename = "file.txt"
        self._f = " "
        
    def fileno(self):
        return self._encrypted.fileno()
    
    def read(self):
        return self._encrypted.read()

    def handle_msg(self, msg):
        #Iterates once every call to handle_msg. 
        for self._order_number in range(self._order_number,self._order_number+1):
            if self._order_number == 0:
                self._returning_user = msg
            if self._order_number == 1:
                self._username = msg
            if self._order_number == 2:
                self._password = msg
                self.print_user()
            #self._order_number = self._order_number + 1
            print("self._order_number:")
            print(self._order_number)
    
                
        
    
    def print_user(self):
        print("self._returning_user:")
        print(self._returning_user)
        print("self._username:")
        print(self._username)
        print("self._password:")
        print(self._password)
        print("self._verified:")
        print(self._verified)
        print("self._reciever:")
        print(self._reciever)
        print("self._date_accessed:")
        print(self._date_accessed)
        print("self._entered_message:")
        print(self._entered_message)
        print("self._order_number:")
        print(self._order_number)

    
    def verify_user(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        t = (self._username,)
        # check is user exists

        c.execute('SELECT * FROM users WHERE username=?', t)
        exists = c.fetchone()
        if exists is None:
            self._encrypted.write("username password not correct".encode('utf-8'))
            print("username not correct") #send to client
            self._conn.close()
            conn.close()
            return
        
        else:
            c.execute('SELECT * FROM users WHERE username=?', t)
            hash=c.fetchone()[1]#breaks here when username doesnt exist, cant write simple logic for checking if user exists because c.execute is a pointer type.
            print("else loop")
        print(hash)
        if pbkdf2_sha256.verify(self._password, hash) == 1: #verification
            self._encrypted.write("password correct".encode('utf-8'))
            print("password correct") #change print to send
            self._verified = 1
            print(self._username)
            conn.close()
            return 1 # are verification is returning to the client thread
        else:
            self._encrypted.write("username password not correct".encode('utf-8'))
            print("username2 not correct") #send to client
            self._conn.close()
            conn.close()
            return
            #verifyUser() #recursiverly call, can be unlimited for project
        conn.close() #closes connection for users.db



    def get_user_list(self):
        user_conn = sqlite3.connect('users.db')
        c = user_conn.cursor()
        
        #writes the number of users
        i = 0
        for result in c.execute('SELECT username FROM users'):
            i = i + 1
        i = str(i)
        self._encrypted.write(i.encode('utf-8'))

        #send the user list
        for result in c.execute('SELECT username FROM users ORDER BY username'):
            self._encrypted.write(result[0].encode('utf-8'))

        user_conn.close()

    def select_user(self, msg):
        self._reciever = msg
        print(msg)
    
    def get_conversation(self): #get all previous
        message_conn = sqlite3.connect('messages.db')
        message_c = message_conn.cursor()
        t =(self._reciever,self._username,self._username,self._reciever)
        message_c.execute("SELECT * FROM messages WHERE (reciever = ? AND sender = ?) OR (reciever = ? AND sender = ?) ORDER BY date ASC", t)
        self._date_accessed = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        self._first_get_covno_call = message_c.fetchall()
        number_of_tuples = len(self._first_get_covno_call)
        self._encrypted.write(str(number_of_tuples).encode('utf-8'))

        for i in range(0, len(self._first_get_covno_call)): #len(self._first_get_covno_call) means number_of_tuples
            temp_message = str(self._first_get_covno_call[i][0] + " " + self._first_get_covno_call[i][2] + ": " + self._first_get_covno_call[i][1])
            self._encrypted.write(temp_message.encode('utf-8'))
        
    #getlast message
    def getlastmessages(self):
        #get last message
        message_conn = sqlite3.connect('messages.db')
        message_c = message_conn.cursor()
        t =(self._date_accessed,self._reciever,self._username,self._reciever,self._username,)
        message_c.execute("SELECT * FROM messages WHERE date >= ? AND (reciever = ? AND sender = ?) OR (reciever = ? AND sender = ?) ORDER BY date DESC", t)
        self._date_accessed = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        self._encrypted.write(str(message_c.fetchall()).encode('utf-8'))
        #message_c.execute("SELECT * FROM messages WHERE date >= ? AND (reciever = ? OR sender = ?)", t)
        #print(message_c.fetchone())[message_c.]
        #"SELECT COUNT(*) FROM messages WHERE date >= ? AND (reciever = ? OR sender = ?)"
    


    def get_message_to_post(self):
        print("get_message_to_post()")
        #Get a message to post from the client.
        connection_list = [] #append a client obj.
        connection_list.append(self._encrypted)
        list_of_readable_sockets, unused1, unused2 = select.select(connection_list, [], [])
        for current_sock in list_of_readable_sockets:
            if current_sock is self._encrypted:
                self._entered_message = self._encrypted.read()
        #self._reciever = self._encrypted.read().decode('utf-8')
        
        
        
        #self._entered_message = self._encrypted.read()
        #self._reciever = self._encrypted.read().decode('utf-8')
        return self._entered_message
        
        
    def post_message(self,msg):
        self._entered_message = msg
        if self._entered_message is not b'':
            self._entered_message = self._entered_message.decode('utf-8')
            print("post_message()")
            print(self._entered_message)
            #self.print_user()
            message_conn = sqlite3.connect('messages.db')
            message_c = message_conn.cursor()
            ts = time.time()
            date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            #c.execute("INSERT INTO messages VALUES ($username,$hash)")
            t = (date, self._entered_message, self._username, self._reciever)
            message_c.execute("INSERT INTO messages (date, message, sender, reciever) values (?, ?, ?, ?)", t)
            message_conn.commit()
            # We can also close the connection if we are done with it.
            # Just be sure any changes have been committed or they will be lost.
            message_conn.close()

    def check_for_new_message(self):
        #if sender reciever = new message from database in the last 3 seconds update/return true else return false.
        message_conn = sqlite3.connect('messages.db')
        message_c = message_conn.cursor()
        t =(self._reciever,self._username,self._username,self._reciever)
        message_c.execute("SELECT * FROM messages WHERE (reciever = ? AND sender = ?) OR (reciever = ? AND sender = ?) ORDER BY date ASC", t)
        
        mess = message_c.fetchall()
        
        if self._first_get_covno_call != mess:
            print(mess)
            return 1
    
        else:
            return 0
        

    
    def new_user(self):
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        t = (self._username,)
        c.execute('SELECT * FROM users WHERE username=?', t)
        exists = c.fetchone()
        conn.close()
        if exists is None:
            hash = pbkdf2_sha256.encrypt(self._password, rounds=200000, salt_size=16)
            conn = sqlite3.connect('users.db')
            c = conn.cursor() # create a cursor to iterate through database
            c.execute("INSERT INTO users (username, password_hash) values (?, ?)",
                (self._username, hash))
            conn.commit()
            conn.close()
            self._encrypted.write("username accepted".encode('utf-8'))

        
        else:
            self._encrypted.write("username not accepted".encode('utf-8'))
            #use verify user logic to passback username taken message to signup page
    
    def testloop(self): #use for testing a way to gracefully close connection.
        while True:
            #Sending message to connected client
            message = 'Hi! I am server\n'
            self._encrypted.write(message.encode('utf-8')) #send only takes string
            #Receiving from client
            data = self._encrypted.read() # 1024 stands for bytes of data to be received
            #print(data.decode('utf-8'))
