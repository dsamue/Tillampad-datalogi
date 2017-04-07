#Tilda lab 5.1 - David Samuelsson - CMETE2 - 20140228 

from Nyhashfil2 import *
from hashtest2 import skapaAtomlista, lagraHashtabell
from molgrafik import Ruta, Molgrafik



def huvudprogram():
    atomlista = skapaAtomlista()
    hashtabell = lagraHashtabell(atomlista)
    print("\n-------------------------------------------------------")
    print('\nHej och välkommen till Atomprogrammet!\nAvsluta genom att mata in #')
    svar=input('\nAtombeteckning: ')
    while svar !='#':
        try:
            svar=kollaInmatning(svar)
            vikt=hashtabell.get(svar).vikt
            namn=hashtabell.get(svar).namn
            mg=Molgrafik()
            r=Ruta(namn,vikt)
            mg.show(r)
            print(hashtabell.get(svar).vikt)
            svar=input('\nAtombeteckning: ')
        except KeyError:
            print('Sökt atom finns ej. Försök igen!')
        except ValueError:
            svar='#'
    print('Programmet är avslutat')
        

def kollaInmatning(svar):
    
    if svar=='#':           #kanske lite klumpigt..
        raise ValueError
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


