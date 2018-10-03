from utilery import Reader
from utilery import Writer
import utilery as Tools
R=Reader()
print('You are in easy mode gCode set Z axis modifier')
print('In order to use the easy mode, please put your files in the same carpet of the program')
print('To use it in easy mode please put your gCodes files in the same carpet of the program')
print('However, if you want to put all the path name please choose manual mode')
print('easy mode(1) manual mode(2) ')
s=int(input('Select: '))
sw=0
print('------------------')
if s==1:
    print('Easy Mode')
    print('Insert the name of your file')
    #p=input('(without .gcode) :')
    p='DPE_Tensile-8'
elif s==2:
    print('Manual mode')
    print('Insert the path of your file, please be sure of ')
    p=input('put all the information')
    p=p.replace('\\','/')
else:
    print('Please choose a valid option')
    s=3
print('--------------')
if s!=3:
    R=Reader()
    W=Writer()
    if s==1:
        Read=R.oFile(p)
    if s==2:
        Read=R.oFullPath(p)
    B=Read.readlines()
    Read.close()
    #z=input('Enter the Z start value :')
    z=1
    print('The nearest value is')
    print(Tools.obtainZWorkValues(B,z))
