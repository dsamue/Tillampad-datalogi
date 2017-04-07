# Tilda lab6 - David Samuelsson CMETE2 - 140331
# Kontrollerar om molekyler i infil är skrivna på rätt form

from LinkedQ import LinkedQ
from Hashtabell import *
from molgrafik import *
from Compare import *

class Syntaxfel(Exception):
    pass


def readFormel(q,atomhash):

    x=q.peek()
    if x==None or x==')':                                     #Bara för tom rad
        raise Syntaxfel('Felaktig gruppstart')
    
    mol=readMol(q,atomhash)
    
    if not q.isEmpty():
       readFormel(q,atomhash)
           
    return mol


def readMol(q,atomhash):                    #Vill bara veta att vi har en eller flera efterföljande grupper
    x=q.peek()
    
    if x==None:                                     #Bara för tom rad (även problem med isalpha om tomt)
        raise Syntaxfel('Felaktig gruppstart')
    if not isLet(x) and not x=='(' and not x==')':
        raise Syntaxfel('Felaktig gruppstart')
    
    mol=readGroup(q,atomhash)
    
    if not q.isEmpty() and q.peek()!=')':
        mol.next=readMol(q,atomhash)
        return mol
    return mol



def readGroup(q,atomhash):                  #Kollar om gruppen är korrekt
    rutan=Ruta()
    if isLet(q.peek()):
        rutan.atom=readAtom(q,atomhash)
        rutan.num=readNumber(q,atomhash,'atom')
        return rutan

    if q.peek()=='(':
        q.get()
        rutan.down=readMol(q,atomhash)
        if q.isEmpty(): raise Syntaxfel('Saknad högerparentes')
        if q.peek()!=')': raise Syntaxfel('Saknad högerparentes')  #Kanske något onödig
        q.get()
        rutan.num=readNumber(q,atomhash,'mol')
        return rutan # Något osäkert. returnerar iaf tomma parentesrutan vilket verkat vettigt
    
    if q.peek()==')': return rutan   #fixar rekursionsupphopp
    
    return rutan 



def readAtom(q,atomhash):                   #Kollar att atombeteckningen är korrekt
    x=q.peek()
    if x.isupper():                         #Kolla om vi har en stor bokstav. Om nästa är en liten plockar vi ut den.
        x=q.get()
        if not q.isEmpty():
            if q.peek().islower():  
                x+=q.get()           
        if atomhash.get(x)!=None:              #Om atomen finns
            return x
        raise Syntaxfel('Okänd atom')
    raise Syntaxfel('Saknad stor bokstav')



def readNumber(q,atomhash,typ):              #Kontrollerar om vi har ett giltigt tal efter 'atom' resp. 'mol
    x=''
    if q.peek()=='0':
        q.get()
        raise Syntaxfel('För litet tal')
    
    while not q.isEmpty():
        if isNum(q.peek()):
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
    atomsträng='H-1.008 He-4.003 Li-6.941 Be-9.012 B-10.81 C-12.01 N-14.01 O-16.00 F-19.00 Ne-20.18 Na-22.99 Mg-24.31 Al-26.98 Si-28.09 P-30.97 S-32.01 Cl-35.45 Ar-39.95'
    atomlista=atomsträng.split()
    atomhash=Hashtabell(18)
    for i in atomlista:
        atom=i.split('-')
        namn=atom[0]
        vikt=float(atom[1])
        atomhash.put(namn,vikt)
    return atomhash




def weight(mol,atomhash):
    if mol.down==None:
        if mol.next!=None:
            return weight(mol.next,atomhash) + (atomhash.get(mol.atom)*mol.num)
        else:
            if not mol.atom=='()':
                return atomhash.get(mol.atom)*mol.num
            else: return 0
    else:
        if mol.next!=None:
            return weight(mol.down,atomhash)*mol.num + weight(mol.next,atomhash)
        else:
            return weight(mol.down,atomhash)*mol.num

    


def huvudprogram():
    atomhash=läsInAtomer()
    print('Välkommen till Molekylprogrammet!\nDu kan när som helst avsluta genom att mata in "#".\n')
    rad=input('Mata in Molekylformeln: ')
    
    while rad!= "#":
        mg=Molgrafik()
        q = LinkedQ()
        rad=rad.strip()
        for tecken in rad:
            q.put(tecken)
        try:
            mol=readFormel(q,atomhash)
            print("Formeln är syntaktiskt korrekt")
            vikt=0
            vikt+=weight(mol,atomhash)
            print('Molekylmassa:',str(round(vikt,2))+'u''\n')
            mol.atom='hejhej'
            mg.show(mol)
            
        except Syntaxfel as felet:
            resten=''
            while not q.isEmpty():
                resten+=q.get()
            resten=resten.strip()
            
            print(felet, "vid radslutet", resten,'\n')             #'felet' är meddelandet vi skickar med vårt error
        rad=input('Mata in Molekylformeln: ')
        


huvudprogram()
