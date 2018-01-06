#!/usr/local/bin/python3.6
import socket, sys, ssl
class Client():
    def __init__(self):
        self._username = "default"
        self._password = "default"
        self._host = 'localhost' # '127.0.0.1' can also be used
        self._port = 10032
        self._sock = " "
        self._returning_user_string = 'y'
        self._newuser = b'0'
        self._returning_user = b'1'
        self._ssl_sock = " "
        self._first_get_covno_call = " "
        self._post_message = "If you are seeing this an error has occured"

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

    def get_coversation(self):
        print("get_coversation() called")
        number_of_messages = self._ssl_sock.read()
        number_of_messages = number_of_messages.decode('utf-8')
        print(number_of_messages)
        number_of_messages = int(number_of_messages)
        print(number_of_messages)
        convo_list = []
        for i in range(number_of_messages):
            data = self._ssl_sock.read().decode('utf-8')
            convo_list.append(data)
        #if(wait longet than 8 seconds break)
        print(convo_list[3])
        return convo_list


        
    def post_message(self):

        entered_message = input("Say: ")
        print( " said:" , entered_message)

        #ssl_sock.write(username.encode('utf-8')) Server already knows who its talking to in thread
        ssl_sock.write(entered_message.encode('utf-8'))
        #ssl_sock.write(user_list[selected_contact_number].encode('utf-8'))



        #goals
        #select one user name from list. build a message and post it to db

        #retreive message list from db
        #will always call get last message if it is eqivalent it wont print it


    def createuser(self):
        if returning_user_string == 'y':
            self._ssl_sock.write(returning_user)
        else:
            self._ssl_sock.write(newuser)
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
 
