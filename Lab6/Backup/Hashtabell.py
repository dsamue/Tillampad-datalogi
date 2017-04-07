# Hashtabell - Tilda lab5 - David Samulesson - CMETE2 - 20140302

class Node:
    def __init__(self,key,data,next=None):
        self.key=key
        self.data=data
        self.next=next


class Hashtabell:
    def __init__(self,number):
        self.size=findbin(2*number)  #hittar 'binär' storlek' på hashtabellen. kostar lite tid
        #self.size=2*number
        self.hashtabell=[None]*self.size  #Skapar tom lista med 'size' antal element
        
    def gelista(self):           #för egen koll bara
        return self.hashtabell
        
    
    def put(self, key, data):
        index=hashfunktion(key)%self.size
        
        if self.hashtabell[index]==None:    #...om tomt
            self.hashtabell[index]=Node(key,data)
        else:                               #...alternativt vid krock
            nod=Node(key, data)
            nod.next=self.hashtabell[index]
            self.hashtabell[index]=nod

    def get(self,key):
        index=hashfunktion(key)%self.size
        try:
            if self.hashtabell[index].key==key:
                return self.hashtabell[index].data
            else:
                nod=self.hashtabell[index]
                while nod.key!=key:
                    nod=nod.next
                    if nod==None:
                        raise KeyError
                return nod.data
            
        except AttributeError:      #Om man råkar hamna på ett None-index redan från start..
            return

           
        
def hashfunktion(namn):
    index=0
    faktor=1
    for bokstav in namn:
        nummer=ord(bokstav)
        x=faktor*nummer
        index+=x
        faktor*=100      #skriv hellre 99 (för att i vissa lägen slippa nollor)
    return index


def findbin(number):
    x=1
    if number<=1:
        s=2*int(input('Ange ett större antal element än 1 för hashtabellen: '))
        return findbin(s)
    while number>x:
        x*=2
    return x
