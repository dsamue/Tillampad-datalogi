# Tilda lab6 - David Samuelsson CMETE2 - 140325
# Kontrollerar om molekyler i infil är skrivna på rätt form

from LinkedQ import LinkedQ
from sys import stdin


class Syntaxfel(Exception):
    pass


def readFormel(q):   # Måste fråga om detta är rätt tänkt eller om (och hur!) vvi ska använda reguljära uttryck..
    x=q.peek()
    if not x.isalpha() and not x.isupper():   #liten bokstav ska jag nog kolla i atom
        raise Syntaxfel('Felaktig gruppstart')
    
    readMol(q)
    
    if not q.isEmpty:
        readFormel(q)  #Eventuellt?
        
    return True

def readMol(q):
    #ska den jämföra nåt här eller hoppa direkt vidare?
    readGroup(q)

    return True

def readGroup(q):
    return True

    



def huvudprogram():
    stdin = open("indata.txt") #Lätt att ändra (genom att kommentera bort) för köra fil eller Kattis
    rad = stdin.readline()
    
    while rad[0]!= "#": 
        q = LinkedQ()
        for tecken in rad:
            q.put(tecken)
        try:
            readFormel(q)
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as felet:
            #resten = str(q).strip()      #skapar mellanrum...

            resten=''
            while not q.isEmpty():
                resten+=q.get()
                
            print(felet, "vid radslutet", resten)  #'felet' är meddelandet vi skickar med vårt error
        rad = stdin.readline()


huvudprogram()
