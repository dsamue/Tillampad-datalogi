# Tilda lab 2 - David Samuelsson Cmete2 - 20140130

from listQFile import ListQ

def trolla(svar):        #Simulerar ett korttrick där första kortet läggs längst ned i högen, nästa läggs ut osv. Inparameter är en stäng, korten som läggs ut printas
    lista=svar.split()     #Lista och kö borde kanske heta korten och korthög eller liknande
    kö=ListQ()                 
    
    for i in lista:            #Lägger alla korten i en kö
        kö.put(i)
        
    while len(kö.lista) >1:    #Lägger ett kort sist i kön och lägger ut ett tills endast ett kort är kvar
        x=kö.get()
        y=kö.get()

        kö.put(x)
        print(y)
        
    y=kö.get()                 #Skriver ut sista kortet
    print(y)



def huvudprogram():
    print('Hej och välkommen till trollkarlsprogrammet!\nDu kan när som helst avsluta genom att trycka "#"')

    svar=input('\nI vilken ordning ligger korten? (separera med mellanslag) \n')
    print('Korten kommer att komma ut i denna ordning:')
    
    while svar != '#':
        trolla(svar)
        svar=input('\nI vilken ordning ligger korten? \n')
        print('Korten kommer att komma ut i denna ordning:')

    print('\nProgrammet är avslutat')

    

huvudprogram() 
          
