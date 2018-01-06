#test first but im pretty sure all these def (need self). 
import os, socket, sys, ssl, sqlite3, datetime, time
from passlib.hash import pbkdf2_sha256 #'pip install passlib' on server running server code
ts = time.time()
date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

class User:
    def __init__(self):
        self._conn = " "
        self._encrypted = " "
        self._username = "default"
        self._password = "default"
        self._reciever = "default"
        self._returning_user = " " #should be a compleately a new class call. if user class is called the user should be a retunring user. or as ive writien it its the same function. will worry about new users later.
        self._date_accessed = " "
        self._first_get_covno_call = " "
    
    def print_user(self):
        print(self._username)
        print(self._password)
    
    def pass_user(self):
        self._username = self._encrypted.read().decode('utf-8')
        self._password = self._encrypted.read().decode('utf-8')

    
    def verify_user(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        t = (self._username,)
#        check is user exists
#        var = c.execute('select count(1) from users where username =?', t)
#        print(var)
#        if var == 1:
#            conn.close()
#            return

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
        print(hash)
        if pbkdf2_sha256.verify(self._password, hash) == 1: #verification
            self._encrypted.write("password correct".encode('utf-8'))
            print("password correct") #change print to send
            print(self._username)
            conn.close()
            return 1 # are verification is returning to the client thread
        else:
            self._encrypted.write("username password not correct".encode('utf-8'))
            print("username not correct") #send to client
            self._conn.close()
            conn.close()
            return
            #verifyUser() #recursiverly call, can be unlimited for project
        conn.close() #closes connection for users.db



    def get_user_list(self):
        user_conn = sqlite3.connect('users.db')
        c = user_conn.cursor()
        
        #create user numbers
        i = 0
        for result in c.execute('SELECT username FROM users'):
            i = i + 1
        i = str(i)
        print(i)
        self._encrypted.write(i.encode('utf-8'))

        #send the user list
        for result in c.execute('SELECT username FROM users ORDER BY username'):
            #print(result[0])
            self._encrypted.write(result[0].encode('utf-8'))

        user_conn.close()

    def select_user(self):
        self._reciever = self._encrypted.read().decode('utf-8')
        print(self._reciever)
    
    
    def get_conversation(self): #get all previous
        message_conn = sqlite3.connect('messages.db')
        message_c = message_conn.cursor()
        t =(self._reciever,self._username,self._username,self._reciever)
        message_c.execute("SELECT * FROM messages WHERE (reciever = ? AND sender = ?) OR (reciever = ? AND sender = ?) ORDER BY date ASC", t) #sql wont trip if variable is not assigned so make sure it is passed to the function with sql using the variable or else it will find nothing []
        self._date_accessed = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        self._first_get_covno_call = message_c.fetchall()
        print(self._first_get_covno_call)
        print(len(self._first_get_covno_call))
        number_of_tuples = len(self._first_get_covno_call)
        self._encrypted.write(str(number_of_tuples).encode('utf-8'))

        for i in range(0, len(self._first_get_covno_call)): #len(self._first_get_covno_call) means number_of_tuples
            print(self._first_get_covno_call[i][0] + " " + self._first_get_covno_call[i][2] + ": " + self._first_get_covno_call[i][1])
            temp_message = str(self._first_get_covno_call[i][0] + " " + self._first_get_covno_call[i][2] + ": " + self._first_get_covno_call[i][1])
            self._encrypted.write(temp_message.encode('utf-8'))
        #tuple
        self._encrypted.write(str(message_c.fetchall()).encode('utf-8'))

        #not needed not that we are using sql as a 4gl
        #i = 0
        #for result in message_c.execute("SELECT * FROM messages WHERE reciever = ? OR sender = ?", t):
        #    i = i + 1
        #i = i
        #print(i)
        
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
    


    def get_message_to_post(conn, encrypted,):
        print("get_message_to_post(conn, encrypted,)")
        #get a message to post from the client
        entered_message = encrypted.read().decode('utf-8')
        reciever = encrypted.read().decode('utf-8')
        
    def post_message(conn, encrypted,):
        print("post_message(conn, encrypted,)")
        #message fucntion should be
        message_conn = sqlite3.connect('messages.db')
        message_c = message_conn.cursor()
        date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print(username)

        #c.execute("INSERT INTO messages VALUES ($username,$hash)")
        message_c.execute("INSERT INTO messages (date, message, sender, reciever) values (?, ?, ?, ?)",(date, entered_message, username, reciever))
        t = ('username',)
        message_conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        message_conn.close()

    #add solo message
    def addsolomessage(conn, encrypted, username):
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
    
    def newUser(conn, encrypted):
        print("newUser(conn, encrypted)")
        #username
        hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16) # you would call this code when making a new account. Then we will store the hash in a shadow file? I think the salt is okay because we are using passlib
        c.execute("INSERT INTO users (username, password_hash) values (?, ?)",
            (username, hash))
        conn.commit()
        conn.close() #closes connection for user
    
    def testloop(self):
        while True:
            #Sending message to connected client
            message = 'Hi! I am server\n'
            self._encrypted.write(message.encode('utf-8')) #send only takes string
            #Receiving from client
            data = self._encrypted.read() # 1024 stands for bytes of data to be received
            print(data.decode('utf-8'))
