# coding=utf-8
from Tkinter import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from jqk_dairy import *

root = Tk()
root.title("kang's diary")
root.geometry('400x400')
w = Label(root, text="Welcom to kang's diary", pady=20)

w.pack()

var = StringVar(value="What do you want to write today?")

text_input = Entry(root, textvariable=var,width=36)
text_input.pack()

def print_content():
	append_text(var.get())
	text_output.config(text=get_text())
	var.set('')

#text_input = Entry(root)
#text_input.insert(0, "Hi, what's up")
#text_input.pack()

#def print_content():
	#print text_input.get()
	#text_input.delete(0,'end')

button = Button(root, text="print", command=print_content)
button.pack()

root.bind('<Return>', lambda event:print_content())

text_output = Message(root, textvariable=var, width=360,pady=20)
text_output.pack()


root.mainloop()