# Tilda Lab 4 - David Samuelsson - CMETE2 - 2014-02-10 - Hittar snabbast vägen från FAN till GUD


from Bintree import *
from LinkedQ import *
import re

def läsinsvenska():    #Läser in svensk textfil och returnerar binärt sökträd för orden
   svenska = Bintree()
   with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
       for rad in svenskfil:
           ordet = rad.strip()                # Ett trebokstavsord per rad
           if svenska.exists(ordet):
              None
           else:
               svenska.put(ordet)             # in i sökträdet
               
   return svenska


def skapaträd():   #Läser in engelsk textfil och returnerar binärt sökträd samt jämför med annat träd. Gemensamma värden skrivs ut
   engelska = Bintree()

   return engelska


def görabarn(nod, slutord, ordlistan, dumbarnen, q):

   #dumbarnen.put(startord)  #Funkar kanske inte riktigt som tänkt i 4.2
   alfabetet='abcdefghijklmnopqrstuvwxyzåäö'
   

   for i in range(len(alfabetet)):
      
      ordförsök=alfabetet[i:i+1]+nod[1:3]
      kontrollerabarn(ordförsök, slutord, ordlistan, dumbarnen, q)
         
      ordförsök=nod[0:1]+alfabetet[i:i+1]+nod[2:3]
      kontrollerabarn(ordförsök, slutord, ordlistan, dumbarnen, q)
         
      ordförsök=nod[0:2]+alfabetet[i:i+1]
      kontrollerabarn(ordförsök, slutord, ordlistan, dumbarnen, q)


def kontrollerabarn(ordförsök, slutord, ordlistan, dumbarnen, q):
   
   if ordlistan.exists(ordförsök) and not dumbarnen.exists(ordförsök):
      dumbarnen.put(ordförsök)
      q.put(ordförsök)
      
   if ordförsök == slutord:
      print('Det finns en väg till', slutord)    #hittar ingen väg mellan ute-hit. annars ok
      
         
         
   


def huvudprogram():

   print('Hej, och välkommen till programmet!')
   ordlistan=läsinsvenska()
   dumbarnen=skapaträd()
   q=LinkedQ()
   
   startord=input('Vilket ord vill du börja med? ').lower().strip()
   slutord=input('Vilket ord vill du ta dig till? ').lower().strip()
   
   q.put(startord)

   while not q.isEmpty():
      nod=q.get()
      görabarn(nod, slutord, ordlistan, dumbarnen, q)
   
   

huvudprogram()
