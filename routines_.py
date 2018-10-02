#This line returns the line modified with some values
def replaceline(line,letter,value):
    b=''
    for i in line.split():
        if letter in i:
            c=0
            d=1
            for j in letter:
                if j==i[c]:
                   c=c+1
                if c>len(letter):
                   d=0
            if c*d==len(letter):
                rep=letter+str(value)
                b=line.replace(i,rep)
                line=b
    if b!='':
        line=b
    return line
