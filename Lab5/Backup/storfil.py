from time import *
from Nyhashfil2 import *      

def lasfil(infil):
    
    songtable = Hashtabell(1048576)
    with open(infil) as fil:
        for rad in fil:
            data = rad.split("<SEP>")
            artist = data[2].strip()
            song = data[3].strip()
            songtable.put(artist,song)
    return songtable

def hitta(artist, songtable):
    start = time()
    print(songtable.get(artist))
    stop = time()
    tidhash = stop - start
    return tidhash

start=time()
songtable = lasfil("unique_tracks.txt")
stop=time()
artist = "Elude"
tidhash = hitta(artist, songtable)
print(tidhash)
print(stop-start)     #Printar tiden för att skapa hashtabellen
