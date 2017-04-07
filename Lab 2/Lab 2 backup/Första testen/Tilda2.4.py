# Tilda lab 2 - David Samuelsson Cmete2 - 20140130

from listQFile import ListQ

def trolla(svar):
    lista=svar.split(' ')
    kö=ListQ()
    kö.lista.extend(lista)
    
    while len(kö.lista) >1:
        x=kö.get()
        y=kö.get()

        kö.put(x)
        print(y)
        
    y=kö.get()
    print(y)
  
        

svar=input('I vilken ordning ligger korten? \n')
trolla(svar)

