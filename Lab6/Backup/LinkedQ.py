class LinkedQ(object):     #Skapar en kö av länkade objekt

    def __init__(self): 
        self.first = None
        self.last = None

    def __str__(self):  #Skriver ut kön
        
        s = ""
        p = self.first
        while p != None:
            s = s +' ' + str(p.data)
            p = p.next
        return s


    def put(self,x):        #Stoppar in x sist i kön 
        ny = Node(x)
        
        if self.first is None:      #Om kön är tom
            self.first=ny                 
            self.last=ny
            
        else:                       #Om kön inte är tom
            self.last.next=ny
            self.last=ny



    def get(self):          #Returnerar första objektet i kön
        x=self.first.data
        self.first=self.first.next
        
        if self.first==None:     #Om vi tar bort första objektet i kön måste last-pekaren ändras
            self.last=None    
        else:
            None
            
        return x


    def isEmpty(self):          #Returnerar True om kön är tom och annars False
        
        return self.first==None

    def peek(self):     # Returnerar första objektet i kön men låter objektet ligga kvar (tjuvtittar). Returnerar None om tom
        if self.first==None:
            return None   #Himla nödlösning för lab6. Bör returnera typ None
        else:
            return self.first.data


class Node():                   #Varje nytt objekt läggs i en nod som länkas samman med övriga noder
    def __init__(self, x, next=None):
        self.data=x
        self.next=None
