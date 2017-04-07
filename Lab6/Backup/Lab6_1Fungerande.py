# Tilda lab6 - David Samuelsson CMETE2 - 140325
# Kontrollerar om molekyler i infil är skrivna på rätt form

from LinkedQ import LinkedQ
from sys import stdin
from Hashtabell import *


class Syntaxfel(Exception):
    pass


def readFormel(q,atomhash):             # Måste fråga om detta är rätt tänkt eller om (och hur!) vvi ska använda reguljära uttryck..

    x=q.peek()
    if x==None:                         #Bara för tom rad. Oklart om det ska vara så eller syntaktiskt korrekt. bara ta bort dessa två rader isf. 
        raise Syntaxfel('Felaktig gruppstart')
    if not x.isalpha() and not x=='(':
        raise Syntaxfel('Felaktig gruppstart')
    
    readMol(q,atomhash)
    
    if not q.isEmpty():
       readFormel(q,atomhash)
           
    return True

def readMol(q,atomhash):    #Vill bara veta att vi har en eller flera efterföljande grupper
##    if q.peek()==')':
##        q.get()
##        readMolNumber(q,atomhash)
##        return True
    if not q.isEmpty():
        readGroup(q,atomhash)
    return True

def readGroup(q,atomhash):
    if q.peek().isalpha():
        readAtom(q,atomhash)
        readAtomNumber(q,atomhash)
        return True
                    
    if q.peek()=='(':
        q.get()
        while q.peek()!=')':
            if q.isEmpty(): raise Syntaxfel('Saknad högerparentes')
            readMol(q,atomhash)
        q.get()
        readMolNumber(q,atomhash)
        return True
        
##        if q.peek()==')':
##            q.get()
##            readMolNumber()
            
       
    return True

def readAtom(q,atomhash):     #Kanske hade varit bättre att skapat atomhash här, men då skapas den ju varje gång?
    x=q.peek()
    if x.isupper():  #Kolla om vi har en stor bokstav och kolla isåfall om nästa är en liten och plocka då ut den.
        x=q.get()
        if not q.isEmpty() and q.peek().islower():  
            x+=q.get()
            
        if x==atomhash.get(x):
            return True
        raise Syntaxfel('Okänd atom')
    
    raise Syntaxfel('Saknad stor bokstav')

def readMolNumber(q, atomhash):
    x=''    #iom att jag inte sägger x='' och plussar stängar blir det ok att skriva Na00001. kan ju diskuteras om det är rätt.
    if q.peek()=='0':
        q.get()
        raise Syntaxfel('För litet tal')
    
    while not q.isEmpty():
        if q.peek().isdigit():
            x+=(q.get())           #ok, nånstans här ska det alltså dyka upp en siffra även om det bara är en etta..
        else:
            break
    
    if x !='':        #behövs för H1C
        if int(x)>=2:
            return True
        else: raise Syntaxfel('För litet tal')
          
    raise Syntaxfel('Saknad siffra')
    
    

def readAtomNumber(q, atomhash):
    x=''    #iom att jag inte sägger x='' och plussar stängar blir det ok att skriva Na00001. kan ju diskuteras om det är rätt.
    if q.peek()=='0':
        q.get()
        raise Syntaxfel('För litet tal')
    
    while not q.isEmpty():
        if q.peek().isdigit():
            x+=(q.get())           #ok, nånstans här ska det alltså dyka upp en siffra även om det bara är en etta..
        else:
            break
    
    if x !='':        #behövs för H1C
        if int(x)>=2:
            return True
        else: raise Syntaxfel('För litet tal')
          
    return True
    
def läsInAtomer():
    atomsträng='H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar'
    atomlista=atomsträng.split()
    atomhash=Hashtabell(18)
    for i in atomlista:
        atomhash.put(i,i)
    return atomhash

    


def huvudprogram():
    #stdin = open("/Users/David/Desktop/Tilda/Lab6/indata.txt") #Lätt att ändra (genom att kommentera bort) för köra fil eller Kattis
    rad = stdin.readline()
    atomhash=läsInAtomer()
    
    while rad[0]!= "#": 
        q = LinkedQ()
        rad=rad.strip()       #denna behövdes inte tidigare så känns lite oklart. Hade problem med \n nån vända.
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
