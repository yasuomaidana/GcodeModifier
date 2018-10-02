print('Select what you want to do')
print('Modify temperature (1)')
print('Generate Zaxis modifier (2)')
s=int(input('Option :'))
if s==1:
    print('--------------')
    import Tmodifier
    print('---------------')
elif s==2:
    print('------------------')
    import ZaxisModifier
    print('---------------')
else:
    print('Wrong option')
print('End')
