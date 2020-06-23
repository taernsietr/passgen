import random
import string
from tkinter import *

## add buttons to predefined, more common values (8, 16, 32)

def new_password():

	text_pw.delete(1.0, END)
	
	if numbers.get() == True and symbols.get() == True:
		valid = string.ascii_letters + string.digits + string.punctuation
	elif numbers.get() == True and symbols.get() == False:
		valid = string.ascii_letters + string.digits
	elif numbers.get() == False and symbols.get() == True:
		valid = string.ascii_letters + string.punctuation
	else:
		valid = string.ascii_letters
	
	newpw = ''.join(random.choices(valid, k = pwlen.get()))
	
	if show_pw.get() == True:
		text_pw.insert(INSERT, newpw)
	root.clipboard_clear()
	root.clipboard_append(newpw)

def set_length(length):
	pwlen.set(length)
	scale_psize.set(length)

root = Tk()
root.title('Password Generator')

numbers = BooleanVar()
symbols = BooleanVar()
show_pw = BooleanVar()
pwlen = IntVar()

numbers.set(True)
symbols.set(True)
show_pw.set(True)
pwlen.set(16)

## CREATE WIDGETS

button_6 = Button(root, text = '6', width = 2, height = 1, command = lambda: set_length(6))
button_8 = Button(root, text = '8', width = 2, height = 1, command = lambda: set_length(8))
button_10 = Button(root, text = '10', width = 2, height = 1, command = lambda: set_length(10))
button_12 = Button(root, text = '12', width = 2, height = 1, command = lambda: set_length(12))
button_16 = Button(root, text = '16', width = 2, height = 1, command = lambda: set_length(16))
button_20 = Button(root, text = '20', width = 2, height = 1, command = lambda: set_length(20))
button_generate = Button(root, text = 'New Password', width = 16, height = 2, command = new_password)

check_includeNumbers = Checkbutton(root, text = 'Include numbers', onvalue = 1, variable = numbers)
check_includeSymbols = Checkbutton(root, text = 'Include symbols', onvalue = 1, variable = symbols)
check_showpw = Checkbutton(root, text = 'Show password', onvalue = 1, variable = show_pw)

text_pw = Text(root, width = 52, height = 5)
scale_psize = Scale(root, from_ = 4, to = 256, orient = HORIZONTAL, length = 300, sliderlength = 10, variable = pwlen)

## POSITION WIDGETS

button_6.grid(row = 0, column = 3, padx = 1, pady = 0)
button_8.grid(row = 1, column = 3, padx = 1, pady = 0)
button_10.grid(row = 2, column = 3, padx = 1, pady = 0)
button_12.grid(row = 0, column = 4, padx = 1, pady = 0)
button_16.grid(row = 1, column = 4, padx = 1, pady = 0)
button_20.grid(row = 2, column = 4, padx = 1, pady = 0)

button_generate.grid(row = 4, column = 0, padx = 4, pady = 4, sticky = W)

check_includeSymbols.grid(row = 0, column = 0, padx = 4, pady = 4, sticky = W)
check_includeNumbers.grid(row = 1, column = 0, padx = 4, pady = 4, sticky = W)
check_showpw.grid(row = 2, column = 0, padx = 4, pady = 4, sticky = W)

text_pw.grid(row = 0, column = 1, rowspan = 3, padx = 4, pady = 4)
scale_psize.grid(row = 4, column = 1, padx = 4, pady = 4)

root.mainloop()