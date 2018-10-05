import routines_ as Routines


def modify(mA, MCommand, SCommand, Value):
    for i in range(0, len(mA)):
        if MCommand in mA[i]:
            if Value == str(0) and SCommand =='':
                mA[i] = ''
            else:
                mA[i] = Routines.replaceline(mA[i], SCommand, Value)
    return mA

def replaceLine(mA,MCommand,newLine):
    for i in range(0,len(mA)):
        if MCommand in mA[i]:
            mA[i]=newLine
    return mA

def printGCodeLines(mA, start, end):
    for i in range(start, end):
        print(mA[i])

class setZ:
    def searchNearestValue(mA,Value):
        import numpy as np
        array = np.asanyarray(mA)
        idx=(np.abs(array-Value)).argmin()
        return mA[idx]

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

    def delbefStart(mA):
        ini=False
        ret=[]
        for i in mA:
            if i == setZ.startZ(mA):
                ini=True
            if ini:
                ret.append(i)
        return ret

    def obtainZWorkValues(mA):
        mZ=[]
        for i in mA:
            if 'Z' in i:
                if 'G28' not in i:
                    for j in i.split():
                        if 'Z' in j:
                            if j.replace('Z','') != '':
                                mZ.append(float(j.replace('Z','')))
        return mZ

    def newZstartModifier(mA,Value):
        WorkValues=setZ.obtainZWorkValues(mA)
        worksmall=setZ.delbefStart(WorkValues)
        nearPoint=setZ.searchNearestValue(worksmall,Value)
        ini=True
        for i in mA:


class Reader:
    #paths: str

    def __init__(self):
        import os
        self.Dpath = os.getcwd() + '/'
        self.path=''

    def setdirPath(self, newDirectory):
        self.Dpath = newDirectory

    def oFullPath(self, fulPath):
        a = open(fulPath, 'r')
        self.path=fulPath
        return a

    def oFile(self, file):
        a = self.Dpath
        fullpath = a + file + '.gcode'
        b = open(fullpath, 'r')
        self.path=fullpath
        return b

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

class Writer:
    def __init__(self):
        import os
        self.Dpath = os.getcwd() + '/'

    def setdirPath(self, newDirectory):
        self.Dpath = newDirectory

    def wFullPath(self, fulPathName,gcode):
        self.Writer=open(fulPathName, 'w')
        self.writeRoutine(gcode)
        self.endF()

    def wFile(self, fileName,gcode):
        a = self.Dpath
        fullpath = a + fileName + '.gcode'
        self.Writer=open(fullpath, 'w')
        self.writeRoutine(gcode)
        self.endF()

    def reWrite(self,mA,remove):
        import os
        os.remove(remove)
        self.Writer=open(remove,'w')
        self.writeRoutine(mA)
        self.endF()

    def endF(self):
        self.Writer.close()

    def writeRoutine(self,mA):
        self.Writer.writelines(mA)

    def writePerLine(self,mA,path):
        self.Writer=open(path,'w')
        for i in mA:
            self.Writer.writelines("%s\n" %i)
        self.endF()
