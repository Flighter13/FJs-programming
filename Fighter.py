"""
"""

#imports
from time import *
from random import *
from tkinter import *
from tkinter.simpledialog import *
from tkinter.dnd import *
from tkinter.commondialog import *
from tkinter.dialog import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from tkinter.filedialog import *
from tkinter.constants import *
from string import *
from gps_coords import *
import sys
sys.path

root = Tk()
root.geometry("+1+1")
###parent Fighter

class Fighter:
    def __init__(self, model, name):
        self.model = model.upper()
        self.name = name
        if capwords(name) != "Lightning Ii":
            self.name = capwords(name)
        else:
            self.name = "Lightning II"
        

    def __str__(self):
        return f"{self.model} {self.name}" 

    def aviation_os(self):
        self.control_surfaces = [
            "flaps",
            "ailerons",
            "rudders",
            "elevators",
            "flaperons",
            "horizontal stabilizers",
            "vertical stabilizers"
            ]

    def disp_coordinates(self):
            print("coords: " + lat, lon)
            

    def position_os(self):
        print("GPS")
        
    def communication_os(self):
        pass

    def radar_os(self):
        pass

    def munitions_os(self):
        pass

    def full_console():
        def left_console():
            lc1 = Tester(root)
            lc1.top.geometry("+1+60")
            i1 = Icon("Engine Start")
            i2 = Icon("PULL TO EJECT")
            i3 = Icon("ICON3")
            i1.attach(lc1.canvas)
            i2.attach(lc1.canvas)
            i3.attach(lc1.canvas)
            root.mainloop()
        left_console()


"""
Specific model of Fighter class, set to the specifications of the F-16 Fighting Falcon, often called the Viper

"""
from Fighter import *
class F_16(Fighter):
    def __init__(self, block):
        self.block = block
        self.munitions = ["AIM-7", "AIM-9", "AIM-120","GBU-31", "GBU-38", "AGM-45", "AGM-65",
                  "AGM-78", "AGM-84", "AGM-88", "M61"]
    def __str__(self):
        return "F-16 Fighting Falcon"





if __name__ == '__main__':
    F16C = Fighter("F-16", "viper")
    F16C.full_console()

