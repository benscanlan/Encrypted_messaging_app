#!/usr/local/bin/python3.6
import socket, sys, ssl
class Client():
    def __init__(self):
        self._username = str("default")
        self._password = str("default")
        self._host = 'localhost' # '127.0.0.1' can also be used
        self._port = 10033
        self._sock = " "
        #self._returning_user_string = 'y'
        #self._new_user = b'0'
        #self._returning_user = b'1'
        self._new_user = "0"
        self._returning_user = "1"
        self._ssl_sock = " "
        self._first_get_covno_call = " "
        self._post_message = "If you are seeing this an error has occured"
        self._number_of_messages = 0
        self._filename = str("default")
        self._basename = b''

    def print_user(self):
        print(self._username)
        print(self._password)
        print(self._host)
        print(self._port)
        #self._sock = " "
        print(self._returning_user)
        #self._ssl_sock = " "
    
    def create_connection(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._ssl_sock = ssl.wrap_socket(self._sock,
                                   ca_certs="server.crt",
                                   cert_reqs=ssl.CERT_REQUIRED)
        
        self._ssl_sock.connect((self._host, self._port)) #Connect takes tuple of host and port or sock.connect((host, port))

    def pass_user(self): 
        #data = self._ssl_sock.read()
        #print(data.decode('utf-8'))
        print("Requesting Access...")
        self._ssl_sock.write(self._returning_user.encode('utf-8'))
        self._ssl_sock.write(self._username.encode('utf-8'))
        self._ssl_sock.write(self._password.encode('utf-8'))
    
    def verify_user(self):
        return (self._ssl_sock.read().decode('utf-8'))
    


    def get_user_list(self):
        print("Waiting for user list...")
        number_of_users = self._ssl_sock.read()
        number_of_users = number_of_users.decode('utf-8')
        print(number_of_users)
        number_of_users = int(number_of_users)
        print(number_of_users)
        user_list = []
        for i in range(number_of_users):
            data = self._ssl_sock.read().decode('utf-8')
            user_list.append(data)
            #if(wait longet than 8 seconds break)
        
        print("select a user to message")
        #print(user_list)
        for i in range(number_of_users):
            print(i, ' ', user_list[i]) #.button then add function to take you to message (should be a scrollable clicakle contact list.)
        return user_list
    
    def select_user(self, recipient):
        self._ssl_sock.write(recipient.encode('utf-8'))
    
    def select_action(self,action):
        self._ssl_sock.write(action.encode('utf-8'))
    
    def select_send_file(self):
        print(self._basename)
        self._ssl_sock.write(self._basename)
        f = open(self._filename,'rb')
        l = f.read(1024)
        while (l):
            self._ssl_sock.write(l)
            #print('Sent ',repr(l))
            l = f.read(1024)
        f.close()
        self._ssl_sock.write("endoffile".encode('utf-8'))
        
    def select_get_file(self):
        #read a filename from server
        #save it to the basename var because why the fuck not
        #read in that file saving it with that filename
        #server will not care if 1024 or whatever it will just take the whole content of the message and write it to the open file listener.
        # Will eventually have to add code to file upload that adds to the database file so for now just write a get file hardcoded version. ('   :)   ')
        self._basename = self._ssl_sock.read()
        with open(self._basename, 'wb') as f:
            print ('file opened')
            while True:
                print('receiving data...')
                data = self._ssl_sock.read()
                print('data=%s', (data))
                try:
                    if not data or data.decode('utf-8') == "endoffile":
                        break
                except:
                    pass
                # write data to a file
                f.write(data)

        f.close()
        return
        
    

    def get_conversation(self):
        print("get_conversation() called")
        print(self._number_of_messages)
        self._number_of_messages = "default"
        self._number_of_messages = self._ssl_sock.read()
        self._number_of_messages = self._number_of_messages.decode('utf-8')
        print(self._number_of_messages) #This is printing nothing on second call
        self._number_of_messages = int(self._number_of_messages)
        print(self._number_of_messages) #This is printing [] on second call
        convo_list = []
        i=0
        for i in range(self._number_of_messages):
            data = self._ssl_sock.read()
            print(data)
            data = data.decode('utf-8')
            print(data)
            convo_list.append(data)
        #if(wait longet than 8 seconds break)
        return convo_list


        
    def post_message(self):
        self._ssl_sock.write(self._post_message.encode('utf-8'))
        #should call an update to the message list.
        #better if it posts to the list then sends tho.
        #it might be easier to just update the whole list.
        #retreive message list from db
        #will always call get last message if it is eqivalent it wont print it
        
    def new_message_check(self):
        data = self._ssl_sock.read()
        return data
    



    def create_user(self):
        self._ssl_sock.write(self._new_user.encode('utf-8'))
        self._ssl_sock.write(self._username.encode('utf-8'))
        self._ssl_sock.write(self._password.encode('utf-8'))
        return (self._ssl_sock.read().decode('utf-8'))
#        if returning_user_string == 'y':
#            self._ssl_sock.write(returning_user)
#        else:
#            self._ssl_sock.write(newuser)
        #ssl_sock.close()




    def testloop(self):
    #Infinite loop to keep client running.
        while True:
            data = ssl_sock.read()
            print(data.decode('utf-8'))
            #print(data)
            message='HI! I am client.'
            ssl_sock.write(message.encode('utf-8'))
            #sock.send(message.encode('utf-8'))
         
        ssl_sock.close()


    #passuser()
    #testloop()
    #createconnection()
 
