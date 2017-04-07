# Tilda lab 2 - David Samuelsson Cmete2 - 20140130

from listQFile import ListQ

def trolla(svar):
    lista=svar.split(' ')
    kö=ListQ()
    #kö.lista.extend(lista)    #Det här var väl kanske inte så generellt.. ist for-loop
    
    for i in lista:
        kö.put(i)
        
    while len(kö.lista) >1:
        x=kö.get()
        y=kö.get()

        kö.put(x)
        print(y)
        
    y=kö.get()
    print(y)
  
        

svar=input('I vilken ordning ligger korten? \n')
trolla(svar)

