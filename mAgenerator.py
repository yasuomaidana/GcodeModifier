class mPrint():
    def __init__(self,t='',fr='',l=''):
        self.mA=[]
        self.mA.append(';FLAVOR:RepRap')
        self.mA.append(';TIME:'+t)
        self.mA.append(';Filament used: '+l)
        self.mA.append(';Layer height: '+l)
        self.mA.append(';Generated with Yasuo''s' 'Hand')
        self.mA.append('G21        ;metric values')
        self.mA.append('G90        ;absolute positioning')
        self.mA.append('M82        ;set extruder to absolute mode')
        self.mA.append('M107       ;start with the fan off')
        self.mA.append('M302')
        self.mA.append('M92 E2000')
        self.mA.append(';G28 X0 Y0  ;move X/Y to min endstops')
        self.mA.append(';G28 Z0     ;move Z to min endstops')
        self.mA.append(';G1 Z15.0 F9000 ;move the platform down 15mm')
        self.mA.append('G92 E0                  ;zero the extruded length')
        self.mA.append('G1 F200 E3              ;extrude 3mm of feed stock')
        self.mA.append('G92 E0                  ;zero the extruded length again')
        self.mA.append('G1 F9000')
        self.mA.append('M117 Printing...')
        self.mA.append('M107')
        self.mA.append(';it starts here')
        self.mA.append('G1 F'+fr)
        self.mA.append('G1 E'+l)
    def moveZaxis(self,fr,l):
        import utilery as Tools
        time=str(float(fr)/float(l))
        M=[]
        M.append(';TIME:')
        M.append(';Filament used:')
        M.append(';Layer height: ')
        c=0
        for i in M:
            if c==0:
                v=time
            else:
                if float(l)/100<.3:
                   v=l
                else:
                    v='.3'
            self.mA=Tools.replaceLine(self.mA,i,i+v)
            c=c+1
        self.mA=Tools.modify(self.mA,'M92','E','1000')
        self.mA=Tools.modify(self.mA,'G1','F',fr)
        self.mA=Tools.modify(self.mA,'G1','E',l)
