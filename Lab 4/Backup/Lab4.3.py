# Tilda Lab 4 - David Samuelsson - CMETE2 - 2014-02-10 - Hittar snabbast vägen från FAN till GUD


from Bintree import *
from LinkedQ import *
import sys, os


class ParentNode:
   def __init__(self, word, parent = None):
      self.word = word
      self.parent = parent
         

def läsinsvenska():                           #Läser in svensk textfil och returnerar binärt sökträd för orden
   svenska = Bintree()
   with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
       for rad in svenskfil:
           ordet = rad.strip()                # Ett trebokstavsord per rad
           if svenska.exists(ordet):
              None
           else:
               svenska.put(ordet)             # in i sökträdet
               
   return svenska


def skapaträd():                             #Lite larvig men utgick från lab3 
   träd = Bintree()
   
   return träd


def görabarn(nod, slutord, ordlistan, dumbarnen, q):          #Skapar nya ord genom att byta ut en bokstav i nodens ord

   alfabetet='abcdefghijklmnopqrstuvwxyzåäö'
   

   for i in range(len(alfabetet)):                           #Tre fall för 1a, 2a, 3e bokstaven i ordet. Hade kunnat göra två loopar                      
      
      ordförsök=alfabetet[i:i+1]+nod.word[1:3]
      kontrollerabarn(ordförsök, nod, slutord, ordlistan, dumbarnen, q)
         
      ordförsök=nod.word[0:1]+alfabetet[i:i+1]+nod.word[2:3]
      kontrollerabarn(ordförsök, nod, slutord, ordlistan, dumbarnen, q)
         
      ordförsök=nod.word[0:2]+alfabetet[i:i+1]
      kontrollerabarn(ordförsök, nod, slutord, ordlistan, dumbarnen, q)



def kontrollerabarn(ordförsök,nod,slutord,ordlistan, dumbarnen, q):         #Kontrollerar om ordförsök är ett riktigt ord och om vi nått slutordet
   
   if ordlistan.exists(ordförsök) and not dumbarnen.exists(ordförsök):
      dumbarnen.put(ordförsök)
      q.put(ParentNode(ordförsök,nod))
      
   if ordförsök == slutord:
      print('Det finns en väg till', slutord)
      print('\n'+slutord)
      writechain(nod)                   
      sys.exit(0)              
   


def writechain(child):                   #skriver ut hela ordkejdan från slutord till startord
   
   while child.parent!=None:
      print(child.word)
      return writechain(child.parent)    #Förstår inte riktigt varför det måste vara return. Fast kolla lite på rekursiva varianten av kontrollerainput.
   
   print(child.word)                     #skriver ut sista ordet/startordet


def kontrollerainput(ordet):            #Kollar att ordet är trestavigt och består av bokstäver
   status=False
   
   while status == False:
      if ordet.isalpha() and len(ordet)==3:
         return ordet
      else:
         ordet=input('\nKontrollera att du har angivet ett trestavigt ord. Försök igen: ').lower().strip()


###                                         Finns det någon nackdel med att göra det rekursivt som nedan?
##
##   if ordet.isalpha() and len(ordet)==3:
##      return ordet
##   
##   else:
##      ordet=input('\nKontrollera att du har angivet ett trestavigt ord. Försök igen: ')
##      return kontrollerainput(ordet)        #Skriver jag inte return här så returneras bara none till ursprungsanropet och detta anrop försvinner ut i ingenstans..


   


def huvudprogram():                    #Letar upp snabbaste ordkedjan mellan två trestaviga ord

   ordlistan=läsinsvenska()
   dumbarnen=skapaträd()
   q=LinkedQ()

   print('Hej och välkommen till ordprogrammet! \nProgrammet hittar snabbaste vägen mellan två trestaviga ord genom att byta ut en bokstav i taget och skapa andra ord längs vägen.\n')

   startord=input('Vilket ord vill du börja med? ').lower().strip()
   startord=kontrollerainput(startord)

   slutord=input('Vilket ord vill du ta dig till? ').lower().strip()
   slutord=kontrollerainput(slutord)

   dumbarnen.put(startord)                  #hidrar incest. Alltså att fan blir sitt eget barn...
   nod=ParentNode(startord)
   q.put(nod)
   

   try:                                         #Try/except fångar upp sys.exit och dess traceback vid funnet slutord
      while not q.isEmpty():
         nod=q.get()
         görabarn(nod, slutord, ordlistan, dumbarnen, q)
   except SystemExit:
      print('\nProgrammet avslutat')

   if q.isEmpty():
      print('\nTyvärr finns det ingen väg..')

      

huvudprogram()
   
   
