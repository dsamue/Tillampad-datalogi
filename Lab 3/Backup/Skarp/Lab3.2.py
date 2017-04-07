# Tilda Lab 3 - David Samuelsson - CMETE2 - 2014-02-10


from Bintree import *
    
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if svenska.exists(ordet):
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")
