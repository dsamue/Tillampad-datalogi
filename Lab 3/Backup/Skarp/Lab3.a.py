# Tilda Lab 3 - David Samuelsson - CMETE2 - 2014-02-10


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


def baklängesfunktion(root,svensktträd,baklängesträd):   # Skicka in ett träds rot och trädet, kolla vilka ord som blir andra ord baklänges och lägg stängar av dessa i nytt träd
  
   if root==None:    #Går igenom svenska trädet i ordning
      return
   
   baklängesfunktion(root.left,svensktträd,baklängesträd) #Kollar vänstra noden..

   
   #Detta händer med varje nod:
   ordpar=''
   baklängesord=root.value[::-1]          #Vänder på ordet     #(Slice från början(:) till slutet(:) i steg om (-1)) 

   if svensktträd.exists(baklängesord):   #Om baklängesordet är ett nytt ord..
      
      if baklängesord<root.value:         #..så skapar vi en sträng med "minsta" ordet först..  #Hade förstås ha kunnat göra ett till datafält i noden..
         ordpar=baklängesord+' '+root.value  
         
      elif baklängesord>root.value:
         ordpar=root.value+' '+baklängesord
            
      elif baklängesord==root.value:
         None
         
   else:                                 #..annars går vi vidare
      None

   if baklängesträd.exists(ordpar):      #Lägger till stängen i baklängesträdet om den inte redan fanns
      None
   else:
      baklängesträd.put(ordpar)
   
   baklängesfunktion(root.right,svensktträd,baklängesträd)   #Kolla högra noden..

   return baklängesträd                                      #Returnerar fyllt träd med ordpar



def huvudprogram():
   
   tomtträd=Bintree()
   svensktträd=läsinsvenska()
   baklängesträd=baklängesfunktion(svensktträd.root,svensktträd,tomtträd)
   baklängesträd.write()


huvudprogram()
   
