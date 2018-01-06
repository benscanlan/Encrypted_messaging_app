#!/usr/local/bin/python3.6
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from client import Client

class ContactsView(Frame):
    def __init__(self,master):
        super(ContactsView, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        #create label for password
        self.pw_lbl = Label(self,text = "Contacts ")
        self.pw_lbl.grid(row = 0, column = 0 , sticky = W)

        #Listbox for Contacts
        scrollbar = Scrollbar(self, orient=VERTICAL)
        self.listbox = Listbox(self,width = 30, height= 3, yscrollcommand=scrollbar.set)
        self.listbox.grid(row=2, column=0,sticky =W)
        self.listbox.focus_set()
        scrollbar["command"] = self.listbox.yview
        scrollbar.grid(row=2, column=1, sticky=NS)

        self.listbox.insert(END, "a list entry")
        
        for item in ["one", "two", "three", "four"]:
            self.listbox.insert(END, item)

        self.sm_bttn = Button(self)
        self.sm_bttn["text"]= "SEND MESSAGE"
        self.sm_bttn["command"] = self.new_window
        self.sm_bttn.grid(row = 3, column = 0, columnspan = 1, sticky = E)

    def new_window(self):
        print("user selection")
        print(self.listbox.curselection())

########################################################################

#main
root = Tk()
root.title("Secure Messenger")
root.geometry("300x500")
clientobj = Client()
app = ContactsView(root)
root.mainloop()
