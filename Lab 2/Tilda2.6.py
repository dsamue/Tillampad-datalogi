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




def testfall():
    print("Matar in kortföljden 3 1 5 2 4 till funktionen 'trolla()'\n")
    trolla("3 1 5 2 4")
    print("\nDu bör nu ha fått ut följden: 1,2,3,4,5.")

    print('--------------------------')

    print("Matar in kortföljden 3     1   5  2  4 till funktionen (alltså med flera mellanslag)'trolla()'\n")
    trolla("3     1   5  2  4 ")
    print("\nDu bör nu ha fått ut följden: 1,2,3,4,5.")


    print('--------------------------')

    print("Matar in kortföljden: 'jag gillar när du kramar mig' till funktionen (alltså med flera mellanslag)'trolla()'\n")
    trolla("jag gillar när du kramar mig")
    print("\nDu bör nu ha fått ut följden: 'gillar du mig när jag kramar'")

    

huvudprogram()        
