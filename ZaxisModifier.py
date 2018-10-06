from utilery import Reader
from utilery import Writer
from mAgenerator import mPrint
###############################################################################
#####This is the menu of this section
print('Insert the feed rate in mm/m (we made the proof with 9000)')
Velocity=input('Feed rate (Velocity) :')
print('Inser in mm how much you want to move the')
Distance=input('z axis :')
################################################## here ends the menu

#### Here start the modifying part
R=Reader()
W=Writer()
name='ZAxisSetup'
Read=R.checksE(name, True )
Read.close()
matrix=mPrint()
matrix.moveZaxis(Velocity,Distance)
print(R.path)
W.writePerLine(matrix.mA, R.path)
print('***********************')
print('*You will find the file*')
print('* in the  path of the  *')
print('*       program        *')
print('***********************')
