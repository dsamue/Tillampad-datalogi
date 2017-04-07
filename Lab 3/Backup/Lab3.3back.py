# Tilda Lab 3 - David Samuelsson - CMETE2 - 2014-02-10


from Bintree import *
import re
    
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if svenska.exists(ordet):
           None
           #print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet


engelska = Bintree()
engelsktext=open('engelska.txt', 'r')
allaorden=[]

for rad in engelsktext.readlines():
   rad=rad.strip('\n')
   orden=re.findall(r"[\w']+", rad)   #re.findall returnerar en rena lista med orden i strängen rad (från http://stackoverflow.com/questions/1059559/python-strings-split-with-multiple-separators)
   print(orden)
##   for i in orden:
##      print(i)
##      i=i.strip('!''.'',''"''?')
   allaorden.extend(orden)

'''for rad in engelsktext:
   #print(rad)
   #print(type(rad))
   orden=engelsktext.readline()
   orden=rad.split()
   #print(orden)
   #print(type(orden))
   for i in orden:
      i=i.strip('!''"''"'',''.''?').lower()
   allaorden.extend(orden)
##   for i in allaorden:
##      i=i.strip('!')#('"''!''.'',''"')
   
##   for i in orden:
##      i=i.strip('!''"'',''.''?').lower()
##      allaorden.append(i)'''

s=''
for i in allaorden:
      s+=' '+i
print(s)

for i in allaorden:
   print(i)

'''for i in allaorden:
   print(i.strip('!'))'''

   
   
