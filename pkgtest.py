from fjosh import *
from Fighter import *
from F_16 import *
F18D = Fighter("F-18", "Super Hornet")
print(F18D)
F18D.position_os()
print()

F16A = F_16(50)
print(F16A)
F16A.position_os()
F16A.disp_coordinates()
