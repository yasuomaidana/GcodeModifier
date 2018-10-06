#This line returns the line modified with some values
def replaceline(line,letter,value):
    b=''
    #It "read" every word in the line
    for i in line.split():
        if letter in i:
            c=0
            d=1
            #It checks that select the correct "word" in the string
            #comparing each charachter of the "letter" with the "word" selected
            for j in letter:
                if j==i[c]:
                    c=c+1
                if c>len(letter):
                    d=0
                if c>len(i):
                    c=0

            if c*d==len(letter):
                rep=letter+str(value)
                #Replace the line by changing the "word" by rep
                b=line.replace(i,rep)
                line=b
    #I'm not sure why i put this here, but for the moments works, so I won't modify it.
    if b!='':
        line=b
    return line
