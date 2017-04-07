# Tilda lab 2 - David Samuelsson Cmete2 - 20140130

from LinkedQ import LinkedQ

def trolla(svar):
    lista=svar.split(' ')
    kö=LinkedQ()
    
    for i in lista:
        kö.put(i)

    s=''
    
    while kö.isEmpty() != True:   # missade paranteser här ger skumt felmeddelande. varför just det?
        x=kö.get()

        if kö.isEmpty():
            #print(x)
            s+= x + ' '

        else:           
            y=kö.get()
            kö.put(x)
            #print(y)
            s+= y + ' '
                    
    print(s)
  

def huvudprogram():
    print('Hej och välkommen till trollkarlsprogrammet!\nDu kan när som helst avsluta genom att trycka "#"')

    svar=input('\nI vilken ordning ligger korten? \n')
    
    while svar != '#':
        trolla(svar)
        svar=input('\nI vilken ordning ligger korten? \n')

    print('\nProgrammet är avslutat') 

huvudprogram()        
