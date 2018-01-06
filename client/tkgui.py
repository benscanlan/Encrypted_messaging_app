#!/usr/local/bin/python3.6
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from client import Client
#from client.py import client_functions
"""You should divorce your gui code from your client api code. simply call functions from gui and have them return an action."""
"""other things to do besides bite the bullet, write a demo with message objects"""

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
        self.si_lbl = Label(self,text = "Sign In")
        self.si_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W) #row = 0, Position the Label
        #Line One Blue
        self.line_lbl = Label(self,text = "_________________________________________",fg="light blue",font=6)
        self.line_lbl.grid(row = 1, column = 0, columnspan = 2, sticky = W) #row = 1, Position the Line
        #Label "User Name:"
        self.inst_lbl = Label(self,text = "User Name:")
        self.inst_lbl.grid(row = 3, column = 0, columnspan = 2, sticky = W) #row = 2, Position the Label
        
        #failed Line creating attempt, cannot combine canvas and grid for multiple widgets, this was a none starter...
        #self.line = create_line(16,0,16,500, fill="blue",tags="line")
        #self.grid.create_line(16, 0, 16, 500, fill="red",tags="line")
        
        #Entry_Widget to accept username
        self.un_ent = Entry(self)
        self.un_ent.grid(row = 4, column = 0 , sticky = W)
        #Label for password
        self.pw_lbl = Label(self,text = "Password: ")
        self.pw_lbl.grid(row = 5, column = 0 , sticky = W)
        #Entry_Widget to accept password
        self.pw_ent = Entry(self)
        self.pw_ent.config(show="*")
        self.pw_ent.grid(row = 6, column = 0 , sticky = W)
        #Button "SIGN IN"
        self.si_bttn = Button(self)
        self.si_bttn["text"]= "SIGN IN"
        self.si_bttn["command"] = self.login_attempt #ACTIVATE SIGNIN COMMAND HERE
        self.si_bttn.grid(row = 7, column = 0, columnspan = 3, sticky = W)
        #forgot password notification label
        self.t = StringVar()
        self.fpwn_lbl = Label(self,textvariable = self.t, fg="red")
        self.fpwn_lbl.grid(row = 8, column = 0 , sticky = W)
        #Spacer Label
        self.sp1_lbl = Label(self,text = "")
        self.sp1_lbl.grid(row = 9, column = 0 , sticky = W)
        #Clickable Label "Forgot Password?"
        self.fgpw_lbl = Label(self,text = "Forgot Password?",fg="light blue")
        self.fgpw_lbl.grid(row = 10, column = 0 , sticky = W)
        #Cont.. Fuction call self.functionName no () gives mystery second arg "<ButtonPress event num=1 x=95 y=9>"
        self.fgpw_lbl.bind("<Button-1>",self.fakecall)
        #Line Two Blue
        self.inst_lbl = Label(self,text = "_________________________________________",fg="light blue",font=6)
        self.inst_lbl.grid(row = 11, column = 0, columnspan = 2, sticky = W)
        #Label "New User"
        self.pw_lbl = Label(self,text = "New User")
        self.pw_lbl.grid(row = 12, column = 0 , sticky = W)
        #Button "SIGN UP"
        self.su_bttn = Button(self)
        self.su_bttn["text"]= "SIGN UP"
        self.su_bttn["command"] = None #ACTIVATE SIGNUP COMMAND HERE
        self.su_bttn.grid(row = 13, column = 0, columnspan = 3, sticky = W)

    def fakecall(self,Button):
        print("hello")
        print(Button)
    
    def login_attempt(self):
        clientobj._username = self.un_ent.get()
        clientobj._password = self.pw_ent.get()
        
        print (clientobj._username)
        print (clientobj._password)
        clientobj.create_connection()
        clientobj.print_user()
        clientobj.pass_user()
        user_status_string = clientobj.verify_user()
        self.t.set(user_status_string)
        if user_status_string == 'password correct':
            self.new_window()

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
    
    def create_widgets(self):
        global user_list
        user_list = []
        #global user_list
        user_list = clientobj.get_user_list()
        print(user_list)
        #create label for password
        self.pw_lbl = Label(self,text = "Contacts ")
        self.pw_lbl.grid(row = 0, column = 0 , sticky = W)
        #self.pw_lbl = Label(self,text = "Hello ")
        #self.pw_lbl.grid(row = 1, column = 2 , sticky = W)
        
        #contacts list
        #self.yScroll = Scrollbar(self, orient=VERTICAL)
        ##self.listbox = listbox(self,width = 30,height= 3)
        #height=20,yscrollcommand=self.yScroll.set) #doesnt add a actually scrollbar
        
        #Listbox for Contacts
        scrollbar = Scrollbar(self, orient=VERTICAL)
        self.listbox = Listbox(self,width = 30, height= 3, yscrollcommand=scrollbar.set)
        self.listbox.grid(row=2, column=0,sticky =W)
        self.listbox.focus_set()
        scrollbar["command"] = self.listbox.yview
        scrollbar.grid(row=2, column=1, sticky=NS)

        #self.listbox.insert(END, "a list entry")
        
        for item in user_list:
            self.listbox.insert(END, item)

        self.sm_bttn = Button(self)
        self.sm_bttn["text"]= "SEND MESSAGE"
        self.sm_bttn["command"] = self.new_window
        self.sm_bttn.grid(row = 3, column = 0, columnspan = 1, sticky = E)
    
    def new_window(self):
        #print(user_list)
        #user_list[self.listbox.curselection()[0]]
        clientobj.select_user(user_list[self.listbox.curselection()[0]])
        #print(self.listbox.curselection()[0])
        #https://www.tutorialspoint.com/python/tk_listbox.htm
        #has to return username to avoid a new user shifting the values in db transactions.
        for widget in root.winfo_children():
            widget.destroy()
        
        #self.frame = tk.Toplevel(self.master) #pop ups
        
        self.app = MessageView(root)



########################################################################

class MessageView(Frame):
    def __init__(self,master):
        super(MessageView, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        convo_list = []
        convo_list = clientobj.get_coversation()
        
        #Listbox for Messages
        scrollbar = Scrollbar(self, orient=VERTICAL)
        self.listbox = Listbox(self,width = 30,height= 3, yscrollcommand=scrollbar.set)
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
        self.send_ent = Entry(self)
        self.send_ent.grid(row = 3, column = 0 , sticky = W)

        self.send_bttn = Button(self)
        self.send_bttn["text"]= "SEND"
        self.send_bttn["command"] = self.send_attempt
        self.send_bttn.grid(row = 3, column = 1, columnspan = 1, sticky = E)

    def send_attempt(self):
        clientobj._post_message = self.send_ent.get()
        clientobj.post_message()
            


########################################################################

#main
root = Tk()
root.title("Secure Messenger")
root.geometry("300x500")
clientobj = Client()
app = LoginView(root)
root.mainloop()
