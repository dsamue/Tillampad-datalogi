from Bintree import *
from LinkedQ import LinkedQ


class ParentNode:
	def __init__(self, word, parent = None):
		self.word = word
		self.parent = parent

	def writechain(self):
		if self.parent != None:
			self.parent.writechain()
			print(self.word)

		




def makechildren(startord, svenska, gamla, q, slutord):
	
	alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
	#letters = list(startord)
	for index in range(len(startord.word)): #själva ordet i objektet
		
		for letter in alphabet: 
			change = startord.word[:index]+letter+startord.word[index+1:]
			#print(change)

			if svenska.exists(change):
				if not gamla.exists(change):
					gamla.put(change)
					nodes = ParentNode(change, startord)  #######måste göra om######Här måste det stå ParentNode(change, startord)  (stod omvänt innan)
					q.put(nodes)






def main():
	q = LinkedQ()
	#orden = ParentNode(startord)
	startord = input("Ange startordet:")
	slutord = input("Ange slutordet:")
	gamla = Bintree()
	svenska = Bintree()
	with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
	   for rad in svenskfil:
	     ordet = rad.strip()
	     svenska.put(ordet)

	gamla.put(startord)
	startnod = ParentNode(startord)
	q.put(startnod) #puttar in objekt istället för sträng

	while not q.isEmpty():
		nod = q.get()
		makechildren(nod, svenska, gamla, q, slutord)
		if nod.word == slutord:     ########## Måste vara nod.word (inte nod)
			print("Det finns en väg till", slutord)
			print(startord)        ####bara för att ni ska få med 'gud'
			nod.writechain()

#########	#makechildren(startord, svenska, gamla, q, slutord)  #Denna rad måste bort för att inte det absolut första startordet ska skickas in som en sträng i funktionen.


main()
