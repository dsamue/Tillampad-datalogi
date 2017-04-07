# Tilda lab 2 - David Samuelsson Cmete2 - 20140130

class ListQ:                        #Skapar ett kö-objekt
    def __init__(self):
        self.lista=[]

    def put(self, x):               # Lägger till x i kön
        self.lista.append(x)

    def get(self):                  # Returnerar objektet som är längst fram i kön
        return self.lista.pop(0)

    def isEmpty(self):              # Returnerar True om kön är tom, annars False
        return len(self.lista)==0


###Testprogrammet:
##
##q = ListQ()
##q.put(1)
##q.put(2)
##x = q.get()
##y = q.get()
##print(x,y)
