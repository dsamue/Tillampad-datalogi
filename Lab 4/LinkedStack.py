#Tilda lab 2 - David Samuelsson - CEMTE2 - 140204


class LinkedStack(object):          #Skapar en stack

    def __init__(self): 
        self.top = None

    def __str__(self):              #Skriver ut stacken
        
        s = ""
        p = self.top
        while p != None:
            s = s + str(p.data) + ' '
            p = p.next
        return s


    def push(self,x):               #Stoppar in x överst i stacken       
        ny = Node(x)
        
        if self.top is None:        #Om stacken är tom..     
            self.top=ny
        else:               
            ny.next=self.top
            self.top=ny



    def pop(self):          #Returnerar det som ligger överst i stacken
        x=self.top.data
        self.top=self.top.next
        
        return x


    def isEmpty(self):          #Returnerar True om stacken är tom, annars False.
        return self.top==None



class Node():                   #Det skapas en ny nod för varje objekt. Noderna länkas samman.
    def __init__(self, x, next=None):
        self.data=x
        self.next=None
