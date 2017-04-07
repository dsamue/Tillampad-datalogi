# Tilda Lab 3 - David Samuelsson - CMETE2 - 2014-02-10


class Node:
   def __init__(self, value=None):
      self.value = value
      self.left = None
      self.right = None

class Bintree:
    def __init__(self):
        self.root=None

    def put(self,newvalue):
        self.root=putFunc(self.root,newvalue)

    def exists(self,value):
        return existsFunc(self.root,value)

    def write(self):
        writeFunc(self.root)
        print("\n")

        


def putFunc(node,newvalue):     #Det blir en return som är typ root av root av root....
   
    if node==None:              #Kanske att första lilla node borde heta root här för att det ska kännas mer naturligt vid varje loop
        node=Node(newvalue)
               
    elif newvalue<node.value:
        node.left=putFunc(node.left,newvalue)
        
    elif newvalue>node.value:
        node.right=putFunc(node.right,newvalue)

    return node

        


def existsFunc(nodevalue,value):    # döper om self.root till nodevalue

    if nodevalue==None:
        return False
    
    elif nodevalue==value:
        return True

    elif nodevalue>value:
        return exisitsFunc(nodevalue.left,value)

    elif nodevalue<value:
        return exisitsFunc(nodevalue.right,value)


def writeFunc(node):    #insp från http://www.csc.kth.se/utbildning/kth/kurser/2D1343/datae06/grupp1/trad.pdf
   if node==None:      
         return
   writeFunc(node.left)
   print(node.value)
   writeFunc(node.right)
    
träd=Bintree()
träd.put(2)
träd.put(3)
träd.put(5)
träd.put(1)
träd.put(2352)
träd.write()


