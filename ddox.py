from tkinter import *
from tkinter.simpledialog import *
from time import *
from random import *
def test():
    root = Tk()
    def doit(root=root):
        d = SimpleDialog(root,
                     text="This is a test dialog, "
                          "testing value displaying",
                     buttons=["Yes", "No", "Cancel"],
                     default=0,
                     cancel=2,
                     title="Test Dialog")
        print(d.go())
        print(askinteger("Spam", "Egg count", initialvalue=12*12))
        print(askfloat("Spam", "Egg weight\n(in tons)", minvalue=1,
                       maxvalue=100))
        print(askstring("Spam", "Egg label"))
    t = Button(root, text='Test', command=doit)
    t.pack()
    q = Button(root, text='Quit', command=t.quit)
    q.pack()
    t.mainloop()
test()
