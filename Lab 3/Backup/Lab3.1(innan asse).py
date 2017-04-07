# Tilda Lab 3 - David Samuelsson - CMETE2 - 2014-02-10


class Node:
   def __init__(self, value):
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
        print(self.root)
        #writeFunc(self.root)
        print("\n")

        


def putFunc(node,newvalue):
    None

    if node==None:
        return Node(newvalue)

    elif newvalue<node.value:
        return putFunc(node.left,newvalue)
    
    elif newvalue>node.value:
        return putFunc(node.right,newvalue)        



def existsFunc(nodevalue,value):    # döper om self.root till nodevalue

    if nodevalue==None:
        return False
    
    elif nodevalue==value:
        return True

    elif nodevalue>value:
        return exisitsFunc(nodevalue.left,value)

    elif nodevalue<value:
        return exisitsFunc(nodevalue.right,value)

def writeFunc(nodevalue):
    None
    

