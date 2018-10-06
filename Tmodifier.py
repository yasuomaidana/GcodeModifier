import utilery as Utilery
from utilery import Reader
from utilery import Writer

###############################################################################
#####This is the menu of this section
print('You are in easy mode gCode temperature modifier')
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
    p=input('(without .gcode) :')
    t=input('Insert the new temperature if you want disable heaters please insert 0 :')
    print('-----------------------')
    print('Do you want to replace the file(1) or make a new one(2)')
    o=int(input('Option :'))
elif s==2:
    print('Manual mode')
    print('Insert the path of your file, please be sure of ')
    p=input('put all the information')
    p=p.replace('\\','/')
    t=input('Insert the new temperature if you want disable heaters please insert -0 :')
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
    S=''
    if t!=str(-0):
        S='S'
    #This function modify the given instructions
    B=Utilery.modify(B,'M109',S,t)
    B=Utilery.modify(B,'M104',S,t)
    B=Utilery.modify(B,'M140',S,t)
    B=Utilery.modify(B,'M190',S,t)

    #It writes the new file
    W.QuickWriter(o,B,p)

