#!/usr/local/bin/python3.6
import select, os, socket, sys, ssl # Imports all from module socket.
from user_object import User
#'pip3.6 install passlib' on server running server code. This library is used in 'user.py'.
#Defines server address and port.
host = 'localhost'  #'localhost' or '127.0.0.1' or '' are all equivalent.
port = 10033 #Use port a port greater than 1024. Below 1024 all ports are reserved

#Creates socket object.
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setblocking(0)
sock.bind((host, port)) #Binding socket to a address. bind() takes tuple of host and port.

#wrappedSocket = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA") #This code is used down below. Kept for reference

#Listening at the address.
sock.listen(50) #50 denotes the number of clients that can queue.

connection_list = []
connection_list.append(sock)

def shutdown():
    print("")
    print("Server no longer accepting connections...")

try:
    while True:
        #list_of_readable_sockets list or rlist: wait until ready for reading, wlist: wait_until_ready_for_writing, xlist: wait_for_an _exceptional_condition = select.select(connection_list,[],[])
        list_of_readable_sockets, wlist, error_sockets = select.select(connection_list,[],[])
        for current_sock in list_of_readable_sockets:
            if current_sock is sock:
                conn, addr = sock.accept()
                #print("accepted")
                encrypted = ssl.wrap_socket(conn,
                             server_side=True,
                             certfile="security/server.crt",
                             keyfile="security/server.key")

                #Create a user object.
                userobj = User()
                #Set user object variables.
                userobj._conn = conn #Pass the socket.
                userobj._encrypted = encrypted #Pass the encrypted socket.
                #Do not verify user or make new user here.
                #That would only works if thread is sitting and waiting.
                connection_list.append(userobj) # Instead make a verified and unvarified connections toggle.


            else: #it isnt listening sock so it breaks the connection currently

                msg = current_sock.read() #trigger happy read post_message() called multiple times
                print("msg=")
                print(msg)
                try:
                    msg = msg.decode('utf-8')
                except:
                    pass
                #Case structure for what you wanna do.
                #Pass user...
                #print("msg = ")
                #print( msg)
                if msg:
                    if(current_sock._order_number < 3):
                        ##print(msg)
                        current_sock.handle_msg(msg)
                    #Pass user end...
                    if(current_sock._returning_user == "0" and current_sock._order_number == 2):
                        current_sock.new_user()
                        #current_sock._order_number = current_sock._order_number - 1
                        current_sock._returning_user = "1"
                    if(current_sock._returning_user == "1" and current_sock._order_number == 2):
                        current_sock.verify_user()
                    if(current_sock._verified == 1 and msg == "back"): #allows user to go back
                            current_sock._order_number = 2
                    if(current_sock._verified == 1 and current_sock._order_number == 2):
                        current_sock.get_user_list()
                    if(current_sock._verified == 1 and current_sock._order_number == 3):
                        current_sock.select_user(msg)
                        #client needs a second send to say get convo or expect file
                    if(current_sock._verified == 1 and current_sock._order_number == 4 and msg =="getconvo"):
                        current_sock.get_conversation()
                    #if(current_sock._verified == 1 and msg == "update"):
                        #current_sock.get_conversation()
                    if(current_sock._verified == 1 and current_sock._order_number == 4 and msg == "postfile"):
                        #print("msg is part of a file")
                        current_sock._action = "postfile"

                    if(current_sock._verified == 1 and current_sock._order_number == 4 and msg == "getfile"):
                        print("asking for a file")
                        current_sock._action = "getfile"
                        try:
                            current_sock.send_relevant_file()
                            print("rev")
                        except:
                            current_sock.fileexcept()
                            print("nofilefound")


                    if(current_sock._verified == 1 and current_sock._order_number >= 5 and current_sock._action == "getconvo"
                    ):
                        if msg.encode('utf-8') is not b'':
                            if msg != "update" and msg != "getconvo" and current_sock._action != "postfile" and current_sock._action != "getfile":
                                current_sock.post_message(msg.encode('utf-8'))
                            if current_sock._action != "postfile" and current_sock._action != "getfile":
                                current_sock.get_conversation()
                        #Will add basename to message db. current_sock._action instead of msg should fix.

                    if (current_sock._verified == 1 and current_sock._order_number == 5 and current_sock._action == "postfile"):
                            current_sock._basename = msg
                            current_sock._f = open("hosted_files/" + current_sock._basename, 'wb')
                    if(current_sock._verified == 1 and current_sock._order_number >= 6 and current_sock._action == "postfile" and msg != "endoffile"):
                        try:
                            msg = msg.encode('utf-8')
                        except:
                            pass
                        current_sock._f.write(msg)
                    if(current_sock._verified == 1 and current_sock._order_number >= 6 and current_sock._action == "postfile" and msg == "endoffile"):
                        current_sock._f.close()
                        #database transaction should go here.
                        current_sock.postfile_to_database()
                        current_sock._encrypted.close()
                        current_sock._conn.close()
                        connection_list.remove(current_sock)



                    current_sock._order_number = current_sock._order_number + 1
                    #print("current_sock._order_number")
                    #print(current_sock._order_number)
                else:
                    current_sock._encrypted.close()
                    current_sock._conn.close()
                    connection_list.remove(current_sock)


        for current_sock in error_sockets: # close error sockets
            current_sock._encrypted.close()
            current_sock._conn.close()
            connection_list.remove(current_sock)




except KeyboardInterrupt:
    #time.sleep(20)
    shutdown()
