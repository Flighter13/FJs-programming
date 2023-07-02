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

    
