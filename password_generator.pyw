import random, string
import tkinter as tk
import tkinter.ttk as ttk

class Application(tk.Tk):
	def __init__(self):
		super().__init__()
		self.create_variables()
		self.create_checkboxes()
		self.create_widgets()
		self.create_buttons()

	def new_password(self):

		self.pw_display.delete(1.0, tk.END)
		
		if self.case.get() == 1:
			self.valid = string.ascii_uppercase
		elif self.case.get() == 2:
			self.valid = string.ascii_lowercase
		else:
			self.valid = string.ascii_letters

		if self.include_numbers.get() == True:
			self.valid = self.valid + string.digits
		if self.include_symbols.get() == True:
			self.valid = self.valid + string.punctuation
		
		self.new_pw = ''.join(random.choices(self.valid, k = self.pw_length.get()))
		
		if self.display_pw.get() == True:
			self.pw_display.insert(tk.INSERT, self.new_pw)
		self.clipboard_clear()
		self.clipboard_append(self.new_pw)
	
	def set_length(self, length):

		self.pw_length.set(length)
		self.pw_length_slider.set(length)

	def create_widgets(self):

		self.centerFrame = ttk.Frame(self)

		self.pw_display = tk.Text(self.centerFrame, width = 26, height = 10)
		self.pw_length_slider = ttk.Scale(self.centerFrame, from_ = 4, to = 256, orient = tk.HORIZONTAL, length = 300, variable = self.pw_length)

		self.pw_display.grid(row = 0, column = 0)
		self.pw_length_slider.grid(row = 1, column = 0)

		self.centerFrame.grid(row = 0, column = 1, padx = 20, pady = 20)

	def create_checkboxes(self):

		self.checkboxesFrame = ttk.Frame(self)
		self.radiobuttonsFrame = ttk.Frame(self)

		self.case_both = ttk.Radiobutton(self.radiobuttonsFrame, text = 'Both', value = 0, variable = self.case)
		self.case_upper = ttk.Radiobutton(self.radiobuttonsFrame, text = 'Uppercase only', value = 1, variable = self.case)
		self.case_lower = ttk.Radiobutton(self.radiobuttonsFrame, text = 'Lowercase only', value = 2, variable = self.case)

		self.include_numbers_check = ttk.Checkbutton(self.checkboxesFrame, text = 'Include numbers', onvalue = 1, variable = self.include_numbers)
		self.include_symbols_check = ttk.Checkbutton(self.checkboxesFrame, text = 'Include symbols', onvalue = 1, variable = self.include_symbols)
		self.display_pw_check = ttk.Checkbutton(self.checkboxesFrame, text = 'Show password', onvalue = 1, variable = self.display_pw)

		self.case_both.grid(row = 0, column = 0)
		self.case_upper.grid(row = 1, column = 0)
		self.case_lower.grid(row = 2, column = 0)
		self.include_numbers_check.grid(row = 1, column = 0)
		self.include_symbols_check.grid(row = 2, column = 0)
		self.display_pw_check.grid(row = 3, column = 0)

		self.radiobuttonsFrame.grid(row = 0, column = 0, padx = 40, pady = 20)
		self.checkboxesFrame.grid(row = 1, column = 0, padx = 40, pady = 20)

	def create_buttons(self):

		self.buttonsFrame = ttk.Frame(self)
		self.buttonSizes = [8, 10, 12, 16, 24, 32]
		self.buttons = []
		for btn in self.buttonSizes:
			self.buttons.append(ttk.Button(self.buttonsFrame, text = str(btn), width = 2, command = lambda size = btn: self.set_length(size)))
			self.buttons[-1].grid(row = 0, column = len(self.buttons)-1)
		self.button_generate = ttk.Button(self.buttonsFrame, text = 'New Password', width = 16, command = self.new_password)
		self.button_generate.grid(row = 1, column = 0, columnspan = len(self.buttons))

		self.buttonsFrame.grid(row = 1, column = 1, padx = 20, pady = 20)

	def create_variables(self):

		self.case = tk.IntVar()
		self.include_numbers = tk.BooleanVar()
		self.include_symbols = tk.BooleanVar()
		self.display_pw = tk.BooleanVar()
		self.pw_length = tk.IntVar()

		self.case.set(0)
		self.include_numbers.set(True)
		self.include_symbols.set(True)
		self.display_pw.set(True)
		self.pw_length.set(32)

def main():
	application = Application()
	application.title('Password Generator')
	application.mainloop()

if __name__ == '__main__':
	main()