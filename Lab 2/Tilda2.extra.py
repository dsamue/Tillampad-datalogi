# Tilda lab 2 - David Samuelsson - CMETE2 - 20140130

from LinkedStack import LinkedStack
from LinkedQ import LinkedQ


def trolla_tillbaka(svar):   #Bestämmer vilken ordning korten bör ligga i för att komma ut i önskad ordning (Inparameter=sträng med önskad ordning).
    lista=svar.split()    #Lämnar medvetet dessa namn (kö, lista, stack) för att fråga. 2.6 har andra namn.
    stack=LinkedStack()
    kö=LinkedQ()
   
    for i in lista:         #Lägg alla korten i en stack
        stack.push(i)
    
    while stack.isEmpty() != True:    #Ta upp ett kort i taget ur stacken, lägg sist i kön, ta kortet längst fram i kön och lägg sist.
        x=stack.pop()

        kö.put(x)
        y=kö.get()
        kö.put(y)

    while not kö.isEmpty():          #Lägg alla kortet i tom stack.
        x=kö.get()
        stack.push(x)

    print('Korten ska ligga i denna ordning:')
    print(stack)


  

def huvudprogram():
    print('Hej och välkommen till bakvända trollkarlsprogrammet!\nDu kan när som helst avsluta genom att trycka "#"')

    svar=input('\nI vilken ordning vill du att korten ska komma ut? (separera med mellanslag)\n')
    
    while svar != '#':
        trolla_tillbaka(svar)
        svar=input('\nI vilken ordning vill du att korten ska komma ut?\n')

    print('\nProgrammet är avslutat')


def testfall():
    print("Matar in kortföljden 1 2 3 4 5 till funktionen 'trolla_tillbaka()'\n")
    trolla_tillbaka("1 2 3 4 5")
    print("\nDu bör nu ha fått ut följden: 3,1,5,2,4")

    print('--------------------------')

    print("Matar in kortföljden 1    2  3  4   5 till funktionen (alltså med flera mellanslag)'trolla_tillbaka()'\n")
    trolla_tillbaka("1    2  3  4 5")
    print("\nDu bör nu ha fått ut följden: 3,1,5,2,4")


    print('--------------------------')

    print("Matar in kortföljden: 'gillar du mig när jag kramar ' till funktionen (alltså med flera mellanslag)'trolla()'\n")
    trolla_tillbaka("gillar du mig när jag kramar ")
    print("\nDu bör nu ha fått ut följden: 'jag gillar när du kramar mig'")




huvudprogram()        
