# Tilda lab6 - David Samuelsson CMETE2 - 140325
# Kontrollerar om molekyler i infil är skrivna på rätt form

from LinkedQ import LinkedQ
from sys import stdin
from Hashtabell import *


class Syntaxfel(Exception):
    pass


def readFormel(q,atomhash):   # Måste fråga om detta är rätt tänkt eller om (och hur!) vvi ska använda reguljära uttryck..
    x=q.peek()
    if not x.isalpha() and not x=='(':
        raise Syntaxfel('3Felaktig gruppstart')
    
    readMol(q,atomhash)
    
    if not q.isEmpty:
        readFormel(q,atomhash)  #Eventuellt?
        
    return True    #Kanske egentligen borde skita i alla "True"?

def readMol(q,atomhash):    #Vill bara veta att vi har en eller flera efterföljande grupper
    #ska den jämföra nåt här eller hoppa direkt vidare?
    #print('nu är vi i mol',q.peek())
##    if q.peek()==')':
##        raise Syntaxfel('4Felaktig gruppstart')
    
    while not q.isEmpty():
        if q.peek()==')':
            raise Syntaxfel('1Felaktig gruppstart')
        readGroup(q,atomhash)
    #readGroup(q,atomhash)

    return True

def readGroup(q,atomhash):
    if q.peek().isalpha():
        readAtom(q,atomhash)
        if not q.isEmpty():
            if q.peek().isdigit():
                x=0            #ok, nånstans här ska det alltså dyka upp en siffra även om det bara är en etta..
                while q.peek().isdigit():
                    x+=int(q.get())               
                if x<=1:        #ev. är även 1 ok
                    raise Syntaxfel('För litet tal')
            return True
                    
    if q.peek()=='(':
        q.get()
        readGroup(q,atomhash)
        if q.peek()==')':
            q.get()
            if q.peek().isdigit():                              #kodupprepning från ovan. skapa separat funktion
                x=''
                while q.peek().isdigit():
                    x+=q.get()               
                if int(x)<=1:        #ev. är även 1 ok
                    raise Syntaxfel('För litet tal')
            readMol(q,atomhash)
        else: raise Syntaxfel('Högerparentes saknas')  #?
        return True
    
##    if q.peek()==')':
##        raise Syntaxfel('2Felaktig gruppstart')

##    readMol(q,atomhash)
            
##    else:
##        print(q.peek())
##        raise Syntaxfel('Nån form av gruppfel')
        
    return True

def readAtom(q,atomhash):     #Kanske hade varit bättre att skapat atomhash här, men då skapas den ju varje gång?
    x=q.peek()
    if x.isupper():  #Kolla om vi har en stor bokstav och kolla isåfall om nästa är en liten och plocka då ut den.
        x=q.get()
        if q.peek().islower():
            x+=q.get()
            
        if x==atomhash.get(x):
            return True
        raise Syntaxfel('Okänd atom')
    
    raise Syntaxfel('Saknad stor bokstav')
    
def läsInAtomer():
    atomsträng='H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar'
    atomlista=atomsträng.split()
    atomhash=Hashtabell(18)
    for i in atomlista:
        atomhash.put(i,i)
    return atomhash


def huvudprogram():
    stdin = open("indata.txt") #Lätt att ändra (genom att kommentera bort) för köra fil eller Kattis
    rad = stdin.readline()
    atomhash=läsInAtomer()
    
    while rad[0]!= "#": 
        q = LinkedQ() 
        for tecken in rad:
            q.put(tecken)
        try:
            readFormel(q,atomhash)
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as felet:
            #resten = str(q).strip()      #skapar mellanrum...

            resten=''
            while not q.isEmpty():
                resten+=q.get()
            resten=resten.strip()
            
            print(felet, "vid radslutet", resten)  #'felet' är meddelandet vi skickar med vårt error
        rad = stdin.readline()


huvudprogram()
