import routines_ as Routines

###################################################
###################################################
###This method modify a list. To be more specific
###it modifies a list of commands of gcode
###inputs mA List to be modify
###       MCommand Master command that will be afected
###       SCommand Sub command that will be affected
###       Value It is the new value that set up
###Output mA List of command modified
###
###Comments 1. If you sent Value = -0 and SCommand==''
###            it will delete the complete line
###To do, delete an specific subcommand without
###deleting all the line
###################################################
def modify(mA, MCommand, SCommand, Value):
    for i in range(0, len(mA)):
        if MCommand in mA[i]:
            if Value == str(-0) and SCommand =='':
                mA[i] = ''
            else:
                mA[i] = Routines.replaceline(mA[i], SCommand, Value)
    return mA


###################################################
###################################################
###This method replace the lines of a list that contains
###an specific string MCommand for a newLine
###inputs mA List
###       MCommand string
###       newLine string
###Outputs mA List modified
###Comments I don't know why I created this method
###################################################
def replaceLine(mA,MCommand,newLine):
    for i in range(0,len(mA)):
        if MCommand in mA[i]:
            mA[i]=newLine
    return mA

###################################################
###################################################
###This method prints a list from an starting point
###to and end point
###inputs mA list
###       start int
###       end int
###################################################
def printGCodeLines(mA, start, end):
    for i in range(start, end):
        print(mA[i])

###################################################
###################################################
###This class setZ contains a variaty of functions
###that allow us to modify the list of commands
###in order to start from an specific height.
###################################################
class setZ:


    ###################################################
    ###This method search and returns the nearest value
    ###in a list given a reference
    ###inputs mA list
    ###       Value float, this is the reference
    ###Output mA[idx] float, this is the first nearest
    ###                      value
    ###################################################
    def searchNearestValue(mA,Value):
        import numpy as np
        array = np.asanyarray(mA)
        idx=(np.abs(array-Value)).argmin()
        return mA[idx]

    ###################################################
    ###This method search and returns the start point value
    ###(first layer height)
    ###inputs mA list
    ###Output m float, the first layer height
    ###################################################
    def startZ(mA):
        from collections import Counter
        b=[]
        m=0
        for i in mA:
            b.append(round(i-m,2))
            m=i
        m=Counter(b)
        m= m.most_common(1)[0][0]
        return m

    ###################################################
    ###This method search and returns the layers's height
    ###of the gcode
    ###inputs mA list
    ###Output ret list, layer's height
    ###################################################
    def delbefStart(mA):
        ini=False
        ret=[]
        for i in mA:
            if i == setZ.startZ(mA):
                ini=True
            if ini:
                ret.append(i)
        return ret

    ###################################################
    ###This method search and returns value of Z in a string
    ###of a gcode commands line
    ###inputs i string
    ###
    ###Output ret string, the Z's value
    ###################################################
    def obtainZvalue(i):
        ret=''
        for j in i.split():
            if 'Z' in j:
                ret=j.replace('Z','')
        return ret

    ###################################################
    ###This method search and returns a values list of
    ###the Z's values that belongs to movements, without
    ###counting the setting up Z values
    ###input mA list of commands
    ###Output mZ list of Z's values
    ###################################################
    def obtainZWorkValues(mA):
        mZ=[]
        for i in mA:
            if 'Z' in i:
                if ('G28' not in i) and (setZ.obtainZvalue(i)!=''):
                    mZ.append(float(setZ.obtainZvalue(i)))
        return mZ

    ###################################################
    ###This method obtains the value of the Z height given
    ###a layer position
    ###inputs L int, number of layer
    ###       mA list, gcode commands line
    ###Output Z height
    ###################################################
    def Zforlayer(L,mA):
        return (setZ.startZ(setZ.obtainZWorkValues(mA))*L)

    ###################################################
    ###This method set up a new starting point
    ###by removing moving commands of a gcode
    ###it left the commands for configuration
    ###inputs mA list
    ###       Value float, starting point
    ###Output mZ list, this is the modified command lines
    ###################################################
    def ZstartModifier(mA,Value):
        WorkValues=setZ.obtainZWorkValues(mA)
        worksmall=setZ.delbefStart(WorkValues)
        nearPoint=setZ.searchNearestValue(worksmall,Value)
        print('It will start printing from the height :',nearPoint)
        ini=False
        mZ=[]
        c=0
        for i in mA:
            if 'G0' or 'G1' in i:
                if setZ.obtainZvalue(i) !='':
                    if float(setZ.obtainZvalue(i))==nearPoint:
                        ini=True
                if ini:
                    mZ.append(i)
            if not('G0' in i) and not('G1' in i) and not('G2' in i) and not('G3' in i): #Check that part
                mZ.append(i)

        return mZ
###################################################End class setZ

###################################################
###################################################
###This class opens gcodes files, and allows us to
###use in the program
###################################################
class Reader:

    ###################################################
    ###Initialize the class, it gets directory path
    ###################################################
    def __init__(self):
        import os
        self.Dpath = os.getcwd() + '/'
        self.path=''

    ###################################################
    ###This method changes the directory path
    ###inputs newDirectory string
    ###################################################
    def setdirPath(self, newDirectory):
        self.Dpath = newDirectory

    ###################################################
    ###This method reads a file given a path
    ###inputs fulPath string, the FULL path of the file
    ###                       that will be opened
    ####################################################
    def oFullPath(self, fulPath):
        a = open(fulPath, 'r')
        self.path=fulPath
        return a

    ###################################################
    ###This method opens a file in the SAME directory
    ###given at Dpath
    ###inputs file string, the name of the file
    ###################################################
    def oFile(self, file):
        a = self.Dpath
        fullpath = a + file + '.gcode'
        b = open(fullpath, 'r')
        self.path=fullpath
        return b

    ###################################################
    ###This method check if a gcode file with name "name"
    ###and if it doesn't exist, it could create one if
    ###creates is true. The name of the new file will be the same
    ###of the existing one
    ###inputs name string, name of the file
    ###       create boolean
    ###################################################
    def checksE(self,name,create):
        import os.path
        fullpath=self.Dpath+name+'.gcode'
        if os.path.isfile(fullpath):
           r=self.oFile(name)
        else:
            if create:
               open(fullpath,'w')
               r=self.oFile(name)
            else:
                print('The file does not exist')
        return r

    ###################################################
    ###This method allows us to select what kind of reading
    ###we want, the ones with that needs the full path or the
    ###other one
    ###inputs s int
    ###       p string
    ###################################################
    def QuickReader(self,s,p):
        if s==1:
            Read=self.oFile(p)
        if s==2:
            Read=self.oFullPath(p)
        b=Read.readlines()
        Read.close()
        return b
###################################################End class Reader

###################################################
###################################################
###This class creates gcode files
###################################################
class Writer:
    ###################################################
    ###This is the initialize method, it gets the directory path
    ###################################################
    def __init__(self):
        import os
        self.Dpath = os.getcwd() + '/'

    ###################################################
    ###This method changes the directory path
    ###inputs newDirectory string
    ###################################################
    def setdirPath(self, newDirectory):
        self.Dpath = newDirectory

    ###################################################
    ###This method creates and writes a gcode file given
    ###the full path
    ###inputs fulPathName string
    ###       gcode list, this is the gcode commands list
    ###################################################
    def wFullPath(self, fulPathName,gcode):
        self.Writer=open(fulPathName, 'w')
        self.writeRoutine(gcode)
        self.endF()

    ###################################################
    ###This method creates and writes a gcode file in
    ###the directory path
    ###inputs fileName string
    ###       gcode list, this is the gcode commands list
    ###################################################
    def wFile(self, fileName,gcode):
        a = self.Dpath
        fullpath = a + fileName + '.gcode'
        self.Writer=open(fullpath, 'w')
        self.writeRoutine(gcode)
        self.endF()

    ###################################################
    ###This method rewrites the file
    ###inputs mA list, this is the gcode commands list
    ###       remove string, name of the file to be rewrited
    ###################################################
    def reWrite(self,mA,remove):
        import os
        remove=remove+'.gcode'
        os.remove(remove)
        self.Writer=open(remove,'w')
        self.writeRoutine(mA)
        self.endF()

    ###################################################
    ###This method closes the file created allowing us to get it
    ###in a safe way
    ###################################################
    def endF(self):
        self.Writer.close()

    ###################################################
    ###This method writes in the file
    ###inputs mA list
    ###################################################
    def writeRoutine(self,mA):
        self.Writer.writelines(mA)

    ###################################################
    ###This method writes per line in the file
    ###input mA list
    ###      path string
    ###################################################
    def writePerLine(self,mA,path):
        self.Writer=open(path,'w')
        for i in mA:
            self.Writer.writelines("%s\n" %i)
        self.endF()

    ###################################################
    ###This method allows us to select what kind of writing option
    ###we want, the ones with that needs the full path, create another
    ###file or rewrite
    ###inputs o int
    ###       B list
    ###       p string
    ###################################################
    def QuickWriter(self,o,B,p):
        if o==1:
            self.reWrite(B,p)
        elif o==2:
            name=input("Put the name of the file :")
            self.wFile(name,B)
        elif o==100:
            print('Put the pat of the new file it can be new or one used')
            name=input('Path :')
            self.wFullPath(name,B)
        else:
            print('You selected an invalid option')
            print('For this reason you were send')
            print('to the easy manual option')
            print('please name the output file')
            name=input('File name :')
            self.wFile(name,B)
###################################################End class Writer
