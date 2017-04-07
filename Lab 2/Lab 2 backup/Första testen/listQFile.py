class ListQ:
    def __init__(self):
        self.lista=[]

    def put(self, x):
        self.lista.append(x)

    def get(self):
        return self.lista.pop(0)

    def isEmpty(self):
        return len(self.lista)==0

