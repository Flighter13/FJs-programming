from Fighter import *

F16C = Fighter("F-16", "viper")
print(F16C)
F16C.position_os()
F16C.aviation_os()
for f in F16C.control_surfaces:
    print(f)
