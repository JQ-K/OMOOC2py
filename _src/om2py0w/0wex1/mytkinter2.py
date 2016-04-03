# coding=utf-8

import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

import Tkinter as tk
from jqk_dairy import *


def enter_and_print(event):
	append_text(var.get())
	text_output.delete(0.0,'end')
	text_output.insert(0.0,get_text())
	var.set('')


root = tk.Tk()
root.title("kang's diary")

var = tk.StringVar(value="What do you want to write today?")

text_input = tk.Entry(root, textvariable=var, width=36, bd=5)
text_input.pack()

root.bind('<Return>', enter_and_print)

text_output = tk.Text(root,width=46)
text_output.pack(side='left', fill='y')

s =tk.Scrollbar(root)
s.pack(side='right', fill='y')

s.config(command=text_output.yview)
text_output.config(yscrollcommand=s.set)

root.mainloop()