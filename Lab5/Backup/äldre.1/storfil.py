# -*- coding: utf-8 -*-
from time import *
from Nyhashfil import *

class Node:
    def __init__(self,key,data,next=None):
        self.key=key
        self.data=data
        self.next=next    #ändrade från None till next..

class Musikobjekt:
    def __init__(self,artist,titel,next=None):
        self.namn=artist
        self.vikt=titel
        self.next=next    #ändrade från None till next..        

def lasfil(infil):
    
    #infil=open("direkt.txt")
    #print(type(infil))
    songtable = Hashtabell(1000000)
    #infil=infil.unicode(infil)
    #infil=infil.decode('utf-8')
    with open(infil) as fil:
        #fil=fil.encode('utf-8')
        for rad in fil:
            data = rad.split("<SEP>")
            artist = data[2].strip()
            song = data[3].strip()
            musikobjekt=Musikobjekt(artist,song)
            songtable.put(artist,musikobjekt)
    return songtable

def hitta(artist, songtable):
    start = time()
    print(songtable.get(artist).vikt)
    stop = time()
    tidhash = stop - start
    return tidhash

songtable = lasfil("unique_tracks.txt")
artist = "Elude"
tidhash = hitta(artist, songtable)
print(tidhash)
