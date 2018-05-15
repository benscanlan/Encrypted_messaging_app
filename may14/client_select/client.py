#!/usr/local/bin/python3.6
import socket, sys, ssl
class Client():
    def __init__(self):
        self._username = str("default")
        self._password = str("default")
        self._host = 'localhost' # '127.0.0.1' can also be used
        self._port = 10033
        self._sock = " "
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
        #print(self._host)
        #print(self._port)
        #self._sock = " "
        #print(self._returning_user)
        #self._ssl_sock = " "
    
    def create_connection(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._ssl_sock = ssl.wrap_socket(self._sock,
                                   ca_certs="server.crt",
                                   cert_reqs=ssl.CERT_REQUIRED)
        
        self._ssl_sock.connect((self._host, self._port)) #Connect takes tuple of host and port or sock.connect((host, port))

    def pass_user(self):
        self._ssl_sock.write(self._returning_user.encode('utf-8'))
        self._ssl_sock.write(self._username.encode('utf-8'))
        self._ssl_sock.write(self._password.encode('utf-8'))
    
    def verify_user(self):
        return (self._ssl_sock.read().decode('utf-8'))

    def get_user_list(self):
        #print("Waiting for user list...")
        
        number_of_users = self._ssl_sock.read()
        number_of_users = number_of_users.decode('utf-8')
        number_of_users = int(number_of_users)
        user_list = []
        for i in range(number_of_users):
            data = self._ssl_sock.read().decode('utf-8')
            user_list.append(data)
        
        #print("select a user to message")
        ##print(user_list)
        for i in range(number_of_users):
            #print(i, ' ', user_list[i]) #.button then add function to take you to message (should be a scrollable clicakle contact list.)
            return user_list

    def select_user(self, recipient):
        self._ssl_sock.write(recipient.encode('utf-8'))
    
    def select_action(self,action):
        self._ssl_sock.write(action.encode('utf-8'))
    
    def select_send_file(self):
        self._ssl_sock.write(self._basename)
        f = open(self._filename,'rb')
        l = f.read(1024)
        while (l):
            self._ssl_sock.write(l)
            l = f.read(1024)
        f.close()
        self._ssl_sock.write("endoffile".encode('utf-8'))

    def select_get_file(self):
        #Reads a filename from server passes it to the basename var,
        #Read in that file saving it with that filename
        #Server will not care if buffer is 1024 or anysize it will just take the whole content of the message and write it to the open file listener.
        if (True):   #self._ssl_sock.read() == "filefound"):
            self._basename = self._ssl_sock.read()
            with open("downloaded_files/" + self._basename.decode("utf-8"), 'wb') as f:
                print ('file opened')
                while True:
                    #print('receiving data...')
                    data = self._ssl_sock.read()
                    #print('data=%s', (data))
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
        self._number_of_messages = "default"
        self._number_of_messages = self._ssl_sock.read()
        self._number_of_messages = self._number_of_messages.decode('utf-8')
        self._number_of_messages = int(self._number_of_messages)
        convo_list = []
        i=0
        for i in range(self._number_of_messages):
            data = self._ssl_sock.read()
            data = data.decode('utf-8')
            convo_list.append(data)
        return convo_list

        
    def post_message(self):
        self._ssl_sock.write(self._post_message.encode('utf-8'))
        
    def new_message_check(self):
        data = self._ssl_sock.read()
        return data


    def create_user(self):
        self._ssl_sock.write(self._new_user.encode('utf-8'))
        self._ssl_sock.write(self._username.encode('utf-8'))
        self._ssl_sock.write(self._password.encode('utf-8'))
        return (self._ssl_sock.read().decode('utf-8'))


    def testloop(self):
        while True:
            data = ssl_sock.read()
            message='HI! I am client.'
            ssl_sock.write(message.encode('utf-8'))
        ssl_sock.close()

 
