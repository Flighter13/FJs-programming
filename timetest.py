from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('Time')

# This function is used to
# display time on the label

def timetk():
	string = strftime('%I:%M:%S %p')
	lbl.config(text=string)
	lbl.after(1000, timetk)


lbl = Label(root, font=('calibri', 40, 'bold'),
			background='gray',
			foreground='black')

lbl.pack(anchor='center')
timetk()

mainloop()
