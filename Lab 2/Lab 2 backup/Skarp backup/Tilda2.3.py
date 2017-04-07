# Tilda lab 2 - David Samuelsson Cmete2 - 20140130


class ListQ:                        #Skapar ett kö-objekt
    def __init__(self):
        self.lista=[]

    def put(self, x):               # Lägger till x i kön
        self.lista.append(x)

    def get(self):                  # Returnerar objektet som är längst fram i kön
        return self.lista.pop(0)

    def isEmpty(self):              # Returnerar True om kön är tom, annars False
        return len(self.lista)==0



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
