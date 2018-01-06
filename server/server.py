#!/usr/local/bin/python3.6

import os, socket, sys, ssl, sqlite3, datetime, time # Import all from module socket
import _thread as j
from user import User
from passlib.hash import pbkdf2_sha256 #'pip3.6 install passlib' on server running server code

ts = time.time()
date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

# Defining server address and port
host = 'localhost'  #'localhost' or '127.0.0.1' or '' are all same
port = 10032 #Use port > 1024, below it all are reserved

sock = socket.socket() #Creating socket object

sock.bind((host, port)) #Binding socket to a address. bind() takes tuple of host and port.
#wrappedSocket = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA") #This code is used down below. Kept for reference
#Listening at the address
sock.listen(5) #5 denotes the number of clients can queue
    

def client_thread(conn, encrypted): #2
        #I'm thinking this function should only call user.py function and not do any direct read or writes. That way code is more modular. For creating client side protocol.
        
        #create a user object
        userobj = User()
        #set user object varibales
        userobj._conn = conn #pass the socket
        userobj._encrypted = encrypted #pass the encrypted socket
        
        #greet the user
        #message = 'Hi! I am server\n'
        #encrypted.write(message.encode('utf-8'))
        
        userobj.pass_user()
        userobj.print_user()
        if userobj.verify_user():
            print("varriefied user")
            userobj.get_user_list()
            userobj.select_user()
            userobj.get_conversation()
            


        
#        
#        if userobj._verify_user():
#            while no exit
#                userobj._selectRecipient()
#                userobj._message_file_toggle()
#                
#                userobj._get_conversation()
#                userobj._
                
        #I'm going to put all navagation logic here. Dumb functions that just do wjhat asked. real code here. but client has to match logic. Maybe I should write the gui first then rewrite server code. 
        
        


#        userobj._username = encrypted.read().decode('utf-8')
#        userobj._password = encrypted.read().decode('utf-8')
#        userobj._returning_user = encrypted.read().decode('utf-8')
        

        
        ####
        #recursing to verify user ever time we use username variable
        #userobj._verifyUser(conn, encrypted, username, password, returning_user) #verify user should have a return type of username #verifyUser calls selectRecipient(conn, encrypted,username)
        
        #main menu
        #userobj._get_conversation(conn, encrypted, username) # get convo follows selecting getting a recieptient
        
        
        #make test loop into a convo loop
        #instead of threads it could be on a timer to call get and post. call for post should skip if nothing is entered. 
        
        #userobj.testloop()
        
        #will need disconnect(), #postamessage():, getmessages():, getonemessage():
        #set of functions for use to define user interaction

t_end = time.time() + 30 # 60 * 15 15 minutes
 
while time.time() < t_end: #1
    #Accepting incoming connections. Uses server side encryption.
    #print("while")
    conn, addr = sock.accept() #this is a waiting call!!
    #print("while2")
    encrypted = ssl.wrap_socket(conn,
                                 server_side=True,
                                 certfile="server.crt",
                                 keyfile="server.key")
    #print("while3")
    #Creating new thread. Calling clientthread function for this function and passing conn socket AND ENCRYPTED SOCKET as argument.
    j.start_new_thread(client_thread,(conn, encrypted,)) #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    #print("while")
    #break;

print("Server no longer accepting connections...")
time.sleep(20)

j.exit()
#sock.bind((host, port))
encrypted.close()
conn.close()
sock.shutdown()
sock.close()
#sock.bind((None, None))

exit()
