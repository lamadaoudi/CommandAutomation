import glob
from Commands import *

# com1 = GrepCommand("ENCS313-Outline-.pdf", "C:\\Users\\Main\\Documents\\BZU_LamaDaoudi\\LinuxLab")
# com1.executeGrep()
# print(com1.get_outputReport())
# com2= Mv_lastCommand("C:\\Users\\Main\\Documents\\BZU_LamaDaoudi\\LinuxLab\\Test\\Source", "C:\\Users\\Main\\Documents\\BZU_LamaDaoudi\\LinuxLab\\Test\\Source")
# com2.executeMv_last()
# print(com2.get_finishStatus())
# print(com2.get_outputReport())

com3 = CategorizeCommand("C:\\Users\\Main\\Documents\\BZU_LamaDaoudi\\LinuxLab\\Test\\Source")
com3.executeCategorize()