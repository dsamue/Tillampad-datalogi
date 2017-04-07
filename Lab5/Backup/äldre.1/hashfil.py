# Hashtabell baserad på pythons dictionary - Tilda lab5 - David Samulesson - CMETE2

class Hashtabell:
    def __init__(self,size):
        self.hashtabell={}
        self.size=size
        
    def put(self, namn, atomobjekt):
        index=hashfunktion(namn)    
        self.hashtabell[index]=atomobjekt

    def get(self,namn):
        index=hashfunktion(namn)
        return self.hashtabell[index]
        
        
def hashfunktion(namn):
    index=0
    faktor=1
    for bokstav in namn:
        nummer=ord(bokstav)
        x=faktor*nummer
        index+=x
        faktor*=100      
    return index


