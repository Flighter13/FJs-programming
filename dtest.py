#imports
from tkinter import *
from tkinter.ttk import *
from time import *
from tkinter.dialog import *
DIALOG_ICON = 'questhead'

#time
root = Tk()
root.title('Time')
def timetk():
	string = strftime('%I:%M:%S %p')
	lbl.config(text=string)
	lbl.after(1000, timetk)

lbl = Label(root, font=('calibri', 40, 'bold'),
			background='gray',
			foreground='black')

lbl.pack(anchor='center')

def hud1():
        h1 = Dialog(None,{
                "title":"HUD1",
                "text":"Fighter Jet:",
                "strings":("F-14", "F-15", "F-16", "F-22", "Cancel"),
                "bitmap":DIALOG_ICON,
                "default":2
                })

 

#package for all functions and windows
def run_all_hud():
    timetk()
    hud1()
run_all_hud()
mainloop()
