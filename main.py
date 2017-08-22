#!/usr/local/bin/python3

from tkinter import *
from tkinter import font
import socket
from random import randint
#import urllib2

#---Variables---#

text = font.Font(family='Helvetica', size=12)
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
Test = "http://www.google.com"     # address to test internet connection

#---Functions---#

def port():
    return randint(2000, 10000)

#def test():
 #   try:
  #      urllib2.urlopen(test, timeout=1)
   #     return True
    #except urllib2.URLError as err: pass
    #return False

#---GUI---#

root = Tk()
root.title("Chatsphere v1.0")                               #GUI title
w, h = root.winfo_screenwidth(), root.winfo_screenheight() #Get screen size and set to w and h
root.geometry("%dx%d+0+0" % (w, h))                        #Open application to fullscreen on startup

#---MenuBar---#

menu = Menu(root)
root.config(menu=menu)

#FileTab

filemenu = Menu(menu)

menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Test Connection")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

#ConnectionTab

connectionmenu = Menu(menu)

menu.add_cascade(label="Connections", menu=connectionmenu)

connectionmenu.add_command(label="Test Connection")
connectionmenu.add_separator()
connectionmenu.add_command(label="Terminate")

#---InfoBar---#

f = Frame(root, height=32, width=w, bd=2, relief = RAISED)
f.pack_propagate(0) # don't shrink!!!!!!!!!
f.pack(side=BOTTOM) #place at the bottom

test = Button(f, text="Test Connection", padx=30, command=root.quit) #button to test connection
test.pack(side=RIGHT)

conn = Label(f, bg='#fff000000', width=10, padx=30, text="no connection") #label to show conn state
#conn.pack_propagate(0)
conn.pack(side=RIGHT)

#---Connection viewer---#

connect = Frame(root, height=h, width=w/4, bd=2, relief=RAISED)
connect.pack_propagate(0)
connect.pack(side=LEFT)

#---Message viewer frame---#

messageFrame = Frame(root, height=h, width=w*0.75, bd=2, relief=FLAT)
messageFrame.pack_propagate(0)
messageFrame.pack(side=RIGHT)

encrypt = Frame(messageFrame, height=h*.4, width=w*0.75, bd=2, relief=RAISED)
encrypt.pack_propagate(0)
encrypt.pack(side=TOP)

decrypt = Frame(messageFrame, height=h*.5, width=w*0.75, bd=2, relief=RAISED)
encrypt.pack_propagate(0)
decrypt.pack(side=BOTTOM)

message = Text(decrypt, )
#--- Define main loop---#

root.config(menu=menu)
root.mainloop()
