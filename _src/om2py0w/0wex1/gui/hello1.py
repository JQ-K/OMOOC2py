from Tkinter import *

root = Tk() #You should only create one root widget for each program, and it must be created before any other widgets.

w = Label(root, text="Hello, world!") #create a Label widget as a child to the root window:
w.pack()

root.mainloop()