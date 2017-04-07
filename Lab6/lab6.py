# Tilda lab6 - David Samuelsson CMETE2 - 140331
# Kontrollerar om molekyler i infil är skrivna på rätt form

from LinkedQ import LinkedQ
from sys import stdin
from Hashtabell import *


class Syntaxfel(Exception):
    pass


def readFormel(q,atomhash):

    x=q.peek()
    if x==None:                                     #Bara för tom rad (även problem med isalpha om tomt)
        raise Syntaxfel('Felaktig gruppstart')
    
    if not x.isalpha() and not x=='(':
        raise Syntaxfel('Felaktig gruppstart')
    
    readMol(q,atomhash)
    
    if not q.isEmpty():
       readFormel(q,atomhash)
           
    return True



def readMol(q,atomhash):                    #Vill bara veta att vi har en eller flera efterföljande grupper
    if not q.isEmpty():
        readGroup(q,atomhash)
    return True



def readGroup(q,atomhash):                  #Kollar om gruppen är korrekt
    if q.peek().isalpha():
        readAtom(q,atomhash)
        readNumber(q,atomhash,'atom')
        return True
                    
    if q.peek()=='(':
        q.get()
        while q.peek()!=')':
            if q.isEmpty(): raise Syntaxfel('Saknad högerparentes')
            readMol(q,atomhash)
        q.get()
        readNumber(q,atomhash,'mol')
        return True       
    return True                             #Bara för att tom parentes ska gå igenom



def readAtom(q,atomhash):                   #Kollar att atombeteckningen är korrekt
    x=q.peek()
    if x.isupper():                         #Kolla om vi har en stor bokstav. Om nästa är en liten plockar vi ut den.
        x=q.get()
        if not q.isEmpty() and q.peek().islower():  
            x+=q.get()           
        if x==atomhash.get(x):              #Om atomen finns
            return True
        raise Syntaxfel('Okänd atom')
    raise Syntaxfel('Saknad stor bokstav')



def readNumber(q,atomhash,typ):              #Kontrollerar om vi har ett giltigt tal efter 'atom' resp. 'mol
    x=''
    if q.peek()=='0':
        q.get()
        raise Syntaxfel('För litet tal')
    
    while not q.isEmpty():
        if q.peek().isdigit():
            x+=(q.get())
        else:
            break
    
    if x !='':
        if int(x)>=2:
            return True
        else: raise Syntaxfel('För litet tal')

                                            #Om det inte stod någon siffra:      
    if typ=='mol':
        raise Syntaxfel('Saknad siffra')
    if typ=='atom':
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
        rad=rad.strip()
        for tecken in rad:
            q.put(tecken)
        try:
            readFormel(q,atomhash)
            print("Formeln är syntaktiskt korrekt")
            
        except Syntaxfel as felet:
            resten=''
            while not q.isEmpty():
                resten+=q.get()
            resten=resten.strip()
            
            print(felet, "vid radslutet", resten)             #'felet' är meddelandet vi skickar med vårt error
        rad = stdin.readline()


huvudprogram()
