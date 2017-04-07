#Tilda lab 5.1 - David Samuelsson - CMETE2 - 20140228 

from Nyhashfil2 import *
from hashtest2 import skapaAtomlista, lagraHashtabell



def huvudprogram():
    atomlista = skapaAtomlista()
    hashtabell = lagraHashtabell(atomlista)
    print("\n-------------------------------------------------------")
    print('\nHej och välkommen till Atomprogrammet!\nAvsluta genom att mata in #')
    while input !='#':
        try:
            svar=input('\nAtombeteckning: ')
            svar=kollaInmatning(svar)
            print(hashtabell.get(svar).vikt)
        except KeyError:
            print('finns ej')

def kollaInmatning(svar):

    if (len(svar)==2 or len(svar)==1) and svar.isalpha():
        if len(svar)==1:
            svar=svar[0].upper()
            return svar
        else:
            svar=svar[0].upper()+svar[1].lower()
            return svar

    else:
        svar=input('Du har angett en ogiltig beteckning. Försök igen: ')
        return kollaInmatning(svar)
        


huvudprogram()
