# Tilda Lab 4 - David Samuelsson - CMETE2 - 2014-02-10 - Hittar en väg från FAN till GUD


from Bintree import *
from LinkedStack import *
from LinkedQ import *
import sys, os


class ParentNode:
   def __init__(self, word, parent = None):
      self.word = word
      self.parent = parent

class Rekordnod:

   def __init__(self,nod,längd=None):
      self.nod=nod
      self.längd=längd
         

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


def görabarn(nod, slutord, ordlistan, dumbarnen, stack, rekord):          #Skapar nya ord genom att byta ut en bokstav i nodens ord

   alfabetet='abcdefghijklmnopqrstuvwxyzåäö'
   

   for i in range(len(alfabetet)):                           #Tre fall för 1a, 2a, 3e bokstaven i ordet. Hade kunnat göra två loopar                      
      
      ordförsök=alfabetet[i:i+1]+nod.word[1:3]
      kontrollerabarn(ordförsök, nod, slutord, ordlistan, dumbarnen, stack,rekord)
         
      ordförsök=nod.word[0:1]+alfabetet[i:i+1]+nod.word[2:3]
      kontrollerabarn(ordförsök, nod, slutord, ordlistan, dumbarnen, stack,rekord)
         
      ordförsök=nod.word[0:2]+alfabetet[i:i+1]
      kontrollerabarn(ordförsök, nod, slutord, ordlistan, dumbarnen, stack,rekord)



def kontrollerabarn(ordförsök,nod,slutord,ordlistan, dumbarnen, stack,rekord):         #Kontrollerar om ordförsök är ett riktigt ord och om vi nått slutordet
   
   if ordlistan.exists(ordförsök) and not dumbarnen.exists(ordförsök):
      dumbarnen.put(ordförsök)
      stack.push(ParentNode(ordförsök,nod))
      
   if ordförsök == slutord:
      print('Det finns en väg till', slutord)
      print('\n'+slutord)
      längd=countchain(nod)
      rekord[längd]=nod
                   
   

def countchain(nod):
   if nod.parent!=None:
      return countchain(nod.parent)+1
   return +1
   
   

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




def huvudprogram():                    #Letar en ordkedja mellan två trestaviga ord (djupet först)

   ordlistan=läsinsvenska()
   dumbarnen=skapaträd()
   stack=LinkedStack()
   rekord={}

   print('Hej och välkommen till ordprogrammet! \nProgrammet hittar en väg mellan två trestaviga ord genom att byta ut en bokstav i taget och skapa andra ord längs vägen.\n')

   startord=input('Vilket ord vill du börja med? ').lower().strip()
   startord=kontrollerainput(startord)

   slutord=input('Vilket ord vill du ta dig till? ').lower().strip()
   slutord=kontrollerainput(slutord)

   dumbarnen.put(startord)                  #hidrar incest. Alltså att fan blir sitt eget barn...
   nod=ParentNode(startord)
   stack.push(nod)
   

   try:                                         #Try/except fångar upp sys.exit och dess traceback vid funnet slutord
      while not stack.isEmpty():
         nod=stack.pop()
         görabarn(nod, slutord, ordlistan, dumbarnen, stack,rekord)
   except SystemExit:
      print('\nProgrammet avslutat')

   if stack.isEmpty():
      ##print('\nTyvärr finns det ingen väg..')
      index=min(rekord)
      print('Den kortaste vägen')
      writechain(rekord[index])

      

huvudprogram()

''' Tänkte lite knasigt. den är utgår från djupetförst vilket blir fel och dessutom tänkte jag inte på att man skulle köra igenom ett gäng olika startord.
denna kod letar istället hittar istället längst väg mellan startord och slutord'''
   
