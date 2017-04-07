class LinkedQ(object):

    def __init__(self): 
        """Vilka attribut ska kön ha?"""
        self.first = None
        self.last = None

    def __str__(self):
        
        s = ""
        p = self.first
        while p != None:
            s = s +' ' + str(p.data)
            p = p.next
        return s


    def put(self,x):
        """Stoppar in x sist i kön """
        ny = Node(x)
        if self.first is None:      # Om kön är tom blir det på ett sätt...
            self.first=ny                 # ...som du får tänka ut själv.
            self.last=ny
        else:                   # Annars blir det på ett annat sätt..
            self.last.next=ny
            self.last=ny
            
                        # ...som du också får lura ut själv.


    def get(self):
        """Plockar ut och returnerar det som står först i kön """
        x=self.first.data
        self.first=self.first.next
        if self.first==None:
            self.last=None    #Bara nödvändig för sista objektet.
        else:
            None
        return x

    def isEmpty(self):
        """Returnerar True om kön är tom, False annars """
        return self.first==None


class Node():
    def __init__(self, x, next=None):
        self.data=x
        self.next=None
