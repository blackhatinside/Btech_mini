from tkinter import Tk, Label
from time import strftime

def run1():
	root = Tk()
	root.title("Clock")
	label =  Label(root, font=("ds-digital", 80), background = "black", foreground = "cyan")
	label.pack(anchor='center')
	def time():
		string = strftime('%I:%M:%S %p')
		label.config(text=string)
		label.after(1000, time)
	time()

	root.mainloop()
run1()