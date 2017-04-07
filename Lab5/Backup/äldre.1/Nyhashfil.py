# Hashtabell - Tilda lab5 - David Samulesson - CMETE2

class Hashtabell:
    def __init__(self,antal=0):
        self.size=2*antal
        self.hashtabell=[None]*self.size  #Skapar tom lista dubbel så stor som 'size'
        
    def gelista(self):
        return self.hashtabell
    
    def put(self, namn, atomobjekt):
        index=hashfunktion(namn)%self.size
        
        if self.hashtabell[index]==None:    #...om tomt
            self.hashtabell[index]=Node(index,atomobjekt)
        else:                               #Alternativt vid krock
            nod=self.hashtabell[index]
            while nod.next!=None:
                nod=nod.next
            #När nod.next väl är lika med None...
            nod.next=Node(index,atomobjekt)               
            #...så skapar vi ny nod där

    def get(self,namn):
        index=hashfunktion(namn)%self.size
        try:
            if self.hashtabell[index].data.namn==namn:
                return self.hashtabell[index].data
            else:
                nod=self.hashtabell[index]
                while nod.data.namn!=namn:
                    
                    nod=nod.next
                    if nod==None:
                        raise KeyError
   
                return nod.data
            
        except AttributeError:      #Om man råkar hamna på ett None-index..
            raise KeyError  

class Node:
    def __init__(self,key,data,next=None):
        self.key=key
        self.data=data
        self.next=next    #ändrade från None till next..
           
        
def hashfunktion(namn):
    index=0
    faktor=1
    for bokstav in namn:
        nummer=ord(bokstav)
        x=faktor*nummer
        index+=x
        faktor*=100      
    return index


