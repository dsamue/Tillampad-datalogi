# Tilda Lab 3 - David Samuelsson - CMETE2 - 2014-02-10


from Bintree import *
import re

def läsinsvenska():
   svenska = Bintree()
   with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
       for rad in svenskfil:
           ordet = rad.strip()                # Ett trebokstavsord per rad
           if svenska.exists(ordet):
              None
              #print(ordet, end = " ") 
           else:
               svenska.put(ordet)             # in i sökträdet
               
   return svenska


def läsinengelska():
   engelska = Bintree()
   engelsktext=open('engelska.txt', 'r')
   allaorden=[]

   for rad in engelsktext:
      
      orden=re.findall(r"[\w']+", rad)   #re.findall returnerar en rena lista med orden i strängen rad (från http://stackoverflow.com/questions/1059559/python-strings-split-with-multiple-separators)
      allaorden.extend(orden)

   for i in allaorden:
      i=i.lower()
      if engelska.exists(i):
         None
      else:
          engelska.put(i)             # in i sökträdet      


   return engelska

svensktträd=läsinsvenska()
engelsktträd=läsinengelska()
   
   
