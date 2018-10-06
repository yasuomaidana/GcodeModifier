from utilery import Reader
from utilery import Writer
from utilery import setZ
###############################################################################
#####This is the menu of this section
R=Reader()
print('You are in easy mode gCode set Z axis modifier')
print('In order to use the easy mode, please put your files in the same carpet of the program')
print('To use it in easy mode please put your gCodes files in the same carpet of the program')
print('However, if you want to put all the path name please choose manual mode')
print('easy mode(1) manual mode(2) ')
s=int(input('Select: '))
s=1
sw=0
print('------------------')
if s==1:
    print('Easy Mode')
    print('Insert the name of your file')
    p=input('(without .gcode) :')
    print('-----------------------')
    print('Do you want to replace the file(1) or make a new one(2)')
    o=int(input('Option :'))
elif s==2:
    print('Manual mode')
    print('Insert the path of your file, please be sure of ')
    p=input('put all the information')
    p=p.replace('\\','/')
    o=100
else:
    print('Please choose a valid option')
    s=3
print('--------------')
################################################## here ends the menu

#### Here start the modifying part
if s!=3:

    R=Reader()
    W=Writer()
    #It creates a list of the commands
    B=R.QuickReader(s,p)
    s=int(input('Start from an specific layer (1) or high (2) :'))
    if s==2:
        z=float(input('Enter the Z start value :'))
    elif s==1:
        #It obtain the height of the layer that you select
        z=setZ.Zforlayer(float(input('From what layer do you want to start :')),B)
    #It modify the list, removing G0 and G1 instructions before the start point
    B=setZ.ZstartModifier(B,z)
    #It writes the file
    W.QuickWriter(o,B,p)
