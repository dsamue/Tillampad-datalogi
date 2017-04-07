# Tilda lab6 - David Samuelsson CMETE2 - 140331
# Kontrollerar om molekyler i infil är skrivna på rätt form

from LinkedQ import LinkedQ
from Hashtabell import *
import molgrafik

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
    while not q.isEmpty() and q.peek()!=')':
        mol=readGroup(q,atomhash)
    return True



def readGroup(q,atomhash):                  #Kollar om gruppen är korrekt
    rutan=Ruta()
    if q.peek().isalpha():
        rutan.self.atom=readAtom(q,atomhash)
        rutan.self.num=readNumber(q,atomhash,'atom')
        return True

    if q.peek()=='(':
        q.get()
        rutan.down=readMol(q,atomhash)
        if q.isEmpty(): raise Syntaxfel('Saknad högerparentes')
        if q.peek()!=')': raise Syntaxfel('Saknad högerparentes')  #Kanske något onödig
        q.get()
        rutan.self.num=readNumber(q,atomhash,'mol')
        return rutan # Något osäkert. returnerar iaf tomma parentesrutan vilket verkat vettigt
    
    if q.peek()==')': return True   #fixar rekursionsupphopp
    
    return rutan 



def readAtom(q,atomhash):                   #Kollar att atombeteckningen är korrekt
    x=q.peek()
    if x.isupper():                         #Kolla om vi har en stor bokstav. Om nästa är en liten plockar vi ut den.
        x=q.get()
        if not q.isEmpty() and q.peek().islower():  
            x+=q.get()           
        if x==atomhash.get(x):              #Om atomen finns
            return x
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
            return int(x)
        else: raise Syntaxfel('För litet tal')

                                            #Om det inte stod någon siffra:      
    if typ=='mol':
        raise Syntaxfel('Saknad siffra')
    if typ=='atom':
        return 1
    
    

    
def läsInAtomer():
    atomsträng='H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar'
    atomlista=atomsträng.split()
    atomhash=Hashtabell(18)
    for i in atomlista:
        atomhash.put(i,i)
    return atomhash

    


def huvudprogram():
    atomhash=läsInAtomer()
    print('Välkommen till Molekylprogrammet!\nDu kan när som helst avsluta genom att mata in "#".\n')
    rad=input('Mata in Molekylformeln: ')
    
    while rad!= "#":
        mg=molgrafik()
        q = LinkedQ()
        rad=rad.strip()
        for tecken in rad:
            q.put(tecken)
        try:
            mol=readFormel(q,atomhash)
            print("Formeln är syntaktiskt korrekt",'\n')
            mg.show(mol)
            
        except Syntaxfel as felet:
            resten=''
            while not q.isEmpty():
                resten+=q.get()
            resten=resten.strip()
            
            print(felet, "vid radslutet", resten,'\n')             #'felet' är meddelandet vi skickar med vårt error
        rad=input('Mata in Molekylformeln: ')
        


huvudprogram()
