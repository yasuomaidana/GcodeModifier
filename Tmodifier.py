import utilery as Utilery
from utilery import Reader
from utilery import Writer

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
    t=input('Insert the new temperature if you want disable heaters please insert 0 :')
    o=100
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
    S=''
    if t!=str(0):
        S='S'
    B=Utilery.modify(B,'M109',S,t)
    B=Utilery.modify(B,'M104',S,t)
    B=Utilery.modify(B,'M140',S,t)
    B=Utilery.modify(B,'M190',S,t)
    Read.close()
    if o==1:
        W.reWrite(B,R.path)
    elif o==2:
        name=input('Put the name of the file :')
        W.wFile(name,B)
    elif o==100:
        print('Put the pat of the new file it can be new or one used')
        name=input('Path :')
        W.wFullPath(name,B)
    else:
        print('You selected an invalid option')
        print('For this reason you were send')
        print('to the easy manual option')
        print('please name the output file')
        name=input('File name :')
        W.wFile(name,B)

