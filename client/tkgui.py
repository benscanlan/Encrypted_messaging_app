#!/usr/local/bin/python3.6
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from client import Client
#from threading import Thread
import ntpath
from tkinter.filedialog import askopenfilename
#from LoginView import LoginView
#from SignUpView import SignUpView
#from ContactsView import ContactsView
#from MessageView import MessageView
import random
#from client.py import client_functions
"""GUI code is divorced from the networking_client API code. GUI simply calls functions from networking_client and they return an action."""
"""In the future, write a version with message objects."""
##############################################################

class LoginView(Frame):
    def __init__(self,master):
        super(LoginView, self).__init__(master)
        self.grid()
        #failed Line creating attempt, cannot combine canvas and grid for multiple widgets, this was a none starter...
        #self.canvas = Canvas(root, width=500, height=300, bg="white")
        #self.canvas.pack()
        
        self.create_widgets()#this is a function call!
    def create_widgets(self):
        #Label "Sign In" 
        self.sign_in_label = Label(self,text = "Sign In")
        self.sign_in_label.grid(row = 0, column = 0, columnspan = 2, sticky = W) #row = 0, Position the Label
        #Line One Blue
        self.line_1_label = Label(self,text = "_________________________________________",fg="light blue",font=6)
        self.line_1_label.grid(row = 1, column = 0, columnspan = 2, sticky = W) #row = 1, Position the Line
        #Label "User Name:"
        self.username_label = Label(self,text = "Username:")
        self.username_label.grid(row = 3, column = 0, columnspan = 2, sticky = W) #row = 2, Position the Label
        
        #failed Line creating attempt, cannot combine canvas and grid for multiple widgets, this was a none starter...
        #self.line = create_line(16,0,16,500, fill="blue",tags="line")
        #self.grid.create_line(16, 0, 16, 500, fill="red",tags="line")
        
        #Entry_Widget to accept username
        self.username_entry = Entry(self)
        self.username_entry.grid(row = 4, column = 0 , sticky = W)
        #Label for password
        self.password_label = Label(self,text = "Password: ")
        self.password_label.grid(row = 5, column = 0 , sticky = W)
        #Entry_Widget to accept password
        self.password_entry = Entry(self)
        self.password_entry.config(show="*")
        self.password_entry.grid(row = 6, column = 0 , sticky = W)
        #Button "SIGN IN"
        self.sign_in_button = Button(self)
        self.sign_in_button["text"]= "SIGN IN"
        self.sign_in_button["command"] = self.login_attempt #ACTIVATE SIGNIN COMMAND HERE
        self.sign_in_button.grid(row = 7, column = 0, columnspan = 3, sticky = W)
        #forgot password notification label
        self.notification_1 = StringVar()
        self.fpwn_label = Label(self,textvariable = self.notification_1, fg="red")
        self.fpwn_label.grid(row = 8, column = 0 , sticky = W)
        #Spacer Label
        self.spacer_label = Label(self,text = "")
        self.spacer_label.grid(row = 9, column = 0 , sticky = W)
        #Clickable Label "Forgot Password?"
        self.forgot_password_label = Label(self,text = "Forgot Password?",fg="light blue")
        self.forgot_password_label.grid(row = 10, column = 0 , sticky = W)
        #Cont.. Fuction call self.functionName no () gives mystery second arg "<ButtonPress event num=1 x=95 y=9>"
        self.forgot_password_label.bind("<Button-1>",self.fakecall)
        #Line Two Blue
        self.line_2_label = Label(self,text = "_________________________________________",fg="light blue",font=6)
        self.line_2_label.grid(row = 11, column = 0, columnspan = 2, sticky = W)
        #Label "New User"
        self.password_label = Label(self,text = "New User")
        self.password_label.grid(row = 12, column = 0 , sticky = W)
        #Button "SIGN UP"
        self.sign_up_button = Button(self)
        self.sign_up_button["text"]= "SIGN UP"
        self.sign_up_button["command"] = self.sign_up #ACTIVATE SIGNUP COMMAND HERE
        self.sign_up_button.grid(row = 13, column = 0, columnspan = 3, sticky = W)
    
    def fakecall(self,Button):
        print("hello")
        print(Button)
    
    def login_attempt(self):
        if self.username_entry.get() != "":
            clientobj._username = self.username_entry.get()
        if self.password_entry.get() != "":
            clientobj._password = self.password_entry.get()
        
        #print(clientobj._username)
        #print(clientobj._password)
        clientobj.create_connection()
        clientobj.print_user()
        clientobj.pass_user()
        user_status_string = clientobj.verify_user()
        self.notification_1.set(user_status_string)
        if user_status_string == 'password correct':
            self.new_window()

    def new_window(self):
        
        for widget in root.winfo_children():
            widget.destroy()
        
        #self.frame = tk.Toplevel(self.master) #pop ups
        
        self.app = ContactsView(root)


    def sign_up(self):
        
        for widget in root.winfo_children():
            widget.destroy()
            
            #self.frame = tk.Toplevel(self.master) #pop ups
            
        self.app = SignUpView(root)

#####################################################################

class SignUpView(Frame):
    def __init__(self,master):
        super(SignUpView, self).__init__(master)
        self.grid()
        #failed Line creating attempt, cannot combine canvas and grid for multiple widgets, this was a none starter...
        #self.canvas = Canvas(root, width=500, height=300, bg="white")
        #self.canvas.pack()
        
        self.create_widgets()#this is a function call!
    def create_widgets(self):
        #Label "Sign In"
        self.sign_up_label = Label(self,text = "Sign Up")
        self.sign_up_label.grid(row = 0, column = 0, columnspan = 2, sticky = W) #row = 0, Position the Label
        #Line One Blue
        self.line_label = Label(self,text = "_________________________________________",fg="light blue",font=6)
        self.line_label.grid(row = 1, column = 0, columnspan = 2, sticky = W) #row = 1, Position the Line
        #Label "User Name:"
        self.username_label = Label(self,text = "Username:")
        self.username_label.grid(row = 3, column = 0, columnspan = 2, sticky = W) #row = 2, Position the Label
        
        #failed Line creating attempt, cannot combine canvas and grid for multiple widgets, this was a none starter...
        #self.line = create_line(16,0,16,500, fill="blue",tags="line")
        #self.grid.create_line(16, 0, 16, 500, fill="red",tags="line")
        
        #Entry_Widget to accept username
        self.username_entry = Entry(self)
        self.username_entry.grid(row = 4, column = 0 , sticky = W)
        #Label for password
        self.password_label = Label(self,text = "Password: ")
        self.password_label.grid(row = 5, column = 0 , sticky = W)
        #Entry_Widget to accept password
        self.password_entry = Entry(self)
        self.password_entry.config(show="*")
        self.password_entry.grid(row = 6, column = 0 , sticky = W)
        #Entry_Widget to accept password
        self.password_entry_2 = Entry(self)
        self.password_entry_2.config(show="*")
        self.password_entry_2.grid(row = 7, column = 0 , sticky = W)
        #Button "SIGN UP"
        self.sign_up_button = Button(self)
        self.sign_up_button["text"]= "SIGN UP"
        self.sign_up_button["command"] = self.sign_up_attempt #ACTIVATE SIGNIN COMMAND HERE
        self.sign_up_button.grid(row = 8, column = 0, columnspan = 3, sticky = W)
        #taken notification label
        self.notification_1 = StringVar()
        self.username_taken_label = Label(self,textvariable = self.notification_1, fg="red")
        self.username_taken_label.grid(row = 9, column = 0 , sticky = W)
        #forgot password notification label
        self.notification_2 = StringVar()
        self.missmatch_label = Label(self,textvariable = self.notification_2, fg="red")
        self.missmatch_label.grid(row = 10, column = 0 , sticky = W)
        #Spacer Label
        self.spacer_label = Label(self,text = "")
        self.spacer_label.grid(row = 10, column = 0 , sticky = W)

    def sign_up_attempt(self):
        clientobj._username = self.username_entry.get()
        self.notification_1.set("")
        self.notification_2.set("")


        #print("sign_up_attempt")
        if self.password_entry.get() == self.password_entry_2.get():
            clientobj._password = self.password_entry.get()
            clientobj.create_connection()
            unused_password_correct_string = clientobj.create_user()


            #print(unused_password_correct_string)
            if unused_password_correct_string != "username not accepted":
                clientobj.verify_user()
                self.new_window()
            else:
                user_status_string = "This username is taken. Try " + clientobj._username + str(random.randint(1000,9999))
                self.notification_1.set(user_status_string)
            
        else:
            user_status_string = "password mismatch"
            self.notification_2.set(user_status_string)

    def new_window(self):
        
        for widget in root.winfo_children():
            widget.destroy()
            
            #self.frame = tk.Toplevel(self.master) #pop ups
            
            self.app = ContactsView(root)








#######################################################################

class ContactsView(Frame):
    def __init__(self,master):
        super(ContactsView, self).__init__(master)
        self.grid()
        self.create_widgets()
        root.title("Secure Messenger User: (" + clientobj._username + ")")
    
    def create_widgets(self):
        global user_list
        user_list = []
        #global user_list
        user_list = clientobj.get_user_list()
        #print(user_list)
        #create label for password
        self.password_label = Label(self,text = "Contacts ")
        self.password_label.grid(row = 0, column = 0 , sticky = W)
        #self.password_label = Label(self,text = "Hello ")
        #self.password_label.grid(row = 1, column = 2 , sticky = W)
        
        #contacts list
        #self.yScroll = Scrollbar(self, orient=VERTICAL)
        ##self.listbox = listbox(self,width = 30,height= 3)
        #height=20,yscrollcommand=self.yScroll.set) #doesnt add a actually scrollbar
        
        #Listbox for Contacts
        scrollbar = Scrollbar(self, orient=VERTICAL)
        self.listbox = Listbox(self,width = 90, height= 20, yscrollcommand=scrollbar.set)
        self.listbox.grid(row=2, column=0,sticky =W)
        self.listbox.focus_set()
        scrollbar["command"] = self.listbox.yview
        scrollbar.grid(row=2, column=1, sticky=NS)

        #self.listbox.insert(END, "a list entry")
        
        for item in user_list:
            self.listbox.insert(END, item)

        self.send_message_button = Button(self)
        self.send_message_button["text"]= "SEND MESSAGE"
        self.send_message_button["command"] = self.new_window
        self.send_message_button.grid(row = 3, column = 0, columnspan = 1, sticky = E)
        
        self.send_file_button = Button(self)
        self.send_file_button["text"]= "SEND FILE"
        self.send_file_button["command"] = self.file_transfer
        self.send_file_button.grid(row = 4, column = 0, columnspan = 1, sticky = E)
        
        self.get_file_button = Button(self)
        self.get_file_button["text"]= "GET FILE"
        self.get_file_button["command"] = self.get_file_transfer
        self.get_file_button.grid(row = 5, column = 0, columnspan = 1, sticky = E)
    
    def new_window(self):
        ##print(user_list)
        #user_list[self.listbox.curselection()[0]]
        clientobj.select_user(user_list[self.listbox.curselection()[0]])
        clientobj.select_action("getconvo")
        #clientobj.select_send_message() #This should be replaced by generic flagcall in latter versions.
        ##print(self.listbox.curselection()[0])
        #https://www.tutorialspoint.com/python/tk_listbox.htm
        #has to return username to avoid a new user shifting the values in db transactions.
        for widget in root.winfo_children():
            widget.destroy()
        
        #self.frame = tk.Toplevel(self.master) #pop ups
        
        self.app = MessageView(root)

    def file_transfer(self):
        clientobj.select_user(user_list[self.listbox.curselection()[0]])
        clientobj._filename = askopenfilename()
        #print(clientobj._filename)
        "'%s'" % clientobj._filename
        #print(clientobj._filename)
        clientobj._basename = ntpath.basename(clientobj._filename).encode('utf-8')
        #print(clientobj._basename)
        #network call
        clientobj.select_action("postfile")
        clientobj.select_send_file()#This should be replaced by generic flagcall in latter versions.
        for widget in root.winfo_children():
            widget.destroy()
        self.app = ChoiceView(root)

    def get_file_transfer(self):
        clientobj.select_user(user_list[self.listbox.curselection()[0]])
        clientobj.select_action("getfile")
        clientobj.select_get_file()
        for widget in root.winfo_children():
            widget.destroy()
        self.app = ChoiceView(root)




########################################################################

class ChoiceView(Frame):
    def __init__(self,master):
        super(ChoiceView, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.fss_label = Label(self,text = "File Sent Sucessfully")
        self.fss_label.grid(row = 0, column = 0 , sticky = W)
        self.send_button = Button(self)
#        self.send_button["text"]= "Back to Contacts"
#        self.send_button["command"] = self.back_to_contacts
#        self.send_button.grid(row = 1, column = 0, columnspan = 1, sticky = W)
#    def back_to_contacts(self):
#        clientobj.select_action("back")
#        for widget in root.winfo_children():
#            widget.destroy()
#        self.app = ContactsView(root)





########################################################################

class MessageView(Frame):
    def __init__(self,master):
        super(MessageView, self).__init__(master)
        self.grid()
        self.create_widgets()#order protects us from reading anything from get converstation into the thread since this executes first.
#        self.receive_thread = Thread(target=self.receive(clientobj))
#        self.receive_thread.start()

    def create_widgets(self):
        convo_list = []
        convo_list = clientobj.get_conversation()
        
        #Listbox for Messages
        scrollbar = Scrollbar(self, orient=VERTICAL)
        self.listbox = Listbox(self,width = 90,height= 21, yscrollcommand=scrollbar.set)
        self.listbox.grid(row=2, column=0,sticky =W)
        self.listbox.focus_set()
        scrollbar["command"] = self.listbox.yview
        scrollbar.grid(row=2, column=1, sticky=NS)

        for item in convo_list:
            self.listbox.insert(END, item)
        
        
#        scrolledtext = ScrolledText(self)
#        scrolledtext.grid(row=3,column=0,columnspan = 1,sticky=W)
#        scrolledtext.insert(END, "something")
#        scrolledtext.insert(END, "something")
#        scrolledtext.insert(END, "something")
#        scrolledtext.configure(state=DISABLED)

        #Entry_Widget to accept username
        self.send_entry = Entry(self)
        self.send_entry.grid(row = 3, column = 0 , columnspan = 3, sticky = EW)

        self.send_button = Button(self)
        self.send_button["text"]= "SEND"
        self.send_button["command"] = self.send_attempt
        self.send_button.grid(row = 4, column = 0, columnspan = 1, sticky = E)
    
        self.send_button = Button(self)
        self.send_button["text"]= "Update"
        self.send_button["command"] = self.up_attempt
        self.send_button.grid(row = 5, column = 0, columnspan = 1, sticky = E)

        self.send_button = Button(self)
        self.send_button["text"]= "Back to Contacts"
        self.send_button["command"] = self.back_to_contacts
        self.send_button.grid(row = 4, column = 0, columnspan = 1, sticky = W)
        
    def recursive_update(self):
        for widget in root.winfo_children():
            widget.destroy()
        #self.receive_thread.destroy()
        self.app = MessageView(root) #This recursively calls the class to update.

    def up_attempt(self):
        clientobj._post_message = str("update") #same as select_action
        clientobj.post_message()
        self.recursive_update()

    def back_to_contacts(self):
        clientobj.select_action("back")
        for widget in root.winfo_children():
            widget.destroy()
        self.app = ContactsView(root)

    def send_attempt(self):
        try:
            clientobj._post_message = self.send_entry.get()
            #print(clientobj._post_message) gets all characters! Issue not with entry widget. 
            clientobj.post_message()
            self.recursive_update() #This recursively calls the class to update.
        except:
            pass

#    def receive(self,clientobj): #Put last just to be sure.
#        """Handles receiving of messages."""
#        while True:
#            try:
#                msg = clientobj.new_message_check()
#                if (msg == "update"):
#                    self.up_attempt
#
#            except OSError:  # Possibly client has left the chat.
#                break


########################################################################

#main
try:
    root = Tk()
    root.title("Secure Messenger")
    root.geometry("835x460")
    clientobj = Client()
    app = LoginView(root)
    root.mainloop()

except KeyboardInterrupt:
#    clientobj._ssl_sock.shutdown(2) GIVES ERROR IF CLOSE 'x' out AFTER  unceseful login
    clientobj._ssl_sock.close()
#    clientobj._sock.shutdown()
    clientobj._sock.close()
    
    print("")
    print("Client is offline...")
