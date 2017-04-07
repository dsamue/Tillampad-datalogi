# Tilda lab 2 - David Samuelsson Cmete2 - 20140130

from LinkedStack import LinkedStack
from LinkedQ import LinkedQ


def trolla_tillbaka(svar):
    lista=svar.split(' ')
    stack=LinkedStack()
    kö=LinkedQ()
   
    for i in lista:
        stack.push(i)
    
    while stack.isEmpty() != True:
        x=stack.pop()

        kö.put(x)
        y=kö.get()
        kö.put(y)

    while not kö.isEmpty():
        x=kö.get()
        stack.push(x)

    print('Korten ska ligga i denna ordning:')
    print(stack)


  

def huvudprogram():
    print('Hej och välkommen till bakvända trollkarlsprogrammet!\nDu kan när som helst avsluta genom att trycka "#"')

    svar=input('\nI vilken ordning vill du att korten ska komma ut?\n')
    
    while svar != '#':
        trolla_tillbaka(svar)
        svar=input('\nI vilken ordning vill du att korten ska komma ut?\n')

    print('\nProgrammet är avslutat') 

huvudprogram()        
