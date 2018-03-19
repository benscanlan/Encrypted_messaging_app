#!/usr/local/bin/python3.6
# client.py
#import urllib.quote

import socket                   # Import socket module
import ntpath
from tkinter.filedialog import askopenfilename
#from shutil import copyfile
filename = askopenfilename()
print(filename)
"'%s'" % filename
print(filename)
basename = ntpath.basename(filename).encode('utf-8')
print(basename)


s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
s.send(basename)

#filename = '/Users/benscanlan/Desktop/mar6_workfiles/pythonft_2/myimage.jpeg'
#filename='myimage.jpeg'
f = open(filename,'rb')
l = f.read(1024)
while (l):
   s.send(l)
   #print('Sent ',repr(l))
   l = f.read(1024)
f.close()

print('Done sending')




print('Successfully get the file')
s.close()
print('connection closed')

