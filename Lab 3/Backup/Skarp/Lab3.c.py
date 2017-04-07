# Tilda Lab 3 - David Samuelsson - CMETE2 - 2014-02-10


from Bintree import *
import re
import time

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


def görlista():                              #Returnerar en lista med de svenska orden
   svenskfil=open('word3.txt','r', encoding = "utf-8")
   svenskaord=[]
   
   for rad in svenskfil:
      rad.strip('\n')
      orden=rad.split()
      svenskaord.extend(orden)

   return svenskaord
      


def söklista(s,lista):              #Linjärsökning i listan efter ordet s
   for i in lista:
      if i == s:
         return True                #Om ordet hittas retrneras True (for-loop bryts)
      else:
         None
         
   return False


def jämför(s):                      #Jämför sökning efter strängen s i träd vs. lista
   
   träd=läsinsvenska()
   lista=görlista()

   print('Sökning efter',s,'i träd')           #Sökning i träd
   a=time.time()                               #Tidpunkt a
   print(träd.exists(s))
   b=time.time()                               #Tidpunkt b
   print('Tid för sökningen:',b-a,'sekunder\n')#Tiddifferens b-a

   print('\nLinjärsökning efter',s,'i lista')  #Linjär sökning i lista
   a=time.time()
   print(söklista(s,lista))
   b=time.time()
   print('Tid för sökningen:',b-a,'sekunder\n')

   print('\nTest med sökning efter',s,'i "ord in lista"')
   a=time.time()
   print(s in lista)                   #Ville bara testa denna också
   b=time.time()
   print('Tid för sökningen:',b-a,'sekunder\n')


jämför('fax')


