# Tilda Lab 3 - David Samuelsson - CMETE2 - 2014-02-10



class Bintree:                      #Binärt sökträd
    def __init__(self):
        self.root=None

    def put(self,newvalue):         #Lägger till ett värde i trädet 
        self.root=putFunc(self.root,newvalue)

    def exists(self,value):         #Kollar om värdet finns i trädet, returnerar True/False
        return existsFunc(self.root,value)

    def write(self):                #Skriver ut all data i trädet i ordning
        writeFunc(self.root)
        print("\n")


class Node:       
   def __init__(self, value=None):
      self.value = value
      self.left = None
      self.right = None
        


def putFunc(root,newvalue):     #Rör sig rekursivt nedåt i trädet tills vi hittar en tom plats
   
    if root==None:              #Om nuvarande root pekar på none, ersätt med ny nod
        root=Node(newvalue)
               
    elif newvalue<root.value:    #Eller om värdet är mindre än nuvarande rot, skicka in vänster nod som ny rot
        root.left=putFunc(root.left,newvalue)
        
    elif newvalue>root.value:   #Eller om värdet är större nuvarande rot, skincka in höger nod som ny rot
        root.right=putFunc(root.right,newvalue)

    return root                 #Returnererar t.ex. "(roten till(roten till(roten till(ny nod))))"

        


def existsFunc(root, value):     #Returnerar True/False beroende om på värdet finns i träder eller ej

    if root==None:            #Om roten är lika med None..
        return False
    
    elif root.value==value:   #..eller om vi hittat värdet.
        return True

    elif root.value>value:    #..eller om värdet är mindre är roten..
        return existsFunc(root.left,value)

    elif root.value<value:    #..eller om väret är större än roten så letar vi oss nedåt via rätt väg
        return existsFunc(root.right,value)


def writeFunc(root):    #Skriver ut träden inorder #insp från http://www.csc.kth.se/utbildning/kth/kurser/2D1343/datae06/grupp1/trad.pdf
   if root==None:      
         return
   writeFunc(root.left)   #Vi går längst ned till vänster i trädet och först när en nod/"lokal rot" pekar på None så skriver vi ut vänster, rot, höger och hoppar upp en nivå
   print(root.value)
   writeFunc(root.right)

