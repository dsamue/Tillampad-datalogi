# Tilda Lab 4 - David Samuelsson - CMETE2 - 2014-02-10 - Hittar snabbast vägen från FAN till GUD


from Bintree import *
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

   '''engelsktext=open('engelska.txt', 'r')
   allaorden=[]

   for rad in engelsktext:     
      orden=re.findall(r"[\w']+", rad)   #re.findall returnerar en lista med orden i strängen rad (från http://stackoverflow.com/questions/1059559/python-strings-split-with-multiple-separators)
      allaorden.extend(orden)

   for i in allaorden:
      i=i.lower()
      if engelska.exists(i):
         None
      else:
          engelska.put(i)             # in i sökträdet
          if annatträd.exists(i):     # Jämför med annat träd
             print(i)'''

   return engelska


def görabarn(startord, ordlistan, dumbarnen):

   dumbarnen.put(startord)
   alfabetet='abcdefghijklmnopqrstuvwxyzåäö'
   

   for i in range(len(alfabetet)):
      
      ordförsök=alfabetet[i:i+1]+startord[1:3]
      if ordlistan.exists(ordförsök) and not dumbarnen.exists(ordförsök):
         print(ordförsök)
         dumbarnen.put(ordförsök)

      ordförsök=startord[0:1]+alfabetet[i:i+1]+startord[2:3]
      if ordlistan.exists(ordförsök) and not dumbarnen.exists(ordförsök):
         print(ordförsök)
         dumbarnen.put(ordförsök)
         
      ordförsök=startord[0:2]+alfabetet[i:i+1]
      if ordlistan.exists(ordförsök) and not dumbarnen.exists(ordförsök):
         print(ordförsök)
         dumbarnen.put(ordförsök)
      
         
         
   


def huvudprogram():

   print('Hej, och välkommen till programmet!')
   ordlistan=läsinsvenska()
   dumbarnen=skapaträd()
   startord=input('Vilket ord vill du börja med?').lower()
   slutord=input('Vilket ord vill du ta dig till?').lower()
   görabarn(startord, ordlistan, dumbarnen)
   
   

huvudprogram()
