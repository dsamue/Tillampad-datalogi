# Tilda lab 2 - David Samuelsson Cmete2 - 20140130

class ListQ:
    def __init__(self):
        self.lista=[]

    def put(self, x):
        self.lista.append(x)

    def get(self):
        return self.lista.pop(0)

    def isEmpty(self):
        return len(self.lista)==0

##kö=ListQ()
##kö.lista
##kö.put(1)
##print(kö.lista)

q=ListQ()
q.put(1)
q.put(2)
x=q.get()
y=q.get()
print(x,y)
q.isEmpty()
