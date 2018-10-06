#Main program it calls all the function needed

print('Select what you want to do')
print('Modify temperature (1)')
print('Start printing from an especific high or layer (2)')
print('Generate Zaxis movement (3)')
s=int(input('Option :'))
if s==1:
    print('--------------')
    import Tmodifier
    print('---------------')
elif s==2:
    print('------------------')
    import setZaxis
    print('---------------')
elif s==3:
    print('------------------')
    import ZaxisModifier
    print('---------------')
else:
    print('Wrong option')
print('End')
