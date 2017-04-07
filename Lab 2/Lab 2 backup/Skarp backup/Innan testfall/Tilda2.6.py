# Tilda lab 2 - David Samuelsson Cmete2 - 20140130

from LinkedQ import LinkedQ

def trolla(svar):           #Simulerar ett korttrick där första kortet i en hög läggs underst och nästa läggs ut osv. Utlagd ordning skrivs ut i stängen s. Inparameter är en sträng med korten i ordning. 
    korten=svar.split()
    korthög=LinkedQ()
    
    for i in korten:
        korthög.put(i)     #Alla korten läggs i en kö

    s=''
    
    while korthög.isEmpty() != True:
        x=korthög.get()             #Ta översta kortet

        if korthög.isEmpty():       #Lägg ut (i stängen s) om det var det sista
            s+= x + ' '

        else:                       #Annars läggs det underst och nästa läggs ut
            y=korthög.get()
            korthög.put(x)
            s+= y + ' '
                    
    print('Korten kommer att komma ut i denna ordning:\n' + s)   
  

def huvudprogram():
    print('Hej och välkommen till trollkarlsprogrammet!\nDu kan när som helst avsluta genom att trycka "#"')

    svar=input('\nI vilken ordning ligger korten? (separera med mellanslag) \n')
    
    while svar != '#':
        trolla(svar)
        svar=input('\nI vilken ordning ligger korten? \n')

    print('\nProgrammet är avslutat') 

huvudprogram()        
